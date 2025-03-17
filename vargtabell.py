import streamlit as st
from collections import defaultdict
import re

st.title("VARG City Organizer")

# Input text area
input_text = st.text_area("Paste your VARG list here:", height=400)

if st.button("Organize VARGs"):
    if input_text:
        # Dictionary to hold cities and their VARG numbers
        city_vargs = defaultdict(list)

        # Process each line
        for line in input_text.splitlines():
            # Match the line format for the new search list
            match = re.match(r"^(VARG\d+)\s+([A-Za-zÆØÅæøå]+)", line)
            if match:
                varg_number = match.group(1)
                city_name = match.group(2)
                city_vargs[city_name].append(varg_number)

        # Display results
        organized_output = ""
        for city, vargs in sorted(city_vargs.items()):
            organized_output += f"{city}:\n"
            for varg in sorted(vargs):
                organized_output += f"{varg}\n"
            organized_output += "- - -\n"

        # Output the organized list
        st.text_area("Organized VARGs:", organized_output, height=400)
        
        # Option to download the organized list
        st.download_button("Download Organized VARGs", organized_output.encode("utf-8"), "organized_vargs.txt")
    else:
        st.warning("Please enter a VARG list.")
