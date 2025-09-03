import streamlit as st

# Streamlit app
st.title("Power Calculator")
st.write("Enter a number to calculate the square, cube and fourth power")
number = st.number_input("Number", value=1, step=1)

square = number ** 2
cube = number ** 3
fourth = number ** 4

st.write(f"The Square of the {number} is:", square)
st.write(f"The Cube of the {number} is:", cube)
st.write(f"The Fourth Power of the {number} is:", fourth)