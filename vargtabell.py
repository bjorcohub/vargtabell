import streamlit as st

def get_rank_and_bullets(rank_number):
    if 1 <= rank_number <= 58:
        return "Wannabe", 16000
    elif 59 <= rank_number <= 106:
        return "Bråkmaker", 25000
    elif 107 <= rank_number <= 144:
        return "Gangster", 45000
    elif 145 <= rank_number <= 172:
        return "Hitman", 65000
    elif 173 <= rank_number <= 191:
        return "Assassin", 90000
    elif 192 <= rank_number <= 200:
        return "Kaptein", 125000
    return "Sivilist", 10500


def calculate_bullets(input_text):
    output = []
    lines = input_text.strip().splitlines()
    city_name = ""
    for line in lines:
        if line.isalpha():  # City name
            city_name = line
            output.append(f"{city_name}")
        elif line.startswith("VARG"):
            try:
                rank_number = int(line[4:])
                rank, bullets = get_rank_and_bullets(rank_number)
                output.append(f"{line}: {bullets}")
            except ValueError:
                output.append(f"{line}: Invalid rank number")
        else:
            output.append(line)
    return "\n".join(output)


# Streamlit UI
title = "VARG Bullet Calculator"
st.title(title)

st.write("Paste your VARG list below and click the button to calculate bullets:")

input_text = st.text_area("VARG List")
if st.button("Calculate Bullets"):
    if input_text:
        result = calculate_bullets(input_text)
        st.text_area("Bullet Calculation Result", result, height=300)
    else:
        st.warning("Please enter your VARG list.")
