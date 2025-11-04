import re

source_file = "source/staging.tex"
dest_dir = "chapters"

subsection_pattern = r"(?=\\subsection)"

with open(source_file) as f:
    text = f.read()

chapters = re.split(subsection_pattern, text)

part = 1
for chapter, chapter_text in enumerate(chapters):
    if chapter == 24:
        part = 2
    chapter_file = f"{dest_dir}/part{part}/chapter{chapter:02d}.tex"
    with open(chapter_file, 'w') as f:
        f.write(chapter_text)
    # append to parts here