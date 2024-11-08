import streamlit as st
import pandas as pd
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Ecotrack",
    layout="wide",
    page_icon="images/favicon.ico",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help':'https://cfc-help.web.app/',
        'Report a bug':"https://cfc-help.web.app/",
        'About':"EcoTrack ",
    }
)
st.title("Source :blue[Code]")
st.code("1. Home.py")
exp = st.expander("Source Code")
exp.code("""
            import streamlit as st
        st.set_page_config(
            page_title="Ecotrack",
            layout="wide",
            page_icon="images/favicon.ico",
            initial_sidebar_state="auto",
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
        st.video("video/CA.mp4",autoplay=True,muted=True,loop=True)
        st.subheader("Conclution")
        st.write("The global annual carbon footprint has now surpassed an alarming 40 billion tons, underscoring the urgent need for collective action to mitigate climate change. There exists a direct and undeniable correlation between the daily habits of individuals and the surge in CO2 emissions. Everyday practices, ranging from energy consumption and transportation to residential heating-cooling systems and food production-consumption, significantly contribute to this escalating environmental challenge. Recognizing the pivotal role individuals play in this scenario, it becomes imperative to foster awareness regarding their impact on the global increase in CO2 levels. The core objective of the project is to empower individuals by helping them calculate their monthly carbon footprint. By incorporating considerations of daily, weekly, and monthly habits and lifestyle choices, the initiative aims to offer personalized insights. Furthermore, the project is geared towards not only raising awareness but also providing practical recommendations for individuals to actively reduce their carbon footprints. Through these efforts, the goal is to encourage sustainable living practices that contribute to a more environmentally conscious and responsible global community.")
        foot = st.container(height=85)
        foot.write("© 2024 Eco:green[Track]--carbon-Footprint-Calculator. All rights are Reserved")





""")




