import os
import sys
from pathlib import Path
from datetime import datetime

# ===== SETTINGS =====
EXCLUDE_FILES = {"README.md"}
OUTPUT_FILE = Path(__file__).resolve().parents[2] / "README.md"
HEADER = "# Repository Documentation\n\n"  # optional custom header
SEPARATOR = "\n\n---\n\n"  # separates files in combined output
LOG_FILE = Path(__file__).resolve().parents[2] / "combine_markdowns.log"

def log(message: str):
    """Write log messages to both stdout and log file."""
    timestamp = datetime.utcnow().strftime("[%Y-%m-%d %H:%M:%S UTC]")
    formatted = f"{timestamp} {message}"
    print(formatted)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(formatted + "\n")

def collect_markdowns(root="."):
    """Collect all markdown files except excluded ones."""
    log(f"Scanning directory: {os.path.abspath(root)}")
    md_files = []
    for path in Path(root).rglob("*.md"):
        if path.name in EXCLUDE_FILES:
            log(f"Skipping excluded file: {path}")
            continue
        if ".github" in path.parts:
            log(f"Skipping .github file: {path}")
            continue
        md_files.append(path)
    md_files_sorted = sorted(md_files)
    log(f"Found {len(md_files_sorted)} markdown files to combine.")
    for p in md_files_sorted:
        log(f" - {p}")
    return md_files_sorted

def combine_markdowns(md_files):
    """Combine markdown content."""
    log("Combining markdown files...")
    combined = [HEADER]
    for md in md_files:
        rel_path = md.relative_to(Path("."))
        log(f"Adding file: {rel_path}")
        combined.append(f"## {rel_path}\n\n")
        try:
            content = md.read_text(encoding="utf-8")
        except Exception as e:
            log(f"⚠️ Error reading {md}: {e}")
            content = ""
        combined.append(content)
    log("Finished combining markdown files.")
    return SEPARATOR.join(combined)

def main():
    log("=" * 70)
    log("🟢 Starting Markdown Combination Process")
    log(f"Script path: {Path(__file__).resolve()}")
    log(f"Output file: {OUTPUT_FILE}")

    md_files = collect_markdowns()
    if not md_files:
        log("⚠️ No markdown files found. Exiting.")
        return

    combined = combine_markdowns(md_files)

    # Write to README.md
    try:
        OUTPUT_FILE.write_text(combined, encoding="utf-8")
        log(f"✅ Successfully wrote combined markdown to: {OUTPUT_FILE}")
    except Exception as e:
        log(f"❌ Failed to write output: {e}")
        sys.exit(1)

    log("🟩 Markdown combination process completed successfully.")
    log("=" * 70)

if __name__ == "__main__":
    main()
