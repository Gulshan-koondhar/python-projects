import streamlit as st

CONVERTERS = {
    "Length": {
        "Meter (m)": 1,
        "Kilometer (km)": 1000, 
        "Centimeter (cm)": 0.01,
        "Millimeter (mm)": 0.001, 
        "Mile (mi)": 1609.34,
        "Yard (yd)": 0.9144,
        "Foot (ft)": 0.3048, 
        "Inch (in)": 0.0254
    },
    "Weight/Mass": {
        "Kilogram (kg)": 1, "Gram (g)": 0.001, "Milligram (mg)": 1e-6,
        "Metric Ton (t)": 1000, "Pound (lb)": 0.453592, "Ounce (oz)": 0.0283495
    },
    "Temperature": {
        "Celsius (°C)": lambda c: c,
        "Fahrenheit (°F)": lambda c: c * 9/5 + 32,
        "Kelvin (K)": lambda c: c + 273.15
    },

    "Speed": {
        "Meter per second (m/s)": 1, "Kilometer per hour (km/h)": 0.277778,
        "Mile per hour (mph)": 0.44704, "Foot per second (ft/s)": 0.3048,
        "Knot (kn)": 0.514444
    },
    "Time": {
        "Second (s)": 1, "Minute (min)": 60, "Hour (h)": 3600,
        "Day (d)": 86400, "Week (wk)": 604800, "Month (avg)": 2629800,
        "Year (avg)": 31557600
    }
}

def convert(category, value, from_unit, to_unit):
    if category == "Temperature":
        celsius = CONVERTERS[category][from_unit](value)
        return CONVERTERS[category][to_unit](celsius)
    else:
        return value * CONVERTERS[category][from_unit] / CONVERTERS[category][to_unit]

st.title("Unit Converter")

category = st.selectbox("Select Category", list(CONVERTERS.keys()))
units = list(CONVERTERS[category].keys())

value = st.number_input("Enter value")
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", units, key="from")
with col2:
    to_unit = st.selectbox("To", units, key="to")

result = convert(category, value, from_unit, to_unit)

st.markdown(f"<h3 style='text-align: center;'>{value} {from_unit} = {result:.6f} {to_unit}</h3>", unsafe_allow_html=True)