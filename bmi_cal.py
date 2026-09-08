import streamlit as st

#Title of the App
st.header("BMI Calculator")

#Insert and Image
from PIL import Image
st.image(Image.open("BMI.webp"))

#Input: weight in kilograms
weight = st.number_input("Enter Your Weight(Kg):", min_value = 0.0, format = "%.2f")

#Input: Height format selection
height_unit = st.radio("Select Your Height Unit:", ['Centimeters', 'Meters', 'Feet'])

# Input: Height value based on selected unit
height = st.number_input(f"Enter your height ({height_unit.lower()}):", min_value = 0.0, format = "%.2f")

#Calculate BMI when Button is pressed

if st.button("Calculate BMI"):
    try:
        # convert height to meters based on selected unit
        if height_unit == "Centimeters":
            height_m = height / 100
        elif height_unit == "Feet":
            height_m = height / 3.28
        else:
            height_m = height

        # Prevent division by zero error
        if height_m <=0:
            st.error("Height must be greater that zero.")
        else:
            bmi = weight / (height_m ** 2)
            st.success(f"Your BMI is {bmi}")

            #BMI Interpretation
            if bmi < 16:
                st.error("You are Extremely Underweight")
            elif 16 <= bmi < 18.5:
                st.warning("You are Underweight")
            elif 18.5 <= bmi < 25:
                st.success("You are Healthy")
            elif 25 <= bmi < 30:
                st.warning("You are Overweight")
            else:
                st.error("You are Extremely Overweight")

    except:
        st.error("Please enter a valid numeric values.")