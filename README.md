# PVT Toolkit

A lightweight web-based toolkit for petroleum engineering calculations, built with Python and Streamlit.

PVT Toolkit provides a collection of practical tools for working with petroleum properties, gas behavior, and common oilfield unit conversions.

## Features

### Critical Properties
Calculate pseudo-critical properties using different petroleum engineering correlations.

### Z-Factor
Calculate the gas compressibility factor using several correlations, including:

- Papay
- Hall-Yarborough
- Dranchuk-Abou-Kassem
- Dranchuk-Purvis-Robinson
- Hankinson-Thomas-Phillips

### Unit Converter
Convert common petroleum engineering units, including:

- Pressure
- Temperature
- Density
- Molar Mass
- Volume
- Gas Volume
- Viscosity
- Compressibility
- Permeability
- Length
- Area
- Flow Rate
- API Gravity

## Tech Stack

- Python
- Streamlit
- NumPy
- SciPy

## Project Structure

```text
PVT Toolkit/
│
├── .streamlit/
│   └── config.toml
│
├── app.py
│
├── components/
│   └── sidebar.py
│
├── screens/
│   ├── home.py
│   ├── critical.py
│   ├── z_factor.py
│   └── converter.py
│
├── calculations/
│   ├── critical_properties.py
│   ├── z_factor.py
│   └── converter.py
│
└── utils/
    └── validation.py