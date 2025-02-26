import streamlit as st
from forex_python.converter import CurrencyRates
import requests

def convert_units(category, input_value, from_unit, to_unit):
    conversion_factors = {
        "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Inch": 39.37, "Foot": 3.281},
        "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.205, "Ounce": 35.274},
        "Temperature": "Temperature",  # Special case
        "Currency": "Currency"  # Special case
    }
    
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (input_value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (input_value - 32) * 5/9
        else:
            return input_value
    elif category == "Currency":
        try:
            c = CurrencyRates()
            rate = c.get_rate(from_unit, to_unit)
            if rate is None:
                return "Error: Could not fetch exchange rate."
            return input_value * rate
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"
    else:
        return input_value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])

# Streamlit App UI
st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("⚖️ 🌡️Multi-Unit Converter💱📌")
st.sidebar.header("Choose Conversion Type")

categories = ["Length", "Weight", "Temperature", "Currency"]
selected_category = st.sidebar.selectbox("Select Category", categories)

unit_options = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Inch", "Foot"],
    "Weight": ["Kilogram", "Gram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit"],
    "Currency": ["USD", "EUR", "GBP", "PKR"]  # Add more as needed
}

from_unit = st.selectbox("From Unit", unit_options[selected_category])
to_unit = st.selectbox("To Unit", unit_options[selected_category])
input_value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

if st.button("Convert 🌟"):
    result = convert_units(selected_category, input_value, from_unit, to_unit)
    st.success(f"Converted Value: {result}")

st.markdown("---")
st.markdown("💡 **Tip:** Use sidebar to switch between different unit conversions.")
st.markdown("""
    <style>
        /* Dropdown (Selectbox) */
        div[data-testid="stSelectbox"] label {cursor: pointer !important;}
        div[data-testid="stSelectbox"] select {cursor: pointer !important;}

        /* Buttons */
        div.stButton button {cursor: pointer !important;}

        /* Number Input */
        div[data-testid="stNumberInput"] input {cursor: text !important;}
    </style>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr>
    <p style="text-align:center;">© 2025 Madiha Ali Khan | All Rights Reserved</p>
""", unsafe_allow_html=True)

#    import streamlit as st
# from forex_python.converter import CurrencyRates
# import requests

# def convert_units(category, input_value, from_unit, to_unit):
#     conversion_factors = {
#         "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Inch": 39.37, "Foot": 3.281},
#         "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.205, "Ounce": 35.274},
#         "Temperature": "Temperature",  # Special case
#         "Currency": "Currency"  # Special case
#     }
    
#     if category == "Temperature":
#         if from_unit == "Celsius" and to_unit == "Fahrenheit":
#             return (input_value * 9/5) + 32
#         elif from_unit == "Fahrenheit" and to_unit == "Celsius":
#             return (input_value - 32) * 5/9
#         else:
#             return input_value
#     elif category == "Currency":
#         try:
#             c = CurrencyRates()
#             rate = c.get_rate(from_unit, to_unit)
#             if rate is None:
#                 return "Error: Could not fetch exchange rate."
#             return input_value * rate
#         except requests.exceptions.RequestException as e:
#             return f"Error: {str(e)}"
#     else:
#         return input_value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])

# # Streamlit App UI
# st.set_page_config(page_title="Unit Converter", layout="centered")
# st.markdown("""
#     <h1 style="text-align:center;">⚡ Multi-Unit Converter 🔄</h1>
# """, unsafe_allow_html=True)

# st.sidebar.header("📏 Choose Conversion Type 📌")

# categories = {
#     "📏 Length": "Length",
#     "⚖️ Weight": "Weight",
#     "🌡️ Temperature": "Temperature",
#     "💱 Currency": "Currency"
# }
# selected_category = st.sidebar.selectbox("Select Category", list(categories.keys()))
# selected_category = categories[selected_category]  # Get actual category name

# unit_options = {
#     "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Inch", "Foot"],
#     "Weight": ["Kilogram", "Gram", "Pound", "Ounce"],
#     "Temperature": ["Celsius", "Fahrenheit"],
#     "Currency": ["USD", "EUR", "GBP", "PKR"]  # Add more as needed
# }

# from_unit = st.selectbox("From Unit", unit_options[selected_category])
# to_unit = st.selectbox("To Unit", unit_options[selected_category])
# input_value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

# if st.button("Convert"):
#     result = convert_units(selected_category, input_value, from_unit, to_unit)
#     st.success(f"Converted Value: {result}")

# st.markdown("---")
# st.markdown("💡 **Tip:** Use sidebar to switch between different unit conversions.")
