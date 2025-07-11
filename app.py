import streamlit as st
from model import analyze_symptoms
from helpers.healthcare_data import get_nearby_clinics

st.set_page_config(page_title="AI Health Assistant (SDG 3)", layout="wide")

with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🤖 AI Health Assistant")
st.markdown("Supporting **SDG 3: Good Health and Well-being**")

user_input = st.text_area("Enter your symptoms in your own words:")

if st.button("Analyze Symptoms"):
    if user_input:
        with st.spinner("Analyzing your symptoms..."):
            diagnosis, meds = analyze_symptoms(user_input)
            st.subheader("🩺 Preliminary Condition")
            st.write(diagnosis)

            if meds:
                st.subheader("💊 Suggested OTC Medication")
                st.write(", ".join(meds))

            st.subheader("🏥 Nearby Healthcare Facilities in Kenya")
            clinics = get_nearby_clinics()
            for clinic in clinics:
                st.markdown(f"- **{clinic['name']}** – {clinic['location']}")
    else:
        st.warning("Please enter your symptoms.")
