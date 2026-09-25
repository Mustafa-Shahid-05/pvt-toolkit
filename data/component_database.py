COMPONENTS = {
    "Methane": {
        "formula": "CH₄",
        "mw": 16.043,
        "tc": 343.33,      # °R
        "pc": 666.4,       # psia
    },
    "Ethane": {
        "formula": "C₂H₆",
        "mw": 30.070,
        "tc": 549.92,
        "pc": 707.8,
    },
    "Propane": {
        "formula": "C₃H₈",
        "mw": 44.097,
        "tc": 665.73,
        "pc": 616.3,
    },
    "i-Butane": {
        "formula": "i-C₄H₁₀",
        "mw": 58.124,
        "tc": 734.13,
        "pc": 529.1,
    },
    "n-Butane": {
        "formula": "n-C₄H₁₀",
        "mw": 58.124,
        "tc": 765.29,
        "pc": 550.7,
    },
    "i-Pentane": {
        "formula": "i-C₅H₁₂",
        "mw": 72.151,
        "tc": 828.77,
        "pc": 490.4,
    },
    "n-Pentane": {
        "formula": "n-C₅H₁₂",
        "mw": 72.151,
        "tc": 845.47,
        "pc": 488.6,
    },
    "n-Hexane": {
        "formula": "C₆H₁₄",
        "mw": 86.178,
        "tc": 913.47,
        "pc": 436.9,
    },
    "n-Heptane": {
        "formula": "C₇H₁₆",
        "mw": 100.205,
        "tc": 972.37,
        "pc": 397.0,
    },

}


IMPURITIES = {

    "Carbon Dioxide": {
        "mw": 44.010,
        "tc": 547.6,
        "pc": 1071.0,
    },

    "Hydrogen Sulfide": {
        "mw": 34.080,
        "tc": 672.4,
        "pc": 1306.0,
    },

    "Nitrogen": {
        "mw": 28.013,
        "tc": 227.2,
        "pc": 492.3,
    },

}

ALL_COMPONENTS = {
    **COMPONENTS,
    **IMPURITIES,
}