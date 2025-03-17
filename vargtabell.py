import streamlit as st

# Bullet calculation based on rank
RANKS = [
    (1, 58, 'Wannabe', 16000),
    (59, 106, 'Bråkmaker', 25000),
    (107, 144, 'Gangster', 45000),
    (145, 172, 'Hitman', 65000),
    (173, 191, 'Assassin', 90000),
    (192, 200, 'Kaptein', 125000)
]


def calculate_bullets(rank_number):
    for start, end, _, bullets in RANKS:
        if start <= rank_number <= end:
            return bullets
    return 0


def organize_varg_search(search_result):
    lines = search_result.strip().splitlines()
    organized = {}

    for line in lines:
        parts = line.split()
        city = parts[0]
        varg_name = parts[1]
        varg_rank = int(parts[2])
        bullets = calculate_bullets(varg_rank)

        if city not in organized:
            organized[city] = []

        organized[city].append(f"{varg_name} {varg_rank} {bullets}")

    result = []
    for city, vargs in organized.items():
        result.append(f"{city}")
        result.extend(vargs)

    return "\n".join(result)


def add_bullets_to_table(organized_table):
    lines = organized_table.strip().splitlines()
    result = []

    for line in lines:
        parts = line.split()
        if len(parts) == 2 and parts[1].isdigit():
            rank_number = int(parts[1])
            bullets = calculate_bullets(rank_number)
            result.append(f"{line} {bullets}")
        else:
            result.append(line)

    return "\n".join(result)


st.title("VARG Search and Bullet Calculator")

# Input fields
st.header("Organize VARG Search")
search_input = st.text_area("Paste VARG search result here:")

st.header("Convert Organized Table")
table_input = st.text_area("Paste organized table here:")

# Process input
if st.button("Organize Search"):
    if search_input:
        organized_output = organize_varg_search(search_input)
        st.text_area("Organized Table:", organized_output, height=300)
    else:
        st.warning("Please paste a VARG search result.")

if st.button("Convert Table to Include Bullets"):
    if table_input:
        bullet_output = add_bullets_to_table(table_input)
        st.text_area("Table with Bullets:", bullet_output, height=300)
    else:
        st.warning("Please paste an organized table.")
