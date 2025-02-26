# Multi-Unit Converter

![Python](https://img.shields.io/badge/Python-3.12-blue.svg) ![Streamlit](https://img.shields.io/badge/Streamlit-1.20.0-red.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg)

A powerful and educational multi-unit converter built with Python and Streamlit. Convert measurements across categories like Length, Mass, Temperature, Area, Volume, and more with detailed explanations, real-world context, and intuitive design. Perfect for students, professionals, or anyone needing accurate conversions with added insights.

## Features
- **Extensive Unit Support**: Covers Length, Mass, Temperature, Area, Volume, Time, Speed, and more with precise conversion factors.
- **Rich Details**: Learn about each unit's definition, uses, and real-world examples alongside every conversion.
- **Interactive UI**: Clean, centered layout with custom styling for a seamless user experience.
- **Special Conversions**: Handles complex cases like Temperature (Celsius ↔ Fahrenheit ↔ Kelvin) and Fuel Economy (e.g., L/100km).
- **Error Handling**: Gracefully manages invalid inputs (e.g., negative Kelvin, zero in fuel economy).
- **Optimized Performance**: Uses caching for faster load times.

## Demo
![Multi-Unit Converter Screenshot](https://via.placeholder.com/600x400.png?text=App+Screenshot)  
*Add a real screenshot by capturing your app and uploading it to the repo!*

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Riaz-Hussain-Saifi/Python-Multi-unit-converter.git
   cd Python-Multi-unit-converter
   ```

2. **Install Dependencies**:
   Ensure Python 3.12+ is installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**:
   ```bash
   streamlit run app.py
   ```

## Requirements
- Python 3.12+
- Streamlit >= 1.20.0

Install via `requirements.txt`:
```plaintext
streamlit>=1.20.0
```

## Usage
1. Launch the app with `streamlit run app.py`.
2. Select a category (e.g., Length, Temperature).
3. Choose "From" and "To" units.
4. Enter a value to convert.
5. View the result, formula, and detailed explanation including unit descriptions and context.

### Example
- **Input**: 1.7 Meters to Feet  
- **Output**: 5.58 Feet  
- **Details**: "Meter: The base SI unit... Foot: An imperial unit... How it works: Multiplies by 3.28084... Context: Typical human height... Result: 1.7 Meters equals 5.58 Feet."

## Contributing
Contributions are welcome! To contribute:
- Report bugs or suggest features via [Issues](https://github.com/Riaz-Hussain-Saifi/Python-Multi-unit-converter/issues).
- Fork the repo, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Author
Developed by [Riaz Hussain](https://github.com/Riaz-Hussain-Saifi) | © 2025