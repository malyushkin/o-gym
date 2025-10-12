import os
import re
import sys
import yaml
import pathlib
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent

IGNORE_DIRS = {
    ".git",
    ".idea",
    ".mypy_cache",
    ".pytest_cache",
    ".venv",
    ".vscode",
    "__pycache__",
    "node_modules"
    "venv",
}

# Match 123.py or 123_easy.py / 123_medium.py / 123_hard.py
PY_FILE = re.compile(r"^(\d+)(?:_(easy|medium|hard))?\.py$", re.I)


def pct(a: int, b: int) -> int:
    return 0 if b == 0 else round(100 * a / b)


def badge(label: str, value: str, color: str) -> str:
    text = urllib.parse.quote(f"{label}-{value}", safe="")
    return f"![{label}](https://img.shields.io/badge/{text}-{color})"


def color_for(progress: int) -> str:
    if progress == 100:
        return "brightgreen"
    if progress >= 75:
        return "green"
    if progress >= 50:
        return "yellowgreen"
    if progress >= 25:
        return "yellow"
    if progress > 0:
        return "orange"
    return "lightgrey"


def find_plan_dirs():
    # Looks for **/plan.yaml
    for y in ROOT.glob("**/plan.yaml"):
        yield y.parent


def scan_solutions(plan_dir: pathlib.Path) -> dict:
    # Returns { problem_id: {path, level_hint} }
    found = {}
    for dp, dirnames, filenames in os.walk(plan_dir):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for fn in filenames:
            m = PY_FILE.match(fn)
            if not m:
                continue
            pid = int(m.group(1))
            lvl = (m.group(2) or "").lower() or None
            rel = str(pathlib.Path(dp, fn).relative_to(plan_dir)).replace("\\", "/")
            if pid not in found:  # first wins
                found[pid] = {"path": rel, "level": lvl}
    return found


def load_plan(plan_dir: pathlib.Path) -> dict:
    with open(plan_dir / "plan.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def render_plan_readme(plan_dir: pathlib.Path, plan: dict, solutions: dict):
    name = plan.get("name", "Study Plan")
    url = plan.get("url", "")
    desc = (plan.get("description") or "").strip()
    sections = plan.get("sections", [])

    total = sum(len(s.get("problems", [])) for s in sections)
    solved = sum(1 for s in sections for it in s.get("problems", []) if it["id"] in solutions)
    tp = pct(solved, total)

    lines = []
    lines.append(f"# {name}\n")
    lines.append(badge("Total_Progress", f"{solved}/{total} ({tp}%)", "blue"))
    lines.append("")
    if url:
        lines.append(f"This repository contains my solutions to the [{name}]({url}).")
    else:
        lines.append(f"This repository contains my solutions to the {name}.")
    if desc:
        lines.append("")
        lines.append(desc)
    lines.append("")

    for sec in sections:
        sec_name = sec["name"]
        # items = sorted(sec.get("problems", []), key=lambda x: int(x["id"]))
        items = sec.get("problems", [])
        solved_here = sum(1 for it in items if it["id"] in solutions)
        ph = pct(solved_here, len(items))

        lines.append(f"## {sec_name}\n")
        lines.append(f"({solved_here}/{len(items)})  ")
        lines.append(badge("Progress", f"{ph}%", color_for(ph)))
        lines.append("")
        lines.append("| #    | Problem | Level | Solution |")
        lines.append("|------|---------|-------|----------|")

        for it in items:
            pid = int(it["id"])
            title = it["title"]
            sol = solutions.get(pid)
            level = (sol and sol["level"].title()) or (it.get("level") or "Unknown")
            level = f"`{level}`"
            if sol:
                link_text = f"{pid}.py"  # display clean name even if file is 123_easy.py
                lines.append(f"| {pid:<4} | {title} | {level} | [{link_text}]({sol['path']}) |")
            else:
                lines.append(f"| {pid:<4} | {title} | {level} | _TBA_ |")
        lines.append("")

    (plan_dir / "README.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return solved, total, name, plan_dir


def render_root_readme(summary: list):
    """
    summary: list of (platform, name, solved, total, rel_dir)
    """
    total_solved = sum(s for _, _, s, _, _ in summary)
    total_all = sum(t for _, _, _, t, _ in summary)

    lines = []
    lines.append("# Coding Study Plans\n")
    lines.append(badge("Overall_Progress", f"{total_solved}/{total_all} ({pct(total_solved, total_all)}%)", "blue"))
    lines.append("")
    lines.append("| Platform | Plan | Solved | Progress |")
    lines.append("|----------|------|--------|----------|")
    for platform, name, solved, total, rel in summary:
        prog = pct(solved, total)
        lines.append(
            f"| {platform or '-'} | [{name}]({rel}/README.md) | **{solved}/{total}** | {badge('Progress', f'{prog}%', color_for(prog))} |")
    lines.append("")

    (ROOT / "README.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main():
    plans = list(find_plan_dirs())
    if not plans:
        print("No plans found (expected **/studyplans/*/plan.yaml).", file=sys.stderr)
        sys.exit(1)

    summary = []
    for plan_dir in plans:
        plan = load_plan(plan_dir)
        sols = scan_solutions(plan_dir)
        s, t, name, pdir = render_plan_readme(plan_dir, plan, sols)
        rel = str(pathlib.Path(pdir).relative_to(ROOT)).replace("\\", "/")
        platform = plan.get("platform", "")
        summary.append((platform, name, s, t, rel))

    render_root_readme(summary)


if __name__ == "__main__":
    main()
