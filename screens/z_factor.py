import streamlit as st 
from components.cards import card
from components.inputs import value_input
from utils.validation import safe_float
from utils.mappings import (Z_CORRELATIONS , CRITICAL_CORRECTIONS , CRITICAL_CORRELATIONS)
from calculations.units import (convert_pressure , convert_temperature)
from charts.z_factor import standing_katz
from theory import z_factor_theory


def show (): 

    if "results" not in st.session_state:
            st.session_state.results = {
                "z": 0.0,
                "ppr": 0.0,
                "tpr": 0.0,
                "ppc": 0.0,
                "tpc": 0.0,
            }

    st.title ("Gas Compressibility Factor (Z-Factor)")

    st.markdown ("Calculate the gas compressibility factor using empirical correlations such as Papay, Hall–Yarborough, and Dranchuk–Abou-Kassem.")

    calctab , chartstab , theorytab = st.tabs (["Calculator" , "Charts" , "Theory"])
    with calctab : 

        left, right = st.columns(2)

        with left:
            with card("Input Parameters"):

                pressure, p_unit = value_input(
                    "Pressure",
                    value = 0,
                    required= True,
                    units = ["Pa" , "KPa","MPa" , "bar" , "atm" , "psia"],
                    key="pressure"
                )

                temperature, t_unit = value_input(
                    "Temperature",
                    value = 0,
                    units = ["°F","°C","K","°R"],
                    key="temperature",
                    required = True
                )

                gas_density , _ = value_input (
                    "Gas Specific Gravity",
                    value = 0,
                    required = True,
                    key = "gas_density")
                
                have_impurities = st.checkbox (
                    "Gas contains impurities",
                    value = False
                )
                if have_impurities : 
                    correction_method = st.selectbox(
                            "Correction",
                            options = [
                                "Wichert Aziz",
                                "Carr Kobayashi Burrows",
                            ]
                    )
                    yco2,_ = value_input (
                        "CO2 Fraction",
                        value = 0,
                        suffix = "%",
                        key = "yco2"
                    )
                    yh2s,_ = value_input (
                        "H2S Fraction" ,
                        value = 0,
                        suffix = "%",
                        key = "yh2s"
                    )
                    yN2,_ = value_input (
                            "N2 Fraction",
                            value = 0,
                            suffix = "%",
                            key = "yN2"
                        )
                        
            

        
                
        with right:
            with card("Calculation Options"):

                correlation = st.selectbox(
                    "Correlation",
                    options=[
                        "PapayJ",
                        "Hall-Yarborough", 
                        "Dranchuk Abou-Kassem",
                        "Dranchuk Purvis Robinson",
                        "Hakinson Thomas Philips",
                        "Brill",
                        "Brill and Beggs",
                        ]
                )

            

                critical_mode = st.radio(
                    "Critical Properties",
                    ["Auto", "Manual"],
                    horizontal=True
                )
                

                if critical_mode == "Auto":
                    critical_method = st.selectbox(
                            "Correlation",
                            [
                            "Standing",
                            "Katz",
                            "Sutton",
                            
                            ]
                        )
                    
                else:

                    ppc_M, ppc_M_unit = value_input(
                        "Pseudo-critical Pressure",
                        units = ["psia" , "Pa" , "KPa","MPa" , "bar" , "atm"],
                        value=0,
                        key="ppc",
                    )

                    tpc_M, tpc_M_unit = value_input(
                        "Pseudo-critical Temperature",
                        units = ["°R" ,"°F","°C","K"],
                        value=0,
                        key="tpc",
                    )
        st.divider()

        c1, c2, c3= st.columns([1,2,1])

        with c2:
            calculate = st.button(
                "Calculate",
                use_container_width=True,
                type="primary"
            )

        
        st.divider()

        
        
        

        if calculate:
            pressure = convert_pressure (pressure , p_unit , "psia")
            temperature = convert_temperature (temperature , t_unit , "°R")
            ppc , tpc = None , None
            if critical_mode == "Auto":

                ppc, tpc = CRITICAL_CORRELATIONS[critical_method](gas_density)

                if have_impurities:
                    ppc, tpc = CRITICAL_CORRECTIONS[correction_method](
                        ppc,
                        tpc,
                        yCO2=yco2/100,
                        yH2S=yh2s/100,
                        yN2=yN2/100
                    )

            
            else:
                ppc = convert_pressure (ppc_M , ppc_M_unit , "psia")
                tpc = convert_temperature (tpc_M , tpc_M_unit , "°R")

            
            ppr = pressure / ppc
            tpr = temperature / tpc

           
            z = Z_CORRELATIONS[correlation](ppr, tpr)

            
            st.session_state.results = {
                "z": z,
                "ppr": ppr,
                "tpr": tpr,
                "ppc": ppc,
                "tpc": tpc,
            }

        
            
        results = st.session_state.results     
        with card("Results"):

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "Z-Factor",
                    f"{results["z"]:.4f}"
                )

            with c2:
                st.metric(
                    "Ppr",
                    f"{results["ppr"]:.2f}"
                )

            with c3:
                st.metric(
                    "Tpr",
                    f"{results["tpr"]:.2f}"
                )

            st.divider()

            c4, c5 = st.columns(2)

            with c4:
                st.metric(
                    "Ppc",
                    f"{results["ppc"]:.2f}"
                )

            with c5:
                st.metric(
                    "Tpc",
                    f"{results["tpc"]:.2f}"
                )
                
                

    with chartstab : 
        

        left , right = st.columns (2)
        with left :
            ppr_min, ppr_max = st.slider(
                    "Ppr Range",
                    min_value=0.2,
                    max_value=20.0,
                    value=(0.2, 7.0),
                )
            tpr_values = st.multiselect(
                    "Tpr Curves",
                    options=[
                        
                        0.7,
                        0.75,
                        0.8,
                        0.85,
                        0.9,
                        1.00,
                        1.02,
                        1.05,
                        1.10,
                        1.15,
                        1.20,
                        1.30,
                        1.40,
                        1.50,
                        1.60,
                        1.70,
                        1.80,
                        2.00,
                        2.20,
                        2.50,
                        3.00,
                        3.50,
                        4.00,
                    ],
                    default=[
                        0.7,
                        0.75,
                        0.8,
                        1.05,
                        1.10,
                        1.20,
                        1.30,
                        1.50,
                        2.00,
                    ],
                )
        
        with right : 
            chart_correlation = st.selectbox (
                "Correlation",
                options = [
                    "PapayJ",
                    "Hall-Yarborough",
                    "Dranchuk Abou-Kassem",
                    "Dranchuk Purvis Robinson",
                    "Hankinson Thomas Philips",
                    "Brill",
                    "Brill and Beggs"
                ])
            col1 , col2 = st.columns (2)
            with col1 : 
                custom_ppr = safe_float (st.text_input ("Ppr"))
            with col2 : 
                custom_tpr = safe_float (st.text_input ("Tpr"))

        fig = standing_katz(
                z_function=Z_CORRELATIONS[chart_correlation],
                tpr_values=tpr_values,
                ppr_min=ppr_min,
                ppr_max=ppr_max,
                points=100,
                custom_ppr=custom_ppr,
                custom_tpr=custom_tpr,
                )

        st.plotly_chart(fig, use_container_width=True)        
                    
   
    with theorytab : 
        z_factor_theory.show()
        
    