st.code("2. /Pages/Calculate.py")
exp = st.expander("Source Code")
exp.code("""
           import streamlit as st
import pandas as pd
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Ecotrack",
    layout="wide",
    page_icon="images/favicon.ico",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help':'https://cfc-help.web.app/',
        'Report a bug':"https://cfc-help.web.app/",
        'About':"EcoTrack ",
    }
)
st.title("Carbon :green[Footprint]")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["**Personal**","**Travel**","**Waste**","**Energy**","**Others**"])

def click_element(element):
    open_script = f"<script type = 'text/javascript'>window.parent.document.querySelector('[id^=tabs-bui][id$=-{element}]').click();</script>"
    html(open_script, width=0, height=0)

with tab1.form("form1"):
    st.subheader("Personal Details")
    height = st.number_input("Height",0,251,placeholder="160", help="in cm")
    weight = st.number_input("Weight", 0, 250,placeholder="75", help="in kg")
    gender = st.selectbox('Gender', ["Female", "Male"])
    diet = st.selectbox('Diet', ['omnivore', 'pescatarian', 'vegetarian', 'vegan'], help=" Omnivore: Eats both plants and animals.\n Pescatarian: Consumes plants and seafood, but no other meat\n Vegetarian: Diet excludes meat but includes plant-based foods.\n Vegan: Avoids all animal products, including meat, dairy, and eggs.")
    age = st.slider('How old are you?', 0, 100, 2)

    # calculation
    BMIin = 10*weight+6.25*height-5*age
    if gender == "Male":
        BMI = BMIin+5
    if gender == "Female":
        BMI = BMIin-161
    Daily_caloric_need = BMI*1.375
    monthly_caloric_need = Daily_caloric_need*30
    if diet == "omnivore":
        tcfp = 60*6
    if diet == "pescatarian":
        tcfp = 60*4.5
    if diet == "vegetarian":
        tcfp = 60*2
    if diet == "vegan":
        tcfp = 60*3
    tpcf = tcfp+monthly_caloric_need


    
    total_Personal_cfc = tpcf


    st.form_submit_button("Submit")
    but = tab1
    if but.button("Go to Travel", type="primary"):
        click_element('tab-1')

with tab2.form("form2--1"):
    st.subheader("Transportation")
    transport = st.selectbox('Transportation medium', ['public', 'private', 'walk/bicycle'],
                               help="Which transportation method do you prefer the most?")
    st.form_submit_button()
with tab2.form("form2--2"):
    if transport == "private":
        private_tsp = st.selectbox('Vehicle Type', ['Car (Petrol)', 'Car (Diesel)','Car (CNG)','Car (Electric)', 'Bike/scooter (Petrol)','Bike/scooter (Electric)'],
                                      help="What type of fuel do you use in your car?")
    elif transport == "public":
        public_tsp = st.selectbox('Vehicle Type', ['Bus', 'Auto', 'Train', 'Taxi',],
                                      help="What type of fuel do you use in your car?")
    else:
        private_tsp,public_tsp = "None"

    if transport == "walk/bicycle":
        Distance = 0
    else:
        Distance = st.slider('What is the monthly distance traveled by the vehicle per day ?', 0, 250, 40, disabled=False)
    # calculation
    Trans_main_fac = Distance*2.31
    if private_tsp == "Car (Petrol)":
        Trans_main_fac_emi = Trans_main_fac*8/100
    if private_tsp == "Car (Diesel)":
        Trans_main_fac_emi = Trans_main_fac*6/100
    if private_tsp == "Car (CNG)":
        Trans_main_fac_emi = Trans_main_fac*6/100
    if private_tsp == "Car (Electric)":
        Trans_main_fac_emi = Trans_main_fac*1.35/100
    if private_tsp == "Bike/scooter (Petrol)":
        Trans_main_fac_emi = Trans_main_fac*8/100
    if private_tsp == "Bike/scooter (Electric)":
        Trans_main_fac_emi = Trans_main_fac*6/100
    
    Trans_main_fac_emi_month=Trans_main_fac_emi*30
    
    
    st.form_submit_button("Submit")
with tab2.form("form2--3"):
    air_travel = st.selectbox('How often did you fly last month?', ['never', 'rarely', 'frequently', 'very frequently'], help= "Never: I didn't travel by plane.\n Rarely: Around 1-4 Hours.\n Frequently: Around 5 - 10 Hours.\n Very Frequently: Around 10+ Hours. ")

    submitted = st.form_submit_button("Submit")
    but= tab2
    if but.button("Go to Waste", type="primary"):
        click_element('tab-2')

with tab3.form("form3"):
    st.subheader("Waste emission")
    
    gen_waste_bag = st.number_input('What is the Quantity of Daily production of waste from your home?', 0,10,help= "This quantity you have to fill in Kilogram(kg).\n
                                                                                                                             ")
    gen_waste_count = st.slider('How many Genral waste bags do you trash out in a week?', 0, 10, 5)
    
    recycle = st.multiselect('Do you recycle any materials below?', ['Plastic', 'Paper', 'Metal', 'Glass'])


    st.form_submit_button("Submit")
    but = tab3
    if but.button("Go to Energy", type="primary"):
        click_element('tab-3')

with tab4.form("form4"):
    st.subheader("Energy Consumption")
    heating_energy = st.multiselect('What power source do you use for heating?', ['Natural gas', 'Electricity', 'Wood', 'Coal'],default="Electricity")
    electricity = st.number_input("Energy consumption of your Home ?",help="This quantity you have to fill in kWh")
    energy_efficiency = st.selectbox('Do you Include the energy consumption of PC/TV or internet in Total Energy Consumption?', ['No', 'Yes' ],help="if you say yes so that your TV/PC or Internet's energy consumption will not be added with your total energy cunsumption.Otherwise if you say no then the PC/TV's energy consumption will be added with home energy cunsumption and then the sum will be considered for calculation")
    daily_tv_pc = st.slider('How many hours a day do you spend in front of your PC/TV?', 0, 24, 2)
    internet_daily = st.slider('What is your daily internet usage in hours?', 0, 24, 2)
    submitted = st.form_submit_button("Submit")

    but = tab4
    if but.button("Go to Consumption", type="primary"):
        click_element('tab-4')
    
with tab5.form("form5"):
    st.subheader("Other Consumptions")
    
    shower = st.multiselect('Which Electronic Applineces do you use that uses CFC?', ['Refrigerator', 'AC'],default="Refrigerator")
    grocery_bill = st.slider('How Many Hours do you emit CFC', 0, 24, 6)
    clothes_monthly = st.slider('How many clothes do you buy monthly?', 0, 30, 0)
    st.write(Trans_main_fac_emi_month)
    st.form_submit_button("Submit")

_,res,_ = tab5.columns([1,2,1])
if res.button("Get Your Carbon Footprint", type="primary"):
    click_element("tab-6")

""")









st.code("2. /Pages/Calculate.py")
exp = st.expander("Source Code")
exp.code("""

""")