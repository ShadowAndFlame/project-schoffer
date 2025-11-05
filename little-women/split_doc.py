import re
import os

source_file = "source/staging.tex"

chapter_pattern = r"(?=\\chapter)"

with open(source_file) as f:
    text = f.read()

chapters = re.split(chapter_pattern, text)

for chapter, chapter_text in enumerate(chapters):
    # skip empty first split
    if not chapter_text:
        continue
    # Only two parts
    part = 1 if chapter < 24 else 2
    # Write chapter file
    chapter_ref = f"chapters/part{part}/chapter{chapter:02d}"
    chapter_file = chapter_ref + ".tex"
    os.makedirs(os.path.dirname(chapter_file), exist_ok=True)
    with open(chapter_file, 'w') as f:
        f.write(chapter_text)
    # Write part file
    part_ref = f"parts/part{part}"
    part_file = part_ref + ".tex"
    os.makedirs(os.path.dirname(part_file), exist_ok=True)
    if not os.path.isfile(part_file):
        with open(part_file, 'w') as f:
            f.write("\\part{}\n\n")
    with open(part_file, 'a') as f:
        f.write(f"\\input{{{chapter_ref}}}\n")
