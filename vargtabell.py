import streamlit as st
from collections import defaultdict
import re

st.title("VARG Organizer & Bullet Calculator")

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# The input field is bound to session state
st.text_area("Paste your VARG data here:", key="input_text", height=300)
output_text = ""

# Organizer logic
def organize_varg_search(input_text):
    city_vargs = defaultdict(list)
    for line in input_text.splitlines():
        match = re.match(r"^(VARG\d+)\s+([A-Za-zÆØÅæøå]+)", line)
        if match:
            varg_number = match.group(1)
            city_name = match.group(2)
            city_vargs[city_name].append(varg_number)

    organized_output = ""
    for city, vargs in sorted(city_vargs.items()):
        organized_output += f"{city}:\n"
        for varg in sorted(vargs):
            organized_output += f"{varg}\n"
        organized_output += "- - -\n"
    return organized_output

# Bullet calculation logic
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

# Bullet converter logic
def convert_table_with_bullets(input_text):
    bullet_output = ""
    total_bullets = 0

    for line in input_text.splitlines():
        match = re.match(r"^(VARG(\d+))", line)
        if match:
            varg = match.group(1)
            rank_number = int(match.group(2))
            bullets = calculate_bullets(rank_number)
            total_bullets += bullets
            bullet_output += f"{varg} {bullets}\n"
        else:
            bullet_output += f"{line}\n"

    bullet_output += f"Total Bullets: {total_bullets}\n"
    return bullet_output

col1, col2 = st.columns(2)

with col1:
    if st.button("Organize Search"):
        if st.session_state.input_text:
            st.session_state.input_text = organize_varg_search(st.session_state.input_text)
        else:
            st.warning("Please paste your VARG data.")

with col2:
    if st.button("Convert to Bullets"):
        if st.session_state.input_text:
            output_text = convert_table_with_bullets(st.session_state.input_text)
        else:
            st.warning("Please paste your VARG data.")

if output_text:
    st.text_area("Output:", output_text, height=400)
    st.download_button("Download Output", output_text.encode("utf-8"), "output.txt")
