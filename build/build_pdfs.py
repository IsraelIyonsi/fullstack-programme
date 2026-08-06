#!/usr/bin/env python3
"""Render week-NN.md files into styled A4 PDFs, then zip them.

Each markdown file starts with a simple key: value frontmatter block delimited
by ---. Body is markdown with tables, fenced code and blockquotes enabled.
"""

import html
import pathlib
import re
import shutil
import subprocess
import sys
import zipfile

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
DIST = ROOT / "dist"
PDFS = DIST / "pdfs"
CSS = ROOT / "build" / "print.css"

PHASE_ACCENT = {
    "Phase 1": "#1f6feb",
    "Phase 2": "#7d4cdb",
    "Phase 3": "#0f8b8d",
    "Phase 4": "#c2410c",
    "Phase 5": "#9333ea",
    "Phase 6": "#166534",
}

LICENSE_CLASS = {"Red": "red", "Yellow": "yellow", "Green": "green"}


def parse(path):
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        raise SystemExit(f"{path.name}: missing frontmatter")
    _, fm, body = raw.split("---", 2)
    meta = {}
    for line in fm.strip().splitlines():
        if not line.strip():
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip()
    return meta, body.strip()


CHECK_LINE = re.compile(r"^- \[ \] (.+)$")


def inline(text):
    """Minimal inline markdown for checklist items: code spans and bold."""
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def checklists(body):
    """Turn runs of '- [ ] item' lines into a styled checklist block."""
    out, buf = [], []

    def flush():
        if buf:
            items = "".join(f'<li class="checklist">{inline(i)}</li>' for i in buf)
            out.append(f'<ul class="checklist">{items}</ul>\n')
            buf.clear()

    for line in body.splitlines():
        m = CHECK_LINE.match(line)
        if m:
            buf.append(m.group(1).strip())
        else:
            flush()
            out.append(line)
    flush()
    return "\n".join(out)


def render(path):
    meta, body = parse(path)
    body = checklists(body)
    week = meta["week"]
    phase_key = meta["phase"].split(" ")[0] + " " + meta["phase"].split(" ")[1]
    accent = PHASE_ACCENT.get(phase_key, "#1f6feb")
    lic = meta.get("license", "Yellow")
    lic_class = LICENSE_CLASS.get(lic.split()[0], "yellow")

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "attr_list", "sane_lists", "md_in_html"]
    )
    content_html = md.convert(body)

    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Week {week} - {html.escape(meta['title'])}</title>
<style>:root {{ --accent: {accent}; --weeknum-text: "{week}"; }}</style>
</head><body>
<header class="masthead">
  <div class="eyebrow">
    <span>Week {week} &nbsp;/&nbsp; {html.escape(meta['phase'])}</span>
    <span class="right">{html.escape(meta.get('track', 'Full Stack'))}</span>
  </div>
  <h1 class="week-title">{html.escape(meta['title'])}</h1>
  <p class="standfirst">{html.escape(meta['standfirst'])}</p>
  <div class="metastrip">
    <div class="cell"><span class="k">Backend focus</span>
      <span class="v">{html.escape(meta['backend'])}</span></div>
    <div class="cell"><span class="k">Frontend focus</span>
      <span class="v">{html.escape(meta['frontend'])}</span></div>
    <div class="cell"><span class="k">AI licence</span>
      <span class="v"><span class="dot {lic_class}"></span>{html.escape(lic)}</span></div>
    <div class="cell"><span class="k">Time budget</span>
      <span class="v">{html.escape(meta.get('hours', '25 to 30 hrs'))}</span></div>
  </div>
</header>
{content_html}
<p class="footer-note">Week {week} of 24. Hand this in before the next session.
Nothing counts as done until you can explain it out loud with the editor closed.</p>
</body></html>"""

    slug = re.sub(r"[^a-z0-9]+", "-", meta["title"].lower()).strip("-")
    out = PDFS / f"Week-{week}-{slug}.pdf"
    tmp = DIST / "_tmp.html"
    tmp.write_text(doc, encoding="utf-8")
    subprocess.run(
        ["weasyprint", "-s", str(CSS), str(tmp), str(out)],
        check=True, capture_output=True,
    )
    tmp.unlink()
    return out


def main():
    PDFS.mkdir(parents=True, exist_ok=True)
    targets = sorted(CONTENT.glob("week-*.md"))
    if len(sys.argv) > 1:
        targets = [t for t in targets if any(a in t.name for a in sys.argv[1:])]
    if not targets:
        raise SystemExit("no content files matched")
    for t in targets:
        out = render(t)
        print(f"  {out.name}  ({out.stat().st_size // 1024} KB)")

    if len(sorted(CONTENT.glob("week-*.md"))) == len(sorted(PDFS.glob("*.pdf"))):
        zpath = DIST / "fullstack-6-month-curriculum.zip"
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
            for p in sorted(PDFS.glob("*.pdf")):
                z.write(p, f"Full Stack Curriculum/{p.name}")
            readme = ROOT / "dist" / "START-HERE.pdf"
            if readme.exists():
                z.write(readme, "Full Stack Curriculum/START-HERE.pdf")
        print(f"\nzipped -> {zpath} ({zpath.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
