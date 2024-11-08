import streamlit as st
import pandas as pd
from streamlit.components.v1 import html
import plotly.express as px

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

def calulator():
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["**Personal**","**Travel**","**Waste**","**Energy**","**Others**","**Result**"])

    def click_element(element):
        open_script = f"<script type = 'text/javascript'>window.parent.document.querySelector('[id^=tabs-bui][id$=-{element}]').click();</script>"
        html(open_script, width=0, height=0)

    with tab1.form("form1"):
        st.subheader("Personal Details")
        height = st.number_input("Height",0,251,placeholder="160", help="in cm")
        weight = st.number_input("Weight", 0, 250,placeholder="75", help="in kg")
        gender = st.selectbox('Gender', ["Female", "Male"])
        diet = st.selectbox('Diet', ['omnivore', 'pescatarian', 'vegetarian', 'vegan'], help="""
                                                                                                Omnivore: Eats both plants and animals.\n
                                                                                                Pescatarian: Consumes plants and seafood, but no other meat\n
                                                                                                Vegetarian: Diet excludes meat but includes plant-based foods.\n
                                                                                                Vegan: Avoids all animal products, including meat, dairy, and eggs.""")
        age = st.slider('How old are you?', 0, 100, 2)

        # calculation
        BMIin = 10*weight+6.25*height-5*age
        if gender == "Male":
            BMI = BMIin+5
        if gender == "Female":
            BMI = BMIin-161
        Daily_caloric_need = BMI*1.375
        if diet == "omnivore":
            tcfp = 2.5/1000
        if diet == "pescatarian":
            tcfp = 1.8/1000
        if diet == "vegetarian":
            tcfp = 1.7/1000
        if diet == "vegan":
            tcfp = 0.1/1000
        tpcf = Daily_caloric_need*tcfp

        
        total_Personal_cfc = tpcf*365
        if st.form_submit_button("Next", type="primary"):
            click_element('tab-1')
        





















    with tab2.form("form2--1"):
        st.subheader("Transportation")
        transport = st.selectbox('Transportation medium', ['public', 'private', 'walk/bicycle'],
                                help="Which transportation method do you prefer the most?")
        st.form_submit_button()
    with tab2.form("form2--2"):
        if transport == "walk/bicycle":
            Distance = 0
        
        else:
            Distance = st.slider('What is the monthly distance traveled by the vehicle per day ?', 0, 250, 40, disabled=False)
        
        if transport == "private":
            
            private_tsp = st.selectbox('Vehicle Type', ['Car (Petrol)', 'Car (Diesel)','Car (CNG)','Car (Electric)', 'Bike/scooter (Petrol)','Bike/scooter (Electric)'],
                                        help="What type of fuel do you use in your car?")
            Trans_main_fac = Distance*2.31
    
            if private_tsp == "Car (Petrol)":
                Trans_main_fac_emi = Trans_main_fac*0.15
            if private_tsp == "Car (Diesel)":
                Trans_main_fac_emi = Trans_main_fac*0.12
            if private_tsp == "Car (CNG)":
                Trans_main_fac_emi = Trans_main_fac*0.08
            if private_tsp == "Car (Electric)":
                Trans_main_fac_emi = Trans_main_fac*0.025
            if private_tsp == "Bike/scooter (Petrol)":
                Trans_main_fac_emi = Trans_main_fac*0.05
            if private_tsp == "Bike/scooter (Electric)":
                Trans_main_fac_emi = Trans_main_fac*0.0017

        elif transport == "public":
            public_tsp = st.selectbox('Vehicle Type', ['Bus', 'Auto', 'Train', 'Taxi',],
                                        help="What type of fuel do you use in your car?")
            Trans_main_fac = Distance*2.31
    
            if public_tsp == "Bus":
                Trans_main_fac_emi = Trans_main_fac*4
            if public_tsp == "Auto":
                Trans_main_fac_emi = Trans_main_fac*3
            if public_tsp == "Train":
                Trans_main_fac_emi = Trans_main_fac*5
            if public_tsp == "Taxi":
                Trans_main_fac_emi = Trans_main_fac*0.12
            
        else:
            private_tsp,public_tsp = "None"


        
        Trans_main_fac_emi_month=Trans_main_fac_emi*30
        
        st.form_submit_button("Submit")
    with tab2.form("form2--3"):
        air_travel = st.selectbox('How often did you fly last month?', ['never', 'rarely', 'frequently', 'very frequently'], help= """
                                                                                                                                Never: I didn't travel by plane.\n
                                                                                                                                Rarely: Around 1-4 Hours.\n
                                                                                                                                Frequently: Around 5 - 10 Hours.\n
                                                                                                                                Very Frequently: Around 10+ Hours. """)
        if air_travel == "never":
            Flight_emi = 0
        if air_travel == "rarely":
            Flight_emi = 2000*3.15*3
        if air_travel == "frequently":
            Flight_emi = 2000*3.15*8
        if air_travel == "very frequently":
            Flight_emi = 2000*3.15*15
        
        Total_Trans = Trans_main_fac_emi_month+Flight_emi
        if st.form_submit_button("Next", type="primary"):
            click_element('tab-2')






















    with tab3.form("form3"):
        st.subheader("Waste emission")
        
        mass_of_waste = st.number_input('What is the Quantity of Daily production of waste from your home?', 0,10,help= """
                                                                                                                                This quantity you have to fill in Kilogram(kg).\n
                                                                                                                                """)
        no_of_waste_bags_pw = st.slider('How many Genral waste bags do you trash out in a week?', 0, 10, 5)

        Total_waste = mass_of_waste*0.3*no_of_waste_bags_pw*4
        recycle = st.multiselect('Do you recycle any materials below?', ['Plastic', 'Paper', 'Metal', 'Glass'])


        if st.form_submit_button("Next", type="primary"):
            click_element('tab-3')























    with tab4.form("form4"):
        st.subheader("Energy Consumption")
        heating_energy = st.multiselect('What power source do you use for heating?', ['Natural gas', 'Electricity', 'Wood', 'Coal'],default="Electricity")
        electricity = st.number_input("Energy consumption of your Home ?",help="This quantity you have to fill in kWh")
        energy_efficiency = st.selectbox('Do you Include the energy consumption of PC/TV or internet in Total Energy Consumption?', ['No', 'Yes' ],help="if you say yes so that your TV/PC or Internet's energy consumption will not be added with your total energy cunsumption.Otherwise if you say no then the PC/TV's energy consumption will be added with home energy cunsumption and then the sum will be considered for calculation")
        daily_tv_pc = st.slider('How many hours a day do you spend in front of your PC/TV?', 0, 24, 2)
        internet_daily = st.slider('What is your daily internet usage in hours?', 0, 24, 2)
        if st.form_submit_button("Next", type="primary"):
            click_element('tab-4')
        























    with tab5.form("form5"):
        st.subheader("Other Consumptions")
        
        shower = st.multiselect('Which Electronic Applineces do you use that uses CFC?', ['Refrigerator', 'AC'],default="Refrigerator")
        grocery_bill = st.slider('How Many Hours do you emit CFC', 0, 24, 6)
        clothes_monthly = st.slider('How many clothes do you buy monthly?', 0, 30, 0)
        
       
        def result():
            # st.write("Personal",
            #     total_Personal_cfc,
            # )
            # st.write("Transportation",
            #     Total_Trans,
            # )
            total= total_Personal_cfc+Total_Trans+Total_waste
            df = pd.DataFrame({
                'Category':["Personal","Transportation","Waste"],
                'Carbon emission':[total_Personal_cfc,Total_Trans,Total_waste]
            })
            totalt = pd.DataFrame({
                'Total':["Total"],
                'Carbon emission value':[total]
            })

            col1,col2 = st.columns([1,1])

            with col2:
                st.write('DataFrame:')
                st.write(df)
                st.write(totalt)
                
            with col1:
                st.write("pie chart:")
                fig = px.pie(df,values='Carbon emission',names='Category')
                st.plotly_chart(fig,use_container_width=100)

        if st.form_submit_button("Done ", type="primary"):
            click_element('tab-5')

    with tab6.form("res"):
        result()

        if st.form_submit_button("Home", type="primary"):
            click_element('tab-0')

calulator()
 