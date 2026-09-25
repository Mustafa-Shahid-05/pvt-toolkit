import streamlit as st 
import pandas as pd

def show (): 
    st.title("Pseudo-Critical Properties Theory")
    
    st.markdown("""
    Pseudo-critical pressure (**Ppc**) and pseudo-critical temperature (**Tpc**) are
    fundamental properties used to determine the pseudo-reduced pressure and temperature
    of a natural gas. These parameters are required in numerous petroleum engineering
    calculations, including **gas compressibility factor (Z-factor)**, **gas formation
    volume factor (Bg)**, **gas viscosity**, and many equations of state.

    Since laboratory measurements are often unavailable, several empirical correlations
    have been developed to estimate pseudo-critical properties from gas gravity or gas
    composition. For sour gases containing **CO₂**, **H₂S**, or **N₂**, correction
    methods are commonly applied to improve the estimates.
    """)

    # ==========================================================
    # Standing
    # ==========================================================

    with st.expander("Standing Correlation", expanded=True):

        st.markdown("""
        ### Description

        The Standing correlation is one of the earliest empirical methods used to estimate
        pseudo-critical properties from gas specific gravity.

        In this implementation two equations are used:

        - Original Standing equation for light gases
        - Modified Standing equation for heavier gases

        The switch occurs at **γg = 0.70**.
        """)

        st.markdown("### Applicability")

        st.markdown("""
        - Sweet natural gases
        - Gas gravity between approximately **0.55 and 1.30**
        - No correction for acid gases
        """)

        st.markdown("### Equations")

        st.markdown("##### For γg ≤ 0.70")

        st.latex(r"P_{pc}=709.604-58.718\,\gamma_g")

        st.latex(r"T_{pc}=170.491+307.344\,\gamma_g")

        st.markdown("##### For γg > 0.70")

        st.latex(r"P_{pc}=756.8-131.07\gamma_g-3.6\gamma_g^2")

        st.latex(r"T_{pc}=169.2+349.5\gamma_g-74\gamma_g^2")

        st.markdown("### Inputs")

        st.markdown("""
        - Gas specific gravity
        """)

        st.markdown("### Outputs")

        st.markdown("""
        - Pseudo-critical pressure (Ppc)
        - Pseudo-critical temperature (Tpc)
        """)

        st.markdown("### Advantages")

        st.markdown("""
        - Very simple
        - Fast calculation
        - Good for conventional sweet gases
        """)

        st.markdown("### Limitations")

        st.markdown("""
        - Not recommended for sour gases
        - Accuracy decreases for unusual gas compositions
        """)

    # ==========================================================
    # Katz
    # ==========================================================

    with st.expander("Katz Correlation"):

        st.markdown("""
        ### Description

        The Katz correlation estimates pseudo-critical properties directly from gas
        specific gravity. Similar to Standing, two different equations are employed
        depending on the gas gravity.
        """)

        st.markdown("### Applicability")

        st.markdown("""
        - Sweet natural gases
        - Gas gravity approximately **0.55–1.30**
        """)

        st.markdown("### Equations")

        st.markdown("##### For γg < 0.75")

        st.latex(r"P_{pc}=677+15\gamma_g-37.5\gamma_g^2")

        st.latex(r"T_{pc}=168+325\gamma_g-12.5\gamma_g^2")

        st.markdown("##### For γg ≥ 0.75")

        st.latex(r"P_{pc}=706-51.7\gamma_g-11.1\gamma_g^2")

        st.latex(r"T_{pc}=187+330\gamma_g-71.5\gamma_g^2")

        st.markdown("### Inputs")

        st.markdown("""
        - Gas specific gravity
        """)

        st.markdown("### Outputs")

        st.markdown("""
        - Pseudo-critical pressure (Ppc)
        - Pseudo-critical temperature (Tpc)
        """)

        st.markdown("### Advantages")

        st.markdown("""
        - Simple empirical equations
        - Widely used in petroleum engineering
        """)

        st.markdown("### Limitations")

        st.markdown("""
        - Applicable mainly to sweet gases
        - Does not account for impurities
        """)

    # ==========================================================
    # Sutton
    # ==========================================================

    with st.expander("Sutton Correlation"):

        st.markdown("""
        ### Description

        The Sutton correlation estimates hydrocarbon pseudo-critical properties after
        correcting the gas gravity for the presence of non-hydrocarbon gases.

        Unlike the previous correlations, this implementation first computes the
        equivalent hydrocarbon gas gravity and then estimates the pseudo-critical
        properties.
        """)

        st.markdown("### Step 1 — Hydrocarbon Mole Fraction")

        st.latex(r"y_{HC}=1-y_{H_2S}-y_{CO_2}-y_{N_2}")

        st.markdown("### Step 2 — Corrected Hydrocarbon Gas Gravity")

        st.latex(
            r"\gamma_{HC}"
            r"="
            r"\frac{\gamma_gM_{air}"
            r"-\left(y_{H_2S}M_{H_2S}"
            r"+y_{CO_2}M_{CO_2}"
            r"+y_{N_2}M_{N_2}\right)}"
            r"{y_{HC}M_{air}}"
        )

        st.markdown("where")

        st.latex(r"M_{air}=28.97")

        st.latex(r"M_{H_2S}=34.08")

        st.latex(r"M_{CO_2}=44.01")

        st.latex(r"M_{N_2}=28.01")

        st.markdown("### Step 3 — Pseudo-critical Properties")

        st.latex(r"P_{pc}=744-125.4\gamma_{HC}+5.9\gamma_{HC}^{2}")

        st.latex(r"T_{pc}=164.3+375.7\gamma_{HC}-67.7\gamma_{HC}^{2}")

        st.markdown("### Inputs")

        st.markdown("""
        - Gas specific gravity
        - CO₂ mole fraction
        - H₂S mole fraction
        - N₂ mole fraction
        """)

        st.markdown("### Outputs")

        st.markdown("""
        - Hydrocarbon pseudo-critical pressure
        - Hydrocarbon pseudo-critical temperature
        """)

        st.markdown("### Advantages")

        st.markdown("""
        - Accounts for impurities before estimating critical properties
        - More representative for sour gases
        - Suitable for modern natural gas mixtures
        """)

        st.markdown("### Limitations")

        st.markdown("""
        - Requires gas composition
        - More complex than Standing and Katz
        """)
        # ==========================================================
    # Wichert–Aziz
    # ==========================================================

    with st.expander("Wichert–Aziz Correction"):

        st.markdown("""
        ### Description

        The Wichert–Aziz method is one of the most widely used corrections for
        **sour natural gases** containing carbon dioxide (CO₂) and hydrogen sulfide (H₂S).

        These acid gases reduce the effective pseudo-critical temperature and pressure.
        Rather than replacing the original correlation, the Wichert–Aziz method
        corrects the pseudo-critical properties obtained from Standing, Katz, Sutton,
        or other sweet-gas correlations.
        """)

        st.markdown("### Correction Parameter")

        st.latex(r"Y_A=y_{CO_2}+y_{N_2}")

        st.latex(r"Y_H=y_{H_2S}")

        st.latex(
            r"\varepsilon="
            r"120\left(Y_A^{0.9}-Y_A^{1.6}\right)"
            r"+15\left(Y_H^{0.5}-Y_H^4\right)"
        )

        st.markdown("### Corrected Temperature")

        st.latex(r"T'_{pc}=T_{pc}-\varepsilon")

        st.markdown("### Corrected Pressure")

        st.latex(
            r"P'_{pc}"
            r"="
            r"P_{pc}"
            r"\frac{T'_{pc}}"
            r"{T_{pc}+\varepsilon Y_H(1-Y_H)}"
        )

        st.markdown("### Inputs")

        st.markdown("""
        - Pseudo-critical pressure (Ppc)
        - Pseudo-critical temperature (Tpc)
        - CO₂ mole fraction
        - H₂S mole fraction
        """)

        st.markdown("### Outputs")

        st.markdown("""
        - Corrected pseudo-critical pressure
        - Corrected pseudo-critical temperature
        """)

        st.markdown("### Advantages")

        st.markdown("""
        - Industry standard for sour gas
        - Very accurate for gases containing CO₂ and H₂S
        - Easy to implement
        """)

        st.markdown("### Limitations")

        st.markdown("""
        - Does not explicitly account for nitrogen effects
        - Requires an initial estimate of Ppc and Tpc
        """)

        # ==========================================================
        # Carr–Kobayashi–Burrows
        # ==========================================================

    with st.expander("Carr–Kobayashi–Burrows Correction"):

        st.markdown("""
        ### Description

        The Carr–Kobayashi–Burrows (CKB) method corrects pseudo-critical properties
        for gases containing **CO₂**, **H₂S**, and **N₂**.

        Unlike Wichert–Aziz, this method applies direct empirical corrections
        to both pressure and temperature using the impurity mole fractions.
        """)

        st.markdown("### Corrected Temperature")

        st.latex(
            r"T'_{pc}"
            r"="
            r"T_{pc}"
            r"-80y_{CO_2}"
            r"+130y_{H_2S}"
            r"-250y_{N_2}"
        )

        st.markdown("### Corrected Pressure")

        st.latex(
            r"P'_{pc}"
            r"="
            r"P_{pc}"
            r"-440y_{CO_2}"
            r"+600y_{H_2S}"
            r"-170y_{N_2}"
        )

        st.markdown("### Inputs")

        st.markdown("""
        - Pseudo-critical pressure (Ppc)
        - Pseudo-critical temperature (Tpc)
        - CO₂ mole fraction
        - H₂S mole fraction
        - N₂ mole fraction
        """)

        st.markdown("### Outputs")

        st.markdown("""
        - Corrected pseudo-critical pressure
        - Corrected pseudo-critical temperature
        """)

        st.markdown("### Advantages")

        st.markdown("""
        - Includes nitrogen effects
        - Very simple empirical correction
        - Frequently used in engineering calculations
        """)

        st.markdown("### Limitations")

        st.markdown("""
        - Less rigorous than composition-based methods
        - Accuracy depends on gas composition
        """)

        # ==========================================================
        # Comparison
        # ==========================================================

    with st.expander("Correlation Comparison"):

        comparison = pd.DataFrame({
            "Method": [
                "Standing",
                "Katz",
                "Sutton",
                "Wichert–Aziz",
                "Carr–Kobayashi–Burrows",
            ],
            "Input": [
                "Gas Gravity",
                "Gas Gravity",
                "Gas Gravity + Composition",
                "Ppc, Tpc + CO₂/H₂S",
                "Ppc, Tpc + CO₂/H₂S/N₂",
            ],
            "Suitable for Sour Gas": [
                "No",
                "No",
                "Yes",
                "Yes",
                "Yes",
            ],
            "Complexity": [
                "Low",
                "Low",
                "Medium",
                "Medium",
                "Low",
            ],
        })

        st.dataframe(
            comparison,
            hide_index=True,
            use_container_width=True,
        )

        # ==========================================================
        # References
        # ==========================================================

    with st.expander("References"):

        st.markdown("""
        **Standing, M. B. (1947)**  
        A Pressure-Volume-Temperature Correlation for Mixtures of California Oils and Gases.

        **Katz, D. L., et al.**  
        Handbook of Natural Gas Engineering.

        **Sutton, R. P. (1985)**  
        Compressibility Factors for High Molecular Weight Reservoir Gases.

        **Wichert, E., Aziz, K. (1972)**  
        Calculate Z's for Sour Gases.

        **Carr, Kobayashi and Burrows (1954)**  
        Viscosity of Hydrocarbon Gases Under Pressure.
        """)