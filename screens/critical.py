import streamlit as st
from components.cards import card
from components.inputs import value_input
from utils.validation import safe_float
from utils.mappings import CRITICAL_CORRELATIONS, CRITICAL_CORRECTIONS
from calculations.units import convert_pressure, convert_temperature
import pandas as pd
from data.component_database import COMPONENTS , IMPURITIES , ALL_COMPONENTS
import plotly.express as px
from theory import critical_theory


def show():
    if "critical_results" not in st.session_state:
        st.session_state.critical_results = {
            "Gas Specific Gravity": 0.0,
            "Gas Molecular Weight": 0.0,
            "Pseudo-critical Pressure": 0.0,
            "Pseudo-critical Temperature": 0.0,
            "Corrected Pressure": 0.0,
            "Corrected Temperature": 0.0,
        }

    if "critical_results_compo" not in st.session_state : 
        st.session_state.critical_results_compo = {
            
            "Gas Specific Gravity": 0.0,
            "Gas Molecular Weight": 0.0,
            "Pseudo-critical Pressure": 0.0,
            "Pseudo-critical Temperature": 0.0,
        }


    st.title("Pseudo-Critical Properties")

    st.markdown("""
        Estimate the **pseudo-critical pressure (Ppc)** and **pseudo-critical temperature (Tpc)**
        of natural gas mixtures using gas gravity correlations or gas composition (Kay's Mixing Rule).
        Optional impurity corrections are available for gases containing CO₂, H₂S, and N₂ using the
        Wichert–Aziz and Carr–Kobayashi–Burrows methods.
        """)

    CompoTab,CalcTab,TheoryTab = st.tabs(["Composition","Calculator","Theory"])

    with CompoTab : 

        if "composition_df" not in st.session_state:
            st.session_state.composition_df = pd.DataFrame({
                "Component": [None],
                "Mole Fraction": [0.0],
            })

        if "_composition_df_snapshot" not in st.session_state:
            st.session_state._composition_df_snapshot = (
                st.session_state.composition_df.copy()
            )


        with card("Gas Composition"):

            composition_df = st.data_editor(
                st.session_state.composition_df,
                key="composition_editor",
                hide_index=True,
                use_container_width=True,
                num_rows="dynamic",
                column_config={
                    "Component": st.column_config.SelectboxColumn(
                        "Component",
                        options= list (ALL_COMPONENTS.keys()),
                        required=True,
                    ),
                    "Mole Fraction": st.column_config.NumberColumn(
                        "Mole Fraction",
                        min_value=0.0,
                        max_value=1.0,
                        step=0.0001,
                        format="%.4f",
                        default=0.0,  
                    ),
                },
            )


        if not composition_df.equals(st.session_state._composition_df_snapshot):
            st.session_state.composition_df = composition_df.copy()
            st.session_state._composition_df_snapshot = composition_df.copy()
            st.rerun()

        st.session_state.composition_df = composition_df.copy()



        properties = []

        for _, row in composition_df.iterrows():

            component = row["Component"]

            if component in ALL_COMPONENTS:

                mole_fraction = safe_float(row["Mole Fraction"])

                properties.append({
                    "Component": component,
                    "y": mole_fraction,
                    "MW": ALL_COMPONENTS[component]["mw"],
                    "Tc (°R)": ALL_COMPONENTS[component]["tc"],
                    "Pc (psia)": ALL_COMPONENTS[component]["pc"],
                })

        properties_df = pd.DataFrame(properties)



        with st.expander("Component Properties", expanded=False):

            if properties_df.empty:

                st.info("No components selected.")

            else:

                st.dataframe(
                    properties_df,
                    hide_index=True,
                    use_container_width=True,
                )
        
        _, col, _ = st.columns([1, 2, 1])
        
        with col:

            calculate = st.button(
                "Calculate",
                type="primary",
                use_container_width=True,
                key = "compo_calc"
            )

        if calculate:

            
        
            if properties_df.empty:

                st.error("Please add at least one component.")

            elif abs(properties_df["y"].sum() - 1.0) > 1e-4:

                st.error("The mole fractions must sum to 1.0000.")

            else:
                

                compo_results = st.session_state.critical_results_compo

                
                
                compo_results["Gas Molecular Weight"] = (
                        properties_df["y"] *
                        properties_df["MW"]
                    ).sum()

                compo_results["Gas Specific Gravity"] = compo_results["Gas Molecular Weight"]/28.97

                compo_results["Pseudo-critical Pressure"] = (
                        properties_df["y"] *
                        properties_df["Pc (psia)"]
                    ).sum()

                compo_results["Pseudo-critical Temperature"]=(
                        properties_df["y"] *
                        properties_df["Tc (°R)"]
                    ).sum()
                


                

        with card("Results"):

            if properties_df.empty:
                st.info("Add at least one component.")
            else:
                compo_results = st.session_state.critical_results_compo

                c2, c3 = st.columns(2)

                

                with c2:
                    st.metric(
                        "Gas MW (kg/kmol)",
                        f"{compo_results["Gas Molecular Weight"]:.3f}",
                    )

                with c3:
                    st.metric(
                        "Gas Gravity",
                        f"{compo_results["Gas Specific Gravity"]:.4f}",
                    )
                st.divider()
                c4,c5 = st.columns(2)
                with c4 : 
                    st.metric (
                        "Ppc (Psia)",
                        f"{compo_results["Pseudo-critical Pressure"]:.2f}"
                    )
                with c5 : 
                    st.metric (
                        "Tpc (°R)",
                        f"{compo_results["Pseudo-critical Temperature"]:.2f}"
                    )

        with st.expander ("Charts",expanded=False):
            if properties_df.empty:
                st.info("Add components and calculate the mixture first.")
            else:
    
                import plotly.express as px
    
                # ==========================================================
                # Derived Columns
                # ==========================================================
    
                properties_df["MW Contribution"] = (
                    properties_df["y"] * properties_df["MW"]
                )
    
                properties_df["Ppc Contribution"] = (
                    properties_df["y"] * properties_df["Pc (psia)"]
                )
    
                properties_df["Tpc Contribution"] = (
                    properties_df["y"] * properties_df["Tc (°R)"]
                )
    
                # ==========================================================
                # Gas Composition
                # ==========================================================
    
                st.subheader("Gas Composition")

                col7,col8 = st.columns (2)

                with col7:
    
                    fig = px.bar(
                        properties_df,
                        x="Component",
                        y="y",
                        text="y",
                        
                    )
        
                    fig.update_traces(texttemplate="%{text:.3f}",
                                    textposition="outside")
        
                    fig.update_layout(
                        height=500,
                        xaxis_title="Component",
                        yaxis_title="Mole Fraction",
                    )
        
                    st.plotly_chart(fig, use_container_width=True)
        
                st.divider()

                with col8 : 

                    fig = px.pie(
                        properties_df,
                        names="Component",
                        values="y",
                        hole=0.35,
                    )
        
                    fig.update_traces(textinfo="percent+label")
        
                    st.plotly_chart(fig, use_container_width=True)
        
                st.divider()

                st.subheader("Molecular Weight Contributions")
    
                col1, col2 = st.columns(2)
    
                with col1:
    
                    fig = px.bar(
                        properties_df,
                        x="Component",
                        y="MW Contribution",
                        text="MW Contribution",
                        title="MW Contributions",
                    )
    
                    fig.update_traces(
                        texttemplate="%{text:.2f}",
                        textposition="outside",
                    )
    
                    fig.update_layout(height=450)
    
                    st.plotly_chart(fig, use_container_width=True)
    
                with col2:
    
                    fig = px.pie(
                        properties_df,
                        names="Component",
                        values="MW Contribution",
                        title="Contribution to Molecular Weight",
                        hole=0.35,
                    )
    
                    st.plotly_chart(fig, use_container_width=True)
    
                st.divider()
    
                st.subheader("Pseudo-critical Pressure Contributions")
    
                left, right = st.columns(2)
    
                with left:
    
                    fig = px.bar(
                        properties_df,
                        x="Component",
                        y="Ppc Contribution",
                        text="Ppc Contribution",
                        
                    )
    
                    fig.update_traces(
                        texttemplate="%{text:.1f}",
                        textposition="outside",
                    )
    
                    fig.update_layout(height=450)
    
                    st.plotly_chart(fig, use_container_width=True)
    
                with right:
                    fig = px.pie(
                        properties_df,
                        names="Component",
                        values="Ppc Contribution",
                        hole=0.35,
                    )
    
                    st.plotly_chart(fig, use_container_width=True)
    
                    
    
                st.divider()
    
                st.subheader("Pseudo-critical Temperature Contributions")
    
                col1, col2 = st.columns(2)
    
                with col1:
                    fig = px.bar(
                        properties_df,
                        x="Component",
                        y="Tpc Contribution",
                        text="Tpc Contribution",
                        
                    )
    
                    fig.update_traces(
                        texttemplate="%{text:.1f}",
                        textposition="outside",
                    )
    
                    fig.update_layout(height=450)
    
                    st.plotly_chart(fig, use_container_width=True)
    
                    
    
                with col2:
    
                    fig = px.pie(
                        properties_df,
                        names="Component",
                        values="Tpc Contribution",
                        
                        hole=0.35,
                    )
    
                    st.plotly_chart(fig, use_container_width=True)

    with CalcTab:
        left, right = st.columns(2)
        with left:
            with card("Input Parameters"):
                    gas_density, _ = value_input(
                        "Gas Specific Gravity",
                        value=0,
                        required=True,
                        key="gas_gravity"
                    )
                    yCO2, _ = value_input(
                        "CO2 Fraction",
                        value=0,
                        required=True,
                        key="yCO2",
                        suffix="%"
                    )
                    yH2S, _ = value_input(
                        "H2S Fraction",
                        value=0,
                        required=True,
                        key="yH2S",
                        suffix="%"
                    )
                    yN2, _ = value_input(
                        "N2 Fraction",
                        value=0,
                        required=True,
                        key="yN2",
                        suffix="%"
                    )
        with right:
            with card("Calculation Options"):
                corrleation = st.selectbox(
                    "Correlation",
                    options=[
                        "Standing",
                        "Katz",
                        "Sutton"
                    ]
                )
                correction = st.selectbox(
                    "Correction",
                    options=[
                        "Wichert Aziz",
                        "Carr Kobayashi Burrows",
                    ]
                )

                c1, c2 = st.columns(2)
                with c1:
                    p_unit = st.selectbox(
                        "Pressure Unit",
                        options=["psia", "Pa", "kPa", "MPa", "bar", "atm"]
                    )
                with c2:
                    t_unit = st.selectbox(
                        "Temperature Unit",
                        options=["°R", "°F", "°C", "K"]
                    )

        st.divider()
        _, col, _ = st.columns([1, 2, 1])

        with col:
            calculate = st.button(
                "Calculate",
                use_container_width=True,
                type="primary"
            )

            if calculate:
                Ma = 28.97 * gas_density

                if corrleation == "Sutton":

                    ppc, tpc = CRITICAL_CORRELATIONS["Sutton"](
                        gas_density,
                        yCO2=yCO2 / 100,
                        yH2S=yH2S / 100,
                        yN2=yN2 / 100,
                    )

                else:

                    ppc, tpc = CRITICAL_CORRELATIONS[corrleation](gas_density)

                ppc_corrected, tpc_corrected = CRITICAL_CORRECTIONS[correction](
                    ppc,
                    tpc,
                    yCO2=yCO2 / 100,
                    yH2S=yH2S / 100,
                    yN2=yN2 / 100,
                    )
                st.session_state.critical_results = {
                    "Gas Specific Gravity": gas_density,
                    "Gas Molecular Weight": Ma,
                    "Pseudo-critical Pressure": ppc,
                    "Pseudo-critical Temperature": tpc,
                    "Corrected Pressure": ppc_corrected,
                    "Corrected Temperature": tpc_corrected,
                }

        st.divider()
        results = st.session_state.critical_results
        with card("Results"):
            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Gas Specific Gravity",
                    f"{results['Gas Specific Gravity']:.2f}")
            with col2:
                st.metric(
                    "Gas Molecular Weight",
                    f"{results['Gas Molecular Weight']:.2f} Kg/Kmol")

            st.divider()
            col3, col4 = st.columns(2)
            with col3:
                st.metric(
                    "Pseudo-critical Pressure (Ppc)",
                    f"{convert_pressure(results['Pseudo-critical Pressure'], 'psia', p_unit):.2f} {p_unit}")
            with col4:
                st.metric(
                    "Pseudo-critical Temperature (Tpc)",
                    f"{convert_temperature(results['Pseudo-critical Temperature'], '°R', t_unit):.2f} {t_unit}")

            st.divider()
            col5, col6 = st.columns(2)
            with col5:
                st.metric(
                    "Corrected Pressure (Ppc')",
                    f"{convert_pressure(results['Corrected Pressure'], 'psia', p_unit):.2f} {p_unit}")
            with col6:
                st.metric(
                    "Corrected Temperature (Tpc')",
                    f"{convert_temperature(results['Corrected Temperature'], '°R', t_unit):.2f} {t_unit}")

       

        
    with TheoryTab:

        critical_theory.show()




