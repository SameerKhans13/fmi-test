# build_masterclass.py
import json
import slides_data_part1
import append_part1
import append_part1_b
import slides_part2_a
import slides_part2_b
import slides_part3_a
import slides_part3_b

all_slides = (
    slides_data_part1.slides_part1[:10] +
    append_part1.new_slides +
    append_part1_b.slides_21_to_35 +
    slides_part2_a.slides_36_to_52 +
    slides_part2_b.slides_53_to_70 +
    slides_part3_a.slides_71_to_86 +
    slides_part3_b.slides_87_to_102
)

print(f"Total slides loaded: {len(all_slides)}")

slides_json = json.dumps(all_slides, ensure_ascii=False)

with open("masterclass_template.html", "r", encoding="utf-8") as f:
    template = f.read()

output_html = template.replace("__SLIDES_DATA__", slides_json)

with open("fmi_master_class.html", "w", encoding="utf-8") as f:
    f.write(output_html)

print(f"Successfully compiled fmi_master_class.html ({len(output_html)} bytes) with {len(all_slides)} slides!")
