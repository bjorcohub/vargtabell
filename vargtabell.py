import streamlit as st
from collections import defaultdict
import re

st.title("VARG City Organizer and Bullet Calculator")

search_input = st.text_area("Paste your VARG search here:", height=200)
table_input = st.text_area("Paste your organized table here:", height=200)

# Organizer logic (already working)
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

# Bullet converter now reading VARG number directly
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

# Organizer button
if st.button("Organize VARG Search"):
    if search_input:
        organized_output = organize_varg_search(search_input)
        st.text_area("Organized VARGs:", organized_output, height=400)
        st.download_button("Download Organized VARGs", organized_output.encode("utf-8"), "organized_vargs.txt")
    else:
        st.warning("Please enter a VARG search.")

# Converter button
if st.button("Convert Table to Include Bullets"):
    if table_input:
        bullet_output = convert_table_with_bullets(table_input)
        st.text_area("Bullet-Converted Table:", bullet_output, height=400)
        st.download_button("Download Bullet-Converted Table", bullet_output.encode("utf-8"), "bullet_table.txt")
    else:
        st.warning("Please enter an organized table.")
