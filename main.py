import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Multi-Unit Converter",
    page_icon="🔄",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #424242;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stSelectbox label {
        font-size: 1.2rem;
        color: #1E88E5;
        font-weight: bold;
    }
    .category-card {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .value-display {
        font-size: 1.8rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
    }
    .formula-box {
        background-color: #fff9c4;
        padding: 10px;
        border-radius: 5px;
        margin-top: 20px;
        font-style: italic;
    }
    .conversion-details {
        background-color: #e3f2fd;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #616161;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Cache conversion data for performance
@st.cache_data
def load_conversion_data():
    """Load and return the conversion data dictionary."""
    return {
        "Length": {
            "Meter": 1,
            "Kilometer": 1000,
            "Centimeter": 0.01,
            "Millimeter": 0.001,
            "Mile": 1609.34,
            "Yard": 0.9144,
            "Foot": 0.3048,
            "Inch": 0.0254
        },
        "Area": {
            "Square Meter": 1,
            "Square Kilometer": 1000000,
            "Square Centimeter": 0.0001,
            "Square Millimeter": 0.000001,
            "Hectare": 10000,
            "Acre": 4046.86,
            "Square Mile": 2589988.11,
            "Square Yard": 0.836127,
            "Square Foot": 0.092903,
            "Square Inch": 0.00064516
        },
        "Mass": {
            "Kilogram": 1,
            "Gram": 0.001,
            "Milligram": 0.000001,
            "Metric Ton": 1000,
            "Pound": 0.453592,
            "Ounce": 0.0283495,
            "Stone": 6.35029
        },
        "Volume": {
            "Cubic Meter": 1,
            "Cubic Kilometer": 1000000000,
            "Cubic Centimeter": 0.000001,
            "Milliliter": 0.000001,
            "Liter": 0.001,
            "Gallon (US)": 0.00378541,
            "Quart (US)": 0.000946353,
            "Pint (US)": 0.000473176,
            "Cup (US)": 0.000236588,
            "Fluid Ounce (US)": 0.0000295735,
            "Cubic Inch": 0.0000163871
        },
        "Temperature": {
            "Celsius": "C",
            "Fahrenheit": "F",
            "Kelvin": "K"
        },
        "Time": {
            "Second": 1,
            "Millisecond": 0.001,
            "Microsecond": 0.000001,
            "Nanosecond": 1e-9,
            "Minute": 60,
            "Hour": 3600,
            "Day": 86400,
            "Week": 604800,
            "Month (30 days)": 2592000,
            "Year (365 days)": 31536000
        },
        "Speed": {
            "Meter per second": 1,
            "Kilometer per hour": 0.277778,
            "Mile per hour": 0.44704,
            "Knot": 0.514444,
            "Foot per second": 0.3048
        },
        "Data Transfer Rate": {
            "Bit per second": 1,
            "Kilobit per second": 1000,
            "Megabit per second": 1000000,
            "Gigabit per second": 1000000000,
            "Byte per second": 8,
            "Kilobyte per second": 8000,
            "Megabyte per second": 8000000,
            "Gigabyte per second": 8000000000
        },
        "Digital Storage": {
            "Bit": 1,
            "Kilobit": 1000,
            "Megabit": 1000000,
            "Gigabit": 1000000000,
            "Terabit": 1000000000000,
            "Byte": 8,
            "Kilobyte": 8000,
            "Megabyte": 8000000,
            "Gigabyte": 8000000000,
            "Terabyte": 8000000000000
        },
        "Energy": {
            "Joule": 1,
            "Kilojoule": 1000,
            "Calorie": 4.184,
            "Kilocalorie": 4184,
            "Watt-hour": 3600,
            "Kilowatt-hour": 3600000,
            "Electronvolt": 1.602176634e-19,
            "British Thermal Unit": 1055.06
        },
        "Pressure": {
            "Pascal": 1,
            "Kilopascal": 1000,
            "Bar": 100000,
            "Atmosphere": 101325,
            "Millimeter of mercury": 133.322,
            "Pound per square inch": 6894.76
        },
        "Frequency": {
            "Hertz": 1,
            "Kilohertz": 1000,
            "Megahertz": 1000000,
            "Gigahertz": 1000000000
        },
        "Fuel Economy": {
            "Miles per gallon (US)": 1,
            "Miles per gallon (UK)": 1.20095,
            "Kilometer per liter": 0.425144,
            "Liter per 100 kilometers": "SPECIAL"  # Changed to indicate special handling needed
        },
        "Plane Angle": {
            "Degree": 1,
            "Radian": 57.2958,
            "Gradian": 0.9,
            "Arcminute": 1/60,
            "Arcsecond": 1/3600
        }
    }

conversion_data = load_conversion_data()

# Expanded unit descriptions
unit_descriptions = {
    "Length": {
        "Meter": "The meter is the base unit of length in the SI system, defined as the distance light travels in a vacuum in 1/299,792,458 seconds. Used globally for scientific and everyday measurements.",
        "Kilometer": "Equal to 1000 meters, kilometers are ideal for long distances like roads or geographical spans. A typical car trip might be measured in kilometers.",
        "Centimeter": "One-hundredth of a meter (0.01 m), commonly used for small objects like furniture dimensions or human height in metric countries.",
        "Millimeter": "One-thousandth of a meter (0.001 m), perfect for precision tasks like engineering tolerances or rainfall measurement (e.g., 10 mm of rain).",
        "Mile": "A traditional unit in the US and UK, equal to 1,609.34 meters. Often used for road distances or aviation.",
        "Yard": "Equal to 0.9144 meters or 3 feet, used in the US for fabric measurements, sports fields (e.g., football), or gardening.",
        "Foot": "One-third of a yard (0.3048 m), widely used in the US for height, construction, and aviation (e.g., altitude in feet).",
        "Inch": "One-twelfth of a foot (0.0254 m), common for small measurements like screen sizes, paper dimensions, or hardware."
    },
    "Mass": {
        "Kilogram": "The SI base unit of mass, defined by the mass of the international prototype kilogram until 2019, now tied to Planck's constant. Used worldwide for weight.",
        "Gram": "One-thousandth of a kilogram (0.001 kg), ideal for small items like food ingredients or jewelry.",
        "Milligram": "One-millionth of a kilogram (0.000001 kg), used in pharmaceuticals for tiny doses (e.g., 500 mg of aspirin).",
        "Metric Ton": "Equal to 1000 kilograms, used for heavy objects like vehicles, cargo, or industrial materials.",
        "Pound": "An imperial unit (0.453592 kg), common in the US for body weight, groceries, or shipping.",
        "Ounce": "One-sixteenth of a pound (0.0283495 kg), used for lightweight items like food portions or postal weights.",
        "Stone": "Equal to 14 pounds (6.35029 kg), a traditional UK unit still used informally for body weight."
    },
    "Temperature": {
        "Celsius": "A metric scale where water freezes at 0°C and boils at 100°C at standard pressure. Used globally for weather and science.",
        "Fahrenheit": "An imperial scale where water freezes at 32°F and boils at 212°F. Common in the US for weather and cooking.",
        "Kelvin": "The SI unit of temperature, starting at absolute zero (0 K = -273.15°C). Used in physics and engineering."
    },
    "Area": {
        "Square Meter": "The SI unit of area, used for land, rooms, or building plans (e.g., a small apartment might be 50 m²).",
        "Square Kilometer": "Equal to 1,000,000 square meters, used for large areas like cities or national parks.",
        "Hectare": "Equal to 10,000 square meters, common in agriculture and forestry (e.g., a farm might be 5 hectares).",
        "Acre": "An imperial unit (4046.86 m²), widely used in the US and UK for land measurement (e.g., real estate).",
    },
    "Volume": {
        "Cubic Meter": "The SI unit of volume, used for large spaces like warehouses or water tanks (e.g., 1 m³ = 1000 liters).",
        "Liter": "Equal to 0.001 cubic meters, used worldwide for liquids like beverages or fuel.",
        "Gallon (US)": "Equal to 3.78541 liters, common in the US for fuel, milk, or paint containers.",
        "Fluid Ounce (US)": "One-sixteenth of a pint (0.0295735 liters), used for small liquid measurements like cooking ingredients."
    },
    "Fuel Economy": {
        "Miles per gallon (US)": "The standard measure of fuel efficiency in the US, representing distance traveled per unit of fuel.",
        "Miles per gallon (UK)": "Similar to US MPG but using the larger imperial gallon, resulting in higher values for the same efficiency.",
        "Kilometer per liter": "The metric equivalent of MPG, common in many countries outside the US and UK.",
        "Liter per 100 kilometers": "The inverse of efficiency (fuel consumption rather than economy), standard in Europe and many other regions."
    }
}

def convert_value(value, from_unit, to_unit, category):
    """Convert a value from one unit to another within a specified category."""
    try:
        if category == "Temperature":
            if from_unit == "Kelvin" and value < 0:
                raise ValueError("Kelvin temperature cannot be negative.")
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                return value + 273.15
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                return (value - 32) * 5/9
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                return value - 273.15
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
            return value

        elif category == "Fuel Economy":
            if from_unit == to_unit:
                return value
                
            if from_unit == "Liter per 100 kilometers":
                if value == 0:
                    raise ZeroDivisionError("Cannot convert with zero value.")
                if to_unit == "Miles per gallon (US)":
                    return 235.214 / value
                elif to_unit == "Miles per gallon (UK)":
                    return 282.481 / value
                elif to_unit == "Kilometer per liter":
                    return 100 / value
            elif to_unit == "Liter per 100 kilometers":
                if value == 0:
                    raise ZeroDivisionError("Cannot convert with zero value.")
                if from_unit == "Miles per gallon (US)":
                    return 235.214 / value
                elif from_unit == "Miles per gallon (UK)":
                    return 282.481 / value
                elif from_unit == "Kilometer per liter":
                    return 100 / value
            else:
                # For other fuel economy conversions where both units have numerical factors
                return value * (conversion_data[category][from_unit] / conversion_data[category][to_unit])

        if from_unit == to_unit:
            return value
        return value * (conversion_data[category][from_unit] / conversion_data[category][to_unit])

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError as e:
        return f"Error: {str(e)}"

def get_formula(from_unit, to_unit, category, from_value, to_value):
    """Generate a human-readable formula for the conversion."""
    if isinstance(to_value, str):
        return "Conversion failed due to invalid input."
    
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return f"multiply by 9/5, then add 32: ({from_value} × 9/5) + 32 = {to_value}"
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return f"add 273.15: {from_value} + 273.15 = {to_value}"
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return f"subtract 32, then multiply by 5/9: ({from_value} - 32) × 5/9 = {to_value}"
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return f"subtract 32, multiply by 5/9, then add 273.15: ({from_value} - 32) × 5/9 + 273.15 = {to_value}"
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return f"subtract 273.15: {from_value} - 273.15 = {to_value}"
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return f"subtract 273.15, multiply by 9/5, then add 32: ({from_value} - 273.15) × 9/5 + 32 = {to_value}"
        return "no conversion needed"

    elif category == "Fuel Economy":
        if from_unit == to_unit:
            return "no conversion needed"
            
        if from_unit == "Liter per 100 kilometers" and to_unit == "Miles per gallon (US)":
            return f"divide 235.214 by the value: 235.214 ÷ {from_value} = {to_value}"
        elif from_unit == "Liter per 100 kilometers" and to_unit == "Miles per gallon (UK)":
            return f"divide 282.481 by the value: 282.481 ÷ {from_value} = {to_value}"
        elif from_unit == "Liter per 100 kilometers" and to_unit == "Kilometer per liter":
            return f"divide 100 by the value: 100 ÷ {from_value} = {to_value}"
        elif to_unit == "Liter per 100 kilometers" and from_unit == "Miles per gallon (US)":
            return f"divide 235.214 by the value: 235.214 ÷ {from_value} = {to_value}"
        elif to_unit == "Liter per 100 kilometers" and from_unit == "Miles per gallon (UK)":
            return f"divide 282.481 by the value: 282.481 ÷ {from_value} = {to_value}"
        elif to_unit == "Liter per 100 kilometers" and from_unit == "Kilometer per liter":
            return f"divide 100 by the value: 100 ÷ {from_value} = {to_value}"
        else:
            # For other fuel economy conversions
            if from_unit in conversion_data[category] and to_unit in conversion_data[category]:
                if isinstance(conversion_data[category][from_unit], (int, float)) and isinstance(conversion_data[category][to_unit], (int, float)):
                    factor = conversion_data[category][from_unit] / conversion_data[category][to_unit]
                    return f"multiply the {from_unit} value by {factor:.6g}: {from_value} × {factor:.6g} = {to_value}"
            return f"special conversion: {from_value} {from_unit} → {to_value} {to_unit}"

    else:
        if from_unit == to_unit:
            return "no conversion needed"
        from_factor = conversion_data[category][from_unit]
        to_factor = conversion_data[category][to_unit]
        conversion_factor = from_factor / to_factor
        if conversion_factor > 1:
            return f"multiply the {from_unit} value by {conversion_factor:.6g}: {from_value} × {conversion_factor:.6g} = {to_value}"
        return f"divide the {from_unit} value by {1/conversion_factor:.6g}: {from_value} ÷ {1/conversion_factor:.6g} = {to_value}"

def get_conversion_details(from_unit, to_unit, category, from_value, to_value):
    """Provide a detailed explanation of the conversion process with unit context."""
    if isinstance(to_value, str):
        return f"Conversion failed: {to_value}"

    explanation = f"Converting {from_value} {from_unit} to {to_unit}:\n\n"

    # Add unit descriptions
    if category in unit_descriptions and from_unit in unit_descriptions[category]:
        explanation += f"**{from_unit}**: {unit_descriptions[category][from_unit]}\n"
    if category in unit_descriptions and to_unit in unit_descriptions[category] and from_unit != to_unit:
        explanation += f"**{to_unit}**: {unit_descriptions[category][to_unit]}\n"

    # Conversion explanation
    explanation += f"\n**How it works**: Converting {from_value} {from_unit} to {to_unit} "
    
    if category == "Length":
        if from_unit == "Meter" and to_unit == "Centimeter":
            explanation += "involves multiplying by 100 since 1 meter equals 100 centimeters. This is useful for scaling down from larger to smaller measurements."
        elif from_unit == "Kilometer" and to_unit == "Meter":
            explanation += "involves multiplying by 1000 since 1 kilometer equals 1000 meters. This scales up from long distances to a base unit."
        elif from_unit == "Foot" and to_unit == "Inch":
            explanation += "involves multiplying by 12 since 1 foot equals 12 inches, commonly used in imperial systems for finer measurements."
        elif from_unit == "Mile" and to_unit == "Kilometer":
            explanation += "converts from an imperial unit to a metric one using the factor 1 mile ≈ 1.60934 kilometers."
        else:
            explanation += f"uses the ratio between {from_unit} and {to_unit} based on their metric or imperial definitions."

        # Contextual examples
        if from_unit == "Meter" and 1.5 <= from_value <= 2.0:
            explanation += "\n\n**Context**: This range is typical for human heights (e.g., 1.7 m ≈ 5'7\")."
        elif from_unit == "Kilometer" and from_value >= 1:
            explanation += "\n\n**Context**: A kilometer is about the distance of a short walk or a city block."

    elif category == "Mass":
        if from_unit == "Kilogram" and to_unit == "Gram":
            explanation += "involves multiplying by 1000 since 1 kilogram equals 1000 grams, useful for small-scale measurements."
        elif from_unit == "Pound" and to_unit == "Kilogram":
            explanation += "converts from imperial to metric using 1 pound ≈ 0.453592 kilograms."
        elif from_unit == "Gram" and to_unit == "Milligram":
            explanation += "involves multiplying by 1000 since 1 gram equals 1000 milligrams, common in precision tasks."
        else:
            explanation += f"uses the proportional relationship between {from_unit} and {to_unit}."

        if from_unit == "Kilogram" and 1 <= from_value <= 5:
            explanation += "\n\n**Context**: A bag of sugar is typically 1 kg, and a laptop weighs about 1.5-2.5 kg."
        elif from_unit == "Pound" and 5 <= from_value <= 20:
            explanation += "\n\n**Context**: This could represent the weight of a small pet or a grocery bag."

    elif category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            explanation += "uses the formula °F = (°C × 9/5) + 32 to shift from metric to imperial scales."
            if from_value == 0:
                explanation += " This is the freezing point of water (0°C = 32°F)."
            elif from_value == 100:
                explanation += " This is the boiling point of water (100°C = 212°F)."
            elif from_value == 37:
                explanation += " This is normal human body temperature (37°C ≈ 98.6°F)."
            elif from_value <= 0:
                explanation += "\n\n**Context**: Below 0°C, water freezes, leading to frost or snow."
            elif 35 <= from_value <= 40:
                explanation += "\n\n**Context**: This range includes human body temperature (37°C)."
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            explanation += "subtracts 273.15 since Kelvin starts at absolute zero (0 K = -273.15°C)."

    elif category == "Area":
        if from_unit == "Square Meter" and to_unit == "Hectare":
            explanation += "divides by 10,000 since 1 hectare equals 10,000 square meters."
        elif from_unit == "Acre" and to_unit == "Square Meter":
            explanation += "multiplies by 4046.86 since 1 acre equals 4046.86 square meters."
        else:
            explanation += f"uses the conversion factor between {from_unit} and {to_unit}."
        if from_unit == "Acre" and 1 <= from_value <= 10:
            explanation += "\n\n**Context**: An acre is about the size of a football field (without end zones)."

    elif category == "Volume":
        if from_unit == "Liter" and to_unit == "Gallon (US)":
            explanation += "multiplies by 0.264172 since 1 liter equals 0.264172 US gallons."
        elif from_unit == "Cubic Meter" and to_unit == "Liter":
            explanation += "multiplies by 1000 since 1 cubic meter equals 1000 liters."
        else:
            explanation += f"uses the proportional relationship between {from_unit} and {to_unit}."
        if from_unit == "Liter" and 1 <= from_value <= 5:
            explanation += "\n\n**Context**: A typical water bottle is 0.5-1 liter, and a car fuel tank might hold 50 liters."
    
    elif category == "Fuel Economy":
        if from_unit == "Liter per 100 kilometers" and to_unit.startswith("Miles per gallon"):
            explanation += f"uses the inverse relationship between these units. L/100km measures consumption (lower is better), while MPG measures economy (higher is better)."
            explanation += f" The conversion uses the formula MPG = 235.214 ÷ L/100km for US gallons or 282.481 ÷ L/100km for UK gallons."
        elif to_unit == "Liter per 100 kilometers" and from_unit.startswith("Miles per gallon"):
            explanation += f"converts from an economy measure (MPG) to a consumption measure (L/100km) using the formula L/100km = 235.214 ÷ MPG for US gallons or 282.481 ÷ MPG for UK gallons."
        else:
            explanation += f"applies the appropriate conversion factor between these fuel economy units."
            
        if from_unit == "Miles per gallon (US)" and 20 <= from_value <= 30:
            explanation += "\n\n**Context**: This is a typical fuel economy range for many passenger cars in the US."
        elif from_unit == "Liter per 100 kilometers" and 5 <= from_value <= 10:
            explanation += "\n\n**Context**: This is a common consumption range for modern passenger vehicles in Europe and many other regions."

    explanation += f"\n\n**Result**: {from_value} {from_unit} equals {to_value} {to_unit}."
    return explanation

# Main App UI
st.markdown("<h1 class='main-header'>Multi-Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Convert between different units of measurement</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])

with col1:
    st.markdown("### Categories")
    category = st.selectbox("Select category", list(conversion_data.keys()), label_visibility="collapsed")

with col2:
    st.markdown("<div class='category-card'>", unsafe_allow_html=True)
    st.markdown(f"### {category} Conversion")
    
    col_from, col_equal, col_to = st.columns([2, 1, 2])
    
    with col_from:
        from_unit = st.selectbox("From", list(conversion_data[category].keys()), key="from_unit")
        from_value = st.number_input("Enter value", value=1.0, format="%.8f", key="from_value")
    
    with col_equal:
        st.markdown("<div style='text-align: center; font-size: 2rem; margin-top: 1.7rem;'>=</div>", unsafe_allow_html=True)
    
    with col_to:
        to_unit = st.selectbox("To", list(conversion_data[category].keys()), key="to_unit")
        to_value = convert_value(from_value, from_unit, to_unit, category)
        
        precision = 2 if category in ["Temperature", "Fuel Economy"] else 4
        if isinstance(to_value, float):
            st.markdown(f"<div class='value-display'>{to_value:.{precision}f}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='value-display'>{to_value}</div>", unsafe_allow_html=True)
    
    formula = get_formula(from_unit, to_unit, category, from_value, to_value)
    st.markdown(f"<div class='formula-box'><strong>Formula:</strong> {formula}</div>", unsafe_allow_html=True)
    
    detailed_explanation = get_conversion_details(from_unit, to_unit, category, from_value, to_value)
    st.markdown(f"<div class='conversion-details'><strong>Details:</strong>\n{detailed_explanation}</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Developed by Riaz Hussain | © 2025 Multi-Unit Converter</div>", unsafe_allow_html=True)