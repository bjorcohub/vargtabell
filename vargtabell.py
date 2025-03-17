import streamlit as st
import re

def calculate_bullets(rank):
    if 1 <= rank <= 58:
        return 16000
    elif 59 <= rank <= 106:
        return 25000
    elif 107 <= rank <= 144:
        return 45000
    elif 145 <= rank <= 172:
        return 65000
    elif 173 <= rank <= 191:
        return 90000
    elif 192 <= rank <= 200:
        return 125000
    return 0

st.title("VARG Search and Table Organizer")

input_text = st.text_area("Paste VARG search result or organized table:")

if st.button("Organize and Calculate Bullets"):
    if not input_text.strip():
        st.warning("Please paste a search result or organized table.")
    else:
        city_vargs = {}
        current_city = None

        for line in input_text.splitlines():
            line = line.strip()

            if line.endswith(":"):
                current_city = line[:-1]
                city_vargs[current_city] = []
            else:
                match = re.match(r"^(\d+)-\d+\s+(.+)$", line)
                if match:
                    rank = int(match.group(1))
                    name = match.group(2)
                    bullets = calculate_bullets(rank)
                    city_vargs[current_city].append(f"{name} ({rank}) - {bullets} bullets")

        organized_output = []
        for city, vargs in city_vargs.items():
            organized_output.append(f"{city}:")
            organized_output.extend(vargs)
            organized_output.append("")

        st.text("\n".join(organized_output))
