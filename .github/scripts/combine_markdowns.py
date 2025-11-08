import os
from pathlib import Path

# ===== SETTINGS =====
EXCLUDE_FILES = {"README.md"}
OUTPUT_FILE = "README.md"
HEADER = "# Repository Documentation\n\n"  # optional custom header
SEPARATOR = "\n\n---\n\n"  # separates files in combined output

def collect_markdowns(root="."):
    """Collect all markdown files except excluded ones."""
    md_files = []
    for path in Path(root).rglob("*.md"):
        if path.name not in EXCLUDE_FILES and ".github" not in path.parts:
            md_files.append(path)
    return sorted(md_files)

def combine_markdowns(md_files):
    """Combine markdown content."""
    combined = [HEADER]
    for md in md_files:
        rel_path = md.relative_to(Path("."))
        combined.append(f"## {rel_path}\n\n")
        combined.append(md.read_text(encoding="utf-8"))
    return SEPARATOR.join(combined)

def main():
    md_files = collect_markdowns()
    if not md_files:
        print("No markdown files found.")
        return

    combined = combine_markdowns(md_files)
    Path(OUTPUT_FILE).write_text(combined, encoding="utf-8")
    print(f"✅ Combined {len(md_files)} markdown files into {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
