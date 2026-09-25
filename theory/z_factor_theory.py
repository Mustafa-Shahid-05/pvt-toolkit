import streamlit as st


def show ():
        st.header("📚 Gas Compressibility Factor (Z-Factor)")

        st.markdown("""
        The **gas compressibility factor (Z)** is a dimensionless property that
        describes the deviation of a real gas from ideal gas behavior.

        For an ideal gas, intermolecular forces are neglected and:

        - **Z = 1**

        Real gases, however, experience attractive and repulsive molecular forces,
        causing deviations from the ideal gas law. These deviations become more
        significant at high pressures and low temperatures.

        The compressibility factor is one of the most important properties in
        petroleum engineering because it is required in the calculation of gas
        formation volume factor, gas density, gas compressibility, reserves,
        and pipeline flow.
        """)
        with st.expander("📐 Real Gas Law", expanded=True):

                st.latex(r"PV=ZnRT")

                st.markdown("""
            where

            - **P** = Pressure
            - **V** = Gas volume
            - **n** = Number of moles
            - **R** = Universal gas constant
            - **T** = Absolute temperature
            - **Z** = Compressibility factor

            ### Physical interpretation

            - **Z = 1** → Ideal gas
            - **Z < 1** → Attractive forces dominate.
            - **Z > 1** → Repulsive forces dominate.

            As pressure increases, gases become less ideal and Z departs from unity.
            """)
        with st.expander("📊 Reduced Properties"):

            st.markdown("""
            Most generalized compressibility correlations are expressed using
            reduced properties instead of actual pressure and temperature.
            """)

            st.latex(r"P_{pr}=\frac{P}{P_{pc}}")

            st.latex(r"T_{pr}=\frac{T}{T_{pc}}")

            st.markdown("""
            where

            - **Ppc** = Pseudo-critical pressure
            - **Tpc** = Pseudo-critical temperature

            Using reduced properties allows different natural gases to be represented
            by a common generalized relationship.
            """)
        with st.expander("📈 Standing–Katz Chart"):

            st.markdown("""
            The Standing–Katz chart, introduced in **1942**, is the classical
            generalized compressibility chart for natural gases.

            It consists of curves of constant reduced temperature (**Tpr**)
            plotted against reduced pressure (**Ppr**).

            Most modern Z-factor correlations were developed by fitting mathematical
            expressions to this chart.

            Although computers now calculate Z directly, the Standing–Katz chart
            remains an essential educational and engineering reference.
            """)
        with st.expander("Papay (1968)"):

            st.markdown("### Equation")

            st.latex(r"""
                Z=
                1-
                \frac{3.53P_{pr}}
                {10^{0.9813T_{pr}}}
                +
                \frac{0.274P_{pr}^{2}}
                {10^{0.8157T_{pr}}}
                """)

            st.markdown("""
                **Characteristics**

                - Explicit correlation
                - No numerical iteration
                - Very fast computation
                - Suitable for quick engineering calculations
                """)
        with st.expander("Hall–Yarborough (1973)"):

            st.markdown("### Auxiliary variables")

            st.latex(r"t=\frac{1}{T_{pr}}")

            st.latex(r"""
                X_1=-0.06125tP_{pr}
                e^{-1.2(1-t^2)}
                """)

            st.latex(r"""
                X_2=14.76t-9.76t^2+4.58t^3
                """)

            st.latex(r"""
                X_3=90.7t-242.2t^2+42.4t^3
                """)

            st.latex(r"""
                X_4=2.18+2.82t
                """)

            st.markdown("### Nonlinear equation")

            st.latex(r"""
                \frac{Y+Y^2+Y^3-Y^4}{(1-Y)^3}
                -
                X_2Y^2
                +
                X_3Y^{X_4}
                +
                X_1
                =
                0
                """)

            st.markdown("After solving for **Y**:")

            st.latex(r"Z=-\frac{X_1}{Y}")

            st.info("This correlation requires Newton–Raphson iteration.")

        with st.expander("Dranchuk–Abou-Kassem (1975)"):

            st.markdown("""
                    This correlation is one of the most widely used mathematical
                    representations of the Standing–Katz chart.
                    """)

            st.latex(r"""
                    1
                    +
                    \left(
                    A_1+\frac{A_2}{T_{pr}}
                    +\frac{A_3}{T_{pr}^2}
                    +\frac{A_4}{T_{pr}^4}
                    +\frac{A_5}{T_{pr}^5}
                    \right)\rho_r
                    +
                    \left(
                    A_6+\frac{A_7}{T_{pr}}
                    +\frac{A_8}{T_{pr}^2}
                    \right)\rho_r^2
                    -
                    A_9
                    \left(
                    \frac{A_7}{T_{pr}}
                    +\frac{A_8}{T_{pr}^2}
                    \right)\rho_r^5
                    +
                    A_{10}
                    \left(
                    1+A_{11}\rho_r^2
                    \right)
                    \frac{\rho_r^2e^{-A_{11}\rho_r^2}}
                    {T_{pr}^3}
                    -
                    \frac{0.27P_{pr}}
                    {\rho_rT_{pr}}
                    =0
                    """)

            st.latex(r"""
                    Z=
                    \frac{0.27P_{pr}}
                    {\rho_rT_{pr}}
                    """)

            st.success("""
                    One of the most accurate generalized compressibility correlations
                    for natural gases.
                    """)
                
        with st.expander("Dranchuk–Purvis–Robinson (1974)"):

                st.markdown("""
                The Dranchuk–Purvis–Robinson (DPR) correlation is an implicit equation
                derived from the Benedict–Webb–Rubin equation of state.

                It predicts the compressibility factor by solving for **Z** iteratively.
                """)

                st.markdown("### Governing Equation")

                st.latex(r"""
                    1+
                    \left(
                    A_1+\frac{A_2}{T_{pr}}
                    +\frac{A_3}{T_{pr}^3}
                    \right)\rho_r
                    +
                    \left(
                    A_4+\frac{A_5}{T_{pr}}
                    \right)\rho_r^2
                    +
                    \frac{A_5A_6}{T_{pr}}\rho_r^5
                    +
                    \frac{A_7}{T_{pr}^3}
                    \rho_r^2
                    \left(
                    1+A_8\rho_r^2
                    \right)
                    e^{-A_8\rho_r^2}
                    =
                    Z
                    """)

                st.latex(r"""
                    \rho_r=\frac{0.27P_{pr}}{ZT_{pr}}
                    """)

                st.info("""
                    The equation is solved iteratively because Z appears on both sides.
                    """)

                st.markdown("""
                    **Characteristics**

                    - Implicit correlation
                    - Good numerical stability
                    - High accuracy
                    - Suitable for computer implementation
                    """)
        with st.expander("Hankinson–Thomas–Phillips"):

                st.markdown("""
                    The Hankinson–Thomas–Phillips (HTP) correlation uses two different sets
                    of coefficients depending on the reduced pressure.

                    This improves prediction accuracy over a wider operating range.
                    """)

                st.markdown("### Governing Equation")

                st.latex(r"""
                    \frac{1}{Z}
                    -
                    1
                    +
                    \left(
                    A_4T_{pr}
                    -
                    A_2
                    -
                    \frac{A_6}{T_{pr}^2}
                    \right)
                    \frac{P_{pr}}
                    {Z^2T_{pr}^2}
                    +
                    \left(
                    A_3T_{pr}
                    -
                    A_1
                    \right)
                    \frac{P_{pr}^2}
                    {Z^3T_{pr}^3}
                    +
                    A_1A_5A_7
                    \frac{P_{pr}^5}
                    {Z^6T_{pr}^6}
                    \left(
                    1+
                    A_8
                    \frac{P_{pr}^2}
                    {Z^2T_{pr}^2}
                    \right)
                    e^{
                    -
                    \left(
                    1+
                    A_8
                    \frac{P_{pr}^2}
                    {Z^2T_{pr}^2}
                    \right)
                    }
                    =
                    0
                    """)

                st.markdown("""
                    **Characteristics**

                    - Implicit correlation
                    - Uses Newton-Raphson iteration
                    - Two coefficient sets
                    - Good performance at both low and high pressures
                    """)
        with st.expander("Brill"):

                st.markdown("""
                    The Brill correlation is a completely explicit empirical equation.
                    It is one of the fastest methods because no iteration is required.
                    """)

                st.markdown("### Auxiliary Parameters")

                st.latex(r"E=9(T_{pr}-1)")

                st.latex(r"F=0.3106-0.49T_{pr}+0.1824T_{pr}^{2}")

                st.latex(r"""
                    A=
                    1.39\sqrt{T_{pr}-0.92}
                    -
                    0.36T_{pr}
                    -
                    0.10
                    """)

                st.latex(r"""
                    B=
                    (0.62-0.23T_{pr})P_{pr}
                    +
                    \left(
                    \frac{0.066}{T_{pr}-0.86}
                    -
                    0.037
                    \right)
                    P_{pr}^{2}
                    +
                    0.32
                    \frac{P_{pr}^{6}}
                    {10^{E}}
                    """)

                st.latex(r"C=0.132-0.32\ln(T_{pr})")

                st.latex(r"D=10^{F}")

                st.markdown("### Final Equation")

                st.latex(r"""
                    Z=
                    A+
                    \frac{1-A}{e^{B}}
                    +
                    CP_{pr}^{D}
                    """)

                st.success("""
                    Explicit correlation requiring no numerical iteration.
                    """)
        with st.expander("Brill & Beggs"):

                st.markdown("""
                    The Brill & Beggs correlation is an implicit formulation based on reduced
                    density and was developed as an improvement over earlier explicit methods.
                    """)

                st.markdown("### Auxiliary Parameters")

                st.latex(r"""
                    A=
                    0.06125
                    \frac{1}{T_{pr}}
                    e^{-1.2(1-\frac{1}{T_{pr}})^2}
                    """)

                st.latex(r"""
                    B=
                    \frac{1}{T_{pr}}
                    \left(
                    14.76
                    -
                    9.76\frac{1}{T_{pr}}
                    +
                    4.58\frac{1}{T_{pr}^{2}}
                    \right)
                    """)

                st.latex(r"""
                    C=
                    \frac{1}{T_{pr}}
                    \left(
                    90.7
                    -
                    242.2\frac{1}{T_{pr}}
                    +
                    42.4\frac{1}{T_{pr}^{2}}
                    \right)
                    """)

                st.latex(r"""
                    D=
                    2.18+
                    2.82
                    \frac{1}{T_{pr}}
                    """)

                st.markdown("### Nonlinear Equation")

                st.latex(r"""
                    \frac{
                    Y+Y^2+Y^3-Y^4
                    }
                    {
                    (1-Y)^3
                    }
                    -
                    AP_{pr}
                    -
                    BY^2
                    +
                    CY^D
                    =
                    0
                    """)

                st.markdown("After solving for **Y**:")

                st.latex(r"""
                    Z=
                    \frac{AP_{pr}}{Y}
                    """)

                st.info("""
                    This correlation requires iterative solution of the nonlinear equation.
                    """)
        with st.expander("⚠ Validity Ranges"):

                st.warning("""
                Every empirical correlation has a recommended range of validity.

                Results outside these ranges may become inaccurate.

                Always consult the original publication when high accuracy is required.
                """)
        with st.expander("📖 References"):

                st.markdown("""
                    1. Standing, M. B., & Katz, D. L. (1942). *Density of Natural Gases*.

                    2. Hall, K. R., & Yarborough, L. (1973). *A New Equation of State for Z-Factor Calculations*.

                    3. Dranchuk, P. M., & Abou-Kassem, J. H. (1975). *Calculation of Z Factors for Natural Gases Using Equations of State*.

                    4. Dranchuk, P. M., Purvis, R. A., & Robinson, D. B. (1974). *Computer Calculation of Natural Gas Compressibility Factors*.

                    5. Papay, J. (1968). *A Correlation for Gas Compressibility*.

                    6. Hankinson, R. W., Thomas, L. K., & Phillips, K. A. *Compressibility Factor Correlations for Natural Gases*.

                    7. Beggs, H. D., & Brill, J. P. *Two-Phase Flow in Pipes*.
                    """)