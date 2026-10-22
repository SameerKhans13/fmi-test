# qa_check.py
import json

with open("fmi_master_class.html", "r", encoding="utf-8") as f:
    html = f.read()

print(f"File size: {len(html)} characters")

# Check for unrendered latex dollar signs
# Note: we need to distinguish between JS template string or jQuery if any and LaTeX math $...$
# In our HTML/JS template, let's see where $ appears
dollar_lines = []
for i, line in enumerate(html.splitlines()):
    if "$" in line:
        dollar_lines.append((i+1, line.strip()))

print(f"Total lines with '$': {len(dollar_lines)}")
for line_num, text in dollar_lines[:20]:
    print(f"Line {line_num}: {text[:100]}")

# Check for unicode replacement character \ufffd
replacement_count = html.count("\ufffd")
print(f"Unicode replacement characters (\\ufffd): {replacement_count}")

# Check for rupee sign
rupee_count = html.count("\u20b9")
print(f"Rupee symbols count: {rupee_count}")

# Extract JSON and test parse
marker = "const slides = "
start = html.find(marker) + len(marker)
end = html.find(";\n        let currentSlideIdx = 0;", start)
json_str = html[start:end]
slides = json.loads(json_str)
print(f"Parsed {len(slides)} slides successfully from HTML!")

# Check all slide IDs
ids = [s["id"] for s in slides]
assert len(ids) == 102
assert sorted(ids) == list(range(1, 103))
print("All slide IDs from 1 to 102 are present and valid!")
