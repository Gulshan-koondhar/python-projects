import streamlit as st

def main():
    st.title("Unit Converter")
    st.write("Convert between different units of measurement")
    
    # Select conversion category
    category = st.selectbox(
        "Select Category",
        ["Length", "Weight/Mass", "Temperature", "Speed", "Time"]
    )
    
    # Based on the category, show relevant conversion options
    if category == "Length":
        length_converter()
    elif category == "Weight/Mass":
        weight_converter()
    elif category == "Temperature":
        temperature_converter()
    elif category == "Speed":
        speed_converter()
    elif category == "Time":
        time_converter()

def length_converter():
    st.subheader("Length Converter")
    
    # Define conversion factors to meters
    length_units = {
        "Meter (m)": 1.0,
        "Kilometer (km)": 1000.0,
        "Centimeter (cm)": 0.01,
        "Millimeter (mm)": 0.001,
        "Mile (mi)": 1609.34,
        "Yard (yd)": 0.9144,
        "Foot (ft)": 0.3048,
        "Inch (in)": 0.0254
    }
    
    # Input value
    input_value = st.number_input("Enter value", value=1.0, step=0.1)
    
    # From and To units in a single row
    col1, col2 = st.columns(2)
    with col1:
        input_unit = st.selectbox("From", list(length_units.keys()), key="length_from")
    with col2:
        output_unit = st.selectbox("To", list(length_units.keys()), key="length_to")
    
    # Convert to meters, then to target unit
    result = input_value * length_units[input_unit] / length_units[output_unit]
    
    # Display result centered
    st.markdown(f"<h3 style='text-align: center;'>{input_value} {input_unit} = {result:.6f} {output_unit}</h3>", unsafe_allow_html=True)

def weight_converter():
    st.subheader("Weight/Mass Converter")
    
    # Define conversion factors to kilograms
    weight_units = {
        "Kilogram (kg)": 1.0,
        "Gram (g)": 0.001,
        "Milligram (mg)": 0.000001,
        "Metric Ton (t)": 1000.0,
        "Pound (lb)": 0.453592,
    }
    
    # Input value
    input_value = st.number_input("Enter value", value=1.0, step=0.1, key="weight_input")
    
    # From and To units in a single row
    col1, col2 = st.columns(2)
    with col1:
        input_unit = st.selectbox("From", list(weight_units.keys()), key="weight_from")
    with col2:
        output_unit = st.selectbox("To", list(weight_units.keys()), key="weight_to")
    
    # Convert to kg, then to target unit
    result = input_value * weight_units[input_unit] / weight_units[output_unit]
    
    # Display result centered
    st.markdown(f"<h3 style='text-align: center;'>{input_value} {input_unit} = {result:.6f} {output_unit}</h3>", unsafe_allow_html=True)

def temperature_converter():
    st.subheader("Temperature Converter")
    
    temp_units = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]
    
    # Input value
    input_value = st.number_input("Enter value", value=0.0, step=0.1, key="temp_input")
    
    # From and To units in a single row
    col1, col2 = st.columns(2)
    with col1:
        input_unit = st.selectbox("From", temp_units, key="temp_from")
    with col2:
        output_unit = st.selectbox("To", temp_units, key="temp_to")
    
    # Convert to Celsius first
    if input_unit == "Celsius (°C)":
        celsius = input_value
    elif input_unit == "Fahrenheit (°F)":
        celsius = (input_value - 32) * 5/9
    else:  # Kelvin
        celsius = input_value - 273.15
    
    # Convert from Celsius to target unit
    if output_unit == "Celsius (°C)":
        result = celsius
    elif output_unit == "Fahrenheit (°F)":
        result = celsius * 9/5 + 32
    else:  # Kelvin
        result = celsius + 273.15
    
    # Display result centered
    st.markdown(f"<h3 style='text-align: center;'>{input_value} {input_unit} = {result:.2f} {output_unit}</h3>", unsafe_allow_html=True)


def speed_converter():
    st.subheader("Speed Converter")
    
    # Define conversion factors to meters per second
    speed_units = {
        "Meter per second (m/s)": 1.0,
        "Kilometer per hour (km/h)": 0.277778,
        "Mile per hour (mph)": 0.44704,
    }
    
    # Input value
    input_value = st.number_input("Enter value", value=1.0, step=0.1, key="speed_input")
    
    # From and To units in a single row
    col1, col2 = st.columns(2)
    with col1:
        input_unit = st.selectbox("From", list(speed_units.keys()), key="speed_from")
    with col2:
        output_unit = st.selectbox("To", list(speed_units.keys()), key="speed_to")
    
    # Convert to m/s, then to target unit
    result = input_value * speed_units[input_unit] / speed_units[output_unit]
    
    # Display result centered
    st.markdown(f"<h3 style='text-align: center;'>{input_value} {input_unit} = {result:.6f} {output_unit}</h3>", unsafe_allow_html=True)

def time_converter():
    st.subheader("Time Converter")
    
    # Define conversion factors to seconds
    time_units = {
        "Second (s)": 1.0,
        "Millisecond (ms)": 0.001,
        "Microsecond (μs)": 0.000001,
        "Nanosecond (ns)": 1e-9,
        "Minute (min)": 60.0,
        "Hour (h)": 3600.0,
        "Day (d)": 86400.0,
        "Week (wk)": 604800.0,
        "Month (avg)": 2629800.0,  # Average month (30.44 days)
        "Year (avg)": 31557600.0   # Average year (365.25 days)
    }
    
    # Input value
    input_value = st.number_input("Enter value", value=1.0, step=0.1, key="time_input")
    
    # From and To units in a single row
    col1, col2 = st.columns(2)
    with col1:
        input_unit = st.selectbox("From", list(time_units.keys()), key="time_from")
    with col2:
        output_unit = st.selectbox("To", list(time_units.keys()), key="time_to")
    
    # Convert to seconds, then to target unit
    result = input_value * time_units[input_unit] / time_units[output_unit]
    
    # Display result centered
    st.markdown(f"<h3 style='text-align: center;'>{input_value} {input_unit} = {result:.6f} {output_unit}</h3>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
