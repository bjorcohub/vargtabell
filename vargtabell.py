import streamlit as st
from collections import defaultdict
import re

st.title("VARG & Player Organizer + Bullet Calculator")

if "input_text" not in st.session_state:
    st.session_state.input_text = ""
if "output_text" not in st.session_state:
    st.session_state.output_text = ""

# Organizer logic that handles both VARGs and usernames
def organize_search(input_text):
    city_entries = defaultdict(list)
    for line in input_text.splitlines():
        # Match both VARG and usernames with city
        match = re.match(r"^(\S+)\s+([A-Za-zÆØÅæøå]+)\s", line)
        if match:
            name = match.group(1)
            city = match.group(2)
            city_entries[city].append(name)

    organized_output = ""
    for city, names in sorted(city_entries.items()):
        organized_output += f"{city}:\n"
        for name in sorted(names):
            organized_output += f"{name}\n"
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

# Bullet converter logic (only affects VARGs)
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

# Callback functions
def handle_organize():
    st.session_state.input_text = organize_search(st.session_state.input_text)

def handle_convert():
    st.session_state.output_text = convert_table_with_bullets(st.session_state.input_text)

# Layout
st.text_area("Paste your search data here:", key="input_text", height=300)

col1, col2 = st.columns(2)
with col1:
    st.button("Organize Search", on_click=handle_organize)
with col2:
    st.button("Convert to Bullets", on_click=handle_convert)

if st.session_state.output_text:
    st.text_area("Output:", st.session_state.output_text, height=400)
    st.download_button("Download Output", st.session_state.output_text.encode("utf-8"), "output.txt")
