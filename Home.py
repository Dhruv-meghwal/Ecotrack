import streamlit as st
st.set_page_config(
    page_title="Ecotrack",
    layout="wide",
    page_icon="images/favicon.ico",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help':'https://dbdmg.polito.it/',
        'Report a bug':"https://dbdmg.polito.it/",
        'About':"EcoTrack ",
    }
)

st.title("Eco:green[Track]")
st.text("The carbon footprint calculator")
st.subheader("About Carbon Footprint")
st.write("  - The carbon footprint refers to the total amount of greenhouse gases (GHGs) emitted into the atmosphere due to human activities, primarily in the form of carbon dioxide (CO₂) and methane (CH₄).")
st.write("  - Measured in **tons of CO₂ equivalent** (CO₂e).")
st.write("  - Includes both direct and indirect emissions.")
st.subheader("Why it Matters?")
st.write("  - Climate change is driven by increased greenhouse gas emissions.")
st.write("  - Every activity from transportation to food production contributes to the carbon footprint.")
st.write("  - Understanding it helps identify areas to reduce emissions and combat global warming.")
st.subheader("Sources:")
st.write("  1. **Energy Production** (Burning of fossil fuels for electricity, heating, and industry)")
st.write("  2. **Transportation** (Cars, airplanes, ships, etc.)")
st.write("  3. **Agriculture** (Livestock, rice cultivation, deforestation, etc.)")
st.write("  4. **Industry** (Manufacturing processes, chemical production, cement, steel, etc.)")
st.write("  5. **Waste** (Landfills, waste incineration)")
st.subheader("Conclution")
st.write("The global annual carbon footprint has now surpassed an alarming 40 billion tons, underscoring the urgent need for collective action to mitigate climate change. There exists a direct and undeniable correlation between the daily habits of individuals and the surge in CO2 emissions. Everyday practices, ranging from energy consumption and transportation to residential heating-cooling systems and food production-consumption, significantly contribute to this escalating environmental challenge. Recognizing the pivotal role individuals play in this scenario, it becomes imperative to foster awareness regarding their impact on the global increase in CO2 levels. The core objective of the project is to empower individuals by helping them calculate their monthly carbon footprint. By incorporating considerations of daily, weekly, and monthly habits and lifestyle choices, the initiative aims to offer personalized insights. Furthermore, the project is geared towards not only raising awareness but also providing practical recommendations for individuals to actively reduce their carbon footprints. Through these efforts, the goal is to encourage sustainable living practices that contribute to a more environmentally conscious and responsible global community.")
foot = st.container(height=85)
foot.write("© 2024 Eco:green[Track]--carbon-Footprint-Calculator. All rights are Reserved")




