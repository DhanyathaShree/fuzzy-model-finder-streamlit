import streamlit as st
from fuzzywuzzy import process, fuzz

# List of database model names
database_names = [
    "ford_aspire", "ford_ecosport", "ford_endeavour", "ford_figo", "honda_amaze", "honda_city", 
    "honda_wr_v", "hyundai_aura", "hyundai_grand_i10", "hyundai_i10", "jeep_compass", 
    "jeep_meridian", "kia_carens", "kia_seltos", "kia_sonet", "land_rover_defender", 
    "mahindra_scorpio", "mahindra_thar", "mahindra_xuv300", "mahindra_xuv400", 
    "mahindra_xuv700", "maruti_celerio", "maruti_suzuki_brezza", "maruti_suzuki_s_presso", 
    "maruti_suzuki_swift", "maruti_suzuki_wagonr", "maruti_suzuki_xl6", "mg_astor", 
    "mg_gloster", "mg_hector", "mg_zs_ev", "renault_kiger", "renault_triber", 
    "skoda_kushaq", "skoda_slavia", "tata_harrier", "tata_punch", "tata_tiago", 
    "toyota_camry", "toyota_fortuner", "toyota_fortuner_legender", "toyota_glanza", 
    "toyota_innova_crysta"
]

def normalize_string(s):
    return ''.join(e for e in s.lower() if e.isalnum() or e.isspace()).strip()

def match_vehicle_model(user_input, database_names):
    normalized_user_input = normalize_string(user_input)
    normalized_db_names = [normalize_string(name) for name in database_names]
    # Find the best match
    best_match, score = process.extractOne(normalized_user_input, normalized_db_names, scorer=fuzz.token_set_ratio)
    
    # Retrieve the original database name corresponding to the best match
    best_match_original = database_names[normalized_db_names.index(best_match)]
    return best_match_original, score


st.title("Vehicle Model Matcher")
st.markdown("---")
user_input = st.text_input("Enter your vehicle model:", "")

if st.button("Submit"):
    if user_input:
        best_match, score = match_vehicle_model(user_input, database_names)
        st.markdown(f"### Best Matched Database Name: **{best_match}**")
        st.write(f"**Matching Score:** {score}")
    else:
        st.error("Please enter a vehicle model.")
