# verify_slides.py
import slides_data_part1, append_part1, append_part1_b, slides_part2_a, slides_part2_b, slides_part3_a, slides_part3_b

all_slides = (
    slides_data_part1.slides_part1[:10] +
    append_part1.new_slides +
    append_part1_b.slides_21_to_35 +
    slides_part2_a.slides_36_to_52 +
    slides_part2_b.slides_53_to_70 +
    slides_part3_a.slides_71_to_86 +
    slides_part3_b.slides_87_to_102
)

print(f"Total slides compiled: {len(all_slides)}")

dollar_count = 0
for s in all_slides:
    for field in ['title', 'subtitle', 'content_html', 'visual_html']:
        val = s.get(field, '')
        if '$' in val:
            print(f"Slide {s['id']} has raw dollar sign in {field}!")
            dollar_count += 1

print(f"Total raw dollar count across all 102 slides: {dollar_count}")
