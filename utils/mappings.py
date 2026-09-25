"""
Mappings between UI names and calculation functions.
"""

from calculations import z_factor
from calculations import critical



# ===========================
# Z-Factor Correlations
# ===========================

Z_CORRELATIONS = {
    "PapayJ": z_factor.papayJ,
    "Hall-Yarborough": z_factor.hallYarbough,
    "Dranchuk Abou-Kassem": z_factor.dranchukAbouKassem,
    "Dranchuk Purvis Robinson": z_factor.DranchukPurvisRobinson,
    "Hankinson Thomas Philips": z_factor.HankinsonThomasPhilips,
    "Brill": z_factor.Brill,
    "Brill and Beggs": z_factor.BrillandBeggs,
}


# ===========================
# Critical Property Correlations
# ===========================

CRITICAL_CORRELATIONS = {
    "Standing": critical.Standing,
    "Katz": critical.Katz,
    "Sutton": critical.Sutton,
}


# ===========================
# Critical Property Corrections
# ===========================

CRITICAL_CORRECTIONS = {
    "Wichert Aziz": critical.WichertAziz,
    "Carr Kobayashi Burrows": critical.CarrKobayashiBurrows,
}

