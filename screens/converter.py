import streamlit as st

from calculations.units import (
    PRESSURE,
    DENSITY,
    MOLAR_MASS,
    VOLUME,
    GAS_VOLUME,
    VISCOSITY,
    COMPRESSIBILITY,
    PERMEABILITY,
    LENGTH,
    AREA,
    FLOWRATE,

    convert_pressure,
    convert_density,
    convert_molar_mass,
    convert_volume,
    convert_gas_volume,
    convert_viscosity,
    convert_compressibility,
    convert_permeability,
    convert_length,
    convert_area,
    convert_flowrate,
    convert_temperature,
    api_to_specific_gravity,
    specific_gravity_to_api,
)


def show():

    st.title("Unit Converter")
    st.write("Convert common petroleum engineering units.")
    st.divider()

    # ==========================
    # CATEGORY
    # ==========================

    category = st.selectbox(
        "Category",
        [
            "Pressure",
            "Temperature",
            "Density",
            "Molar Mass",
            "Volume",
            "Gas Volume",
            "Viscosity",
            "Compressibility",
            "Permeability",
            "Length",
            "Area",
            "Flow Rate",
            "API Gravity",
        ],
    )

    st.divider()

    # ==========================
    # API GRAVITY
    # ==========================

    if category == "API Gravity":

        st.subheader("API Gravity")

        conversion_type = st.radio(
            "Conversion",
            [
                "API → Specific Gravity",
                "Specific Gravity → API",
            ],
            horizontal=True,
        )

        value = st.number_input(
            "Value",
            value=0.0,
        )

        if conversion_type == "API → Specific Gravity":

            result = api_to_specific_gravity(value)

            st.metric(
                "Specific Gravity",
                f"{result:.6g}",
            )

        else:

            result = specific_gravity_to_api(value)

            st.metric(
                "API Gravity",
                f"{result:.6g} °API",
            )

        return

    # ==========================
    # TEMPERATURE
    # ==========================

    if category == "Temperature":

        units = [
            "K",
            "°C",
            "°F",
            "°R",
        ]

        conversion_function = convert_temperature

    # ==========================
    # OTHER CATEGORIES
    # ==========================

    else:

        category_data = {

            "Pressure": (
                PRESSURE,
                convert_pressure,
            ),

            "Density": (
                DENSITY,
                convert_density,
            ),

            "Molar Mass": (
                MOLAR_MASS,
                convert_molar_mass,
            ),

            "Volume": (
                VOLUME,
                convert_volume,
            ),

            "Gas Volume": (
                GAS_VOLUME,
                convert_gas_volume,
            ),

            "Viscosity": (
                VISCOSITY,
                convert_viscosity,
            ),

            "Compressibility": (
                COMPRESSIBILITY,
                convert_compressibility,
            ),

            "Permeability": (
                PERMEABILITY,
                convert_permeability,
            ),

            "Length": (
                LENGTH,
                convert_length,
            ),

            "Area": (
                AREA,
                convert_area,
            ),

            "Flow Rate": (
                FLOWRATE,
                convert_flowrate,
            ),
        }

        units_dict, conversion_function = category_data[category]

        units = list(units_dict.keys())

    # ==========================
    # INPUTS
    # ==========================

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:

        value = st.number_input(
            "Value",
            value=0.0,
        )

    with col2:

        from_unit = st.selectbox(
            "From",
            units,
        )

    with col3:

        to_unit = st.selectbox(
            "To",
            units,
            index=1 if len(units) > 1 else 0,
        )

    st.divider()

    # ==========================
    # CONVERSION
    # ==========================

    try:

        result = conversion_function(
            value,
            from_unit,
            to_unit,
        )

        st.subheader("Result")

        st.metric(
            label=f"{from_unit} → {to_unit}",
            value=f"{result:.6g} {to_unit}",
        )

    except (KeyError, ValueError, ZeroDivisionError) as e:

        st.error(f"Conversion error: {e}")