import streamlit as st

RANKS = {
    'Wannabe': (1, 58, 16000),
    'Bråkmaker': (59, 106, 25000),
    'Gangster': (107, 144, 45000),
    'Hitman': (145, 172, 65000),
    'Assassin': (173, 191, 90000),
    'Kaptein': (192, 200, 125000)
}

def get_rank_bullets(rank_number):
    for rank_name, (min_rank, max_rank, bullets) in RANKS.items():
        if min_rank <= rank_number <= max_rank:
            return rank_name, bullets
    return None, 0


def organize_varg_search(input_text):
    lines = input_text.strip().split('\n')
    organized_lines = []

    for line in lines:
        parts = line.split()
        if len(parts) < 3:
            continue
        varg_name = parts[0]
        varg_city = parts[1]
        try:
            varg_rank = int(parts[2])
        except ValueError:
            continue
        varg_value = parts[3] if len(parts) > 3 else ''
        varg_money = parts[4] if len(parts) > 4 else ''

        rank_name, bullets = get_rank_bullets(varg_rank)
        organized_line = f'{varg_city} {varg_name} {varg_rank} {varg_value} {varg_money} ({rank_name}) {bullets} bullets'
        organized_lines.append(organized_line)

    return '\n'.join(organized_lines)


def convert_bullets(input_text):
    lines = input_text.strip().split('\n')
    converted_lines = []

    for line in lines:
        parts = line.split()
        if len(parts) < 3:
            continue
        varg_name = parts[1]
        try:
            varg_rank = int(parts[2])
        except ValueError:
            continue

        rank_name, bullets = get_rank_bullets(varg_rank)
        converted_line = f'{line} {bullets} bullets'
        converted_lines.append(converted_line)

    return '\n'.join(converted_lines)


st.title("VARG Table App")

st.subheader("Organize VARG Search")
search_input = st.text_area("Paste search result:")
if st.button("Organize Search"):
    organized_output = organize_varg_search(search_input)
    st.text_area("Organized Table:", value=organized_output, height=300)

st.subheader("Convert Table to Include Bullets")
bullet_input = st.text_area("Paste organized table:")
if st.button("Convert Table"):
    bullet_output = convert_bullets(bullet_input)
    st.text_area("Converted Table:", value=bullet_output, height=300)
