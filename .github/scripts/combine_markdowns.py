import os
import sys
from pathlib import Path
from datetime import datetime
import markdown

# ===== SETTINGS =====
EXCLUDE_FILES = {"README.md"}
OUTPUT_FILE = Path(__file__).resolve().parents[2] / "README.md"
HEADER = "# Repository Documentation\n\n"  # optional custom header
SEPARATOR = "\n\n---\n\n"  # separates files in combined output
LOG_FILE = Path(__file__).resolve().parents[2] / "combine_markdowns.log"
LIST_HTML_FILE = Path(__file__).resolve().parents[2] / "list.html"

def log(message: str):
    """Write log messages to both stdout and log file."""
    timestamp = datetime.utcnow().strftime("[%Y-%m-%d %H:%M:%S UTC]")
    formatted = f"{timestamp} {message}"
    print(formatted)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(formatted + "\n")

def collect_markdowns(root="."):
    """Collect all markdown files only from the root directory."""
    log(f"Scanning only root directory: {os.path.abspath(root)}")
    log(f"Ignoring subfolders under: {Path(root).resolve()}")

    md_files = []
    for path in Path(root).glob("*.md"):  # non-recursive search
        if path.name in EXCLUDE_FILES:
            log(f"Skipping excluded file: {path}")
            continue
        md_files.append(path)

    md_files_sorted = sorted(md_files)
    log(f"Found {len(md_files_sorted)} markdown files in root.")
    for p in md_files_sorted:
        log(f" - {p}")
    return md_files_sorted

def convert_to_html(md_file: Path):
    """Convert a single markdown file to HTML."""
    try:
        content = md_file.read_text(encoding="utf-8")
        html_content = markdown.markdown(content, extensions=["fenced_code", "tables"])
        html_output_path = md_file.with_suffix(".html")
        html_output_path.write_text(html_content, encoding="utf-8")
        log(f"✅ Converted {md_file.name} → {html_output_path.name}")
        return html_output_path
    except Exception as e:
        log(f"❌ Failed to convert {md_file}: {e}")
        return None

def generate_list_html(html_files):
    """Generate list.html with links to all converted HTML files."""
    try:
        html_list_items = "\n".join(
            [f'<li><a href="{html_file.name}" target="_blank">{html_file.stem}</a></li>'
             for html_file in html_files]
        )
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Markdown File List</title>
<style>
body {{ font-family: Arial, sans-serif; margin: 40px; }}
h1 {{ color: #2c3e50; }}
li {{ margin: 8px 0; }}
a {{ text-decoration: none; color: #3498db; }}
a:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
<h1>Markdown to HTML Files</h1>
<ul>
{html_list_items}
</ul>
</body>
</html>"""
        LIST_HTML_FILE.write_text(html_content, encoding="utf-8")
        log(f"✅ Created list.html at {LIST_HTML_FILE}")
    except Exception as e:
        log(f"❌ Failed to create list.html: {e}")

def combine_markdowns(md_files):
    """Combine markdown content."""
    log("Combining markdown files...")
    combined = [HEADER]
    for md in md_files:
        rel_path = md.relative_to(Path("."))
        log(f"Adding file: {rel_path}")
        try:
            content = md.read_text(encoding="utf-8")
        except Exception as e:
            log(f"⚠️ Error reading {md}: {e}")
            content = ""
        combined.append(f"## {rel_path}\n\n{content}")
    log("Finished combining markdown files.")
    return SEPARATOR.join(combined)

def main():
    log("=" * 70)
    log("🟢 Starting Markdown Combination & Conversion Process")
    log(f"Script path: {Path(__file__).resolve()}")
    log(f"Output file: {OUTPUT_FILE}")

    md_files = collect_markdowns()
    if not md_files:
        log("⚠️ No markdown files found. Exiting.")
        return

    # Combine markdowns
    combined = combine_markdowns(md_files)

    # Write combined markdown to README.md
    try:
        OUTPUT_FILE.write_text(combined, encoding="utf-8")
        log(f"✅ Successfully wrote combined markdown to: {OUTPUT_FILE}")
    except Exception as e:
        log(f"❌ Failed to write output: {e}")
        sys.exit(1)

    # Convert each markdown to HTML
    html_files = []
    for md in md_files:
        html_file = convert_to_html(md)
        if html_file:
            html_files.append(html_file)

    # Create list.html linking all HTMLs
    if html_files:
        generate_list_html(html_files)
    else:
        log("⚠️ No HTML files were generated.")

    log("🟩 All processes completed successfully.")
    log("=" * 70)

if __name__ == "__main__":
    main()
