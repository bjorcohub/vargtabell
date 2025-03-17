import streamlit as st
import pandas as pd
import re

def process_raw_search(raw_search):
    # Extract city and VARG names from the raw search
    pattern = r"(\w+),\s*(.*)"
    matches = re.findall(pattern, raw_search)
    organized_data = {}

    for city, names in matches:
        varg_names = [name.strip() for name in names.split(',')]
        organized_data[city] = varg_names

    return organized_data


def process_organized_table(table_text):
    # Convert the organized table into a dictionary format
    organized_data = {}
    for line in table_text.strip().split('\n'):
        city, *varg_names = line.split(', ')
        organized_data[city] = varg_names

    return organized_data


def calculate_bullets(organized_data):
    bullets = {city: len(names) * 3 for city, names in organized_data.items()}
    return bullets


def display_table(organized_data, bullets):
    rows = []
    for city, names in organized_data.items():
        bullet_count = bullets.get(city, 0)
        row = [city] + names + [str(bullet_count)]
        rows.append(row)

    df = pd.DataFrame(rows)
    st.write(df)


st.title("VARG Search and Table Organizer")

input_text = st.text_area("Paste VARG search result or organized table:")

if st.button("Process"):
    if re.search(r",\s*", input_text):
        organized_data = process_raw_search(input_text)
    else:
        organized_data = process_organized_table(input_text)

    bullets = calculate_bullets(organized_data)
    display_table(organized_data, bullets)
