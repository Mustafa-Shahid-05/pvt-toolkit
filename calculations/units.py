# ==========================
# PRESSURE (base = Pa)
# ==========================

PRESSURE = {
    "Pa": 1,
    "kPa": 1e3,
    "MPa": 1e6,
    "bar": 1e5,
    "atm": 101325,
    "psia": 6894.757293,
}


def convert_pressure(value, from_unit, to_unit):
    return value * PRESSURE[from_unit] / PRESSURE[to_unit]


# ==========================
# DENSITY (base = kg/m³)
# ==========================

DENSITY = {
    "kg/m³": 1,
    "g/cm³": 1000,
    "lb/ft³": 16.018463,
}


def convert_density(value, from_unit, to_unit):
    return value * DENSITY[from_unit] / DENSITY[to_unit]

# ==========================
# MOLAR MASS (base = kg/kmol)
# ==========================

MOLAR_MASS = {
    "kg/kmol":1,
    "g/mol":1,
    "lbm/lbmol":1,
    "kg/mol":1e3,
    "g/kmol":1e3,
    "lbm/mol":2.204622621848776,
    "lbm/kmol":2.204622621848776e-3,
}

def convert_molar_mass (value , from_unit,to_unit):
    return value * MOLAR_MASS[from_unit]/MOLAR_MASS[to_unit]


# ==========================
# VOLUME (base = m³)
# ==========================

VOLUME = {
    "m³": 1,
    "L": 0.001,
    "ft³": 0.0283168466,
    "bbl": 0.158987295,
    "rb": 0.158987295,
}


def convert_volume(value, from_unit, to_unit):
    return value * VOLUME[from_unit] / VOLUME[to_unit]


# ==========================
# GAS VOLUME (base = Sm³)
# ==========================

GAS_VOLUME = {
    "Sm³": 1,
    "scf": 0.0283168466,
    "Mscf": 28.3168466,
    "MMscf": 28316.8466,
}


def convert_gas_volume(value, from_unit, to_unit):
    return value * GAS_VOLUME[from_unit] / GAS_VOLUME[to_unit]


# ==========================
# VISCOSITY (base = Pa.s)
# ==========================

VISCOSITY = {
    "Pa.s": 1,
    "mPa.s": 1e-3,
    "cP": 1e-3,
}


def convert_viscosity(value, from_unit, to_unit):
    return value * VISCOSITY[from_unit] / VISCOSITY[to_unit]


# ==========================
# COMPRESSIBILITY (base = 1/Pa)
# ==========================

COMPRESSIBILITY = {
    "1/Pa": 1,
    "1/kPa": 1e-3,
    "1/MPa": 1e-6,
    "1/bar": 1e-5,
    "1/psi": 1 / 6894.757293,
}


def convert_compressibility(value, from_unit, to_unit):
    return value * COMPRESSIBILITY[from_unit] / COMPRESSIBILITY[to_unit]


# ==========================
# PERMEABILITY (base = Darcy)
# ==========================

PERMEABILITY = {
    "D": 1,
    "mD": 1e-3,
}


def convert_permeability(value, from_unit, to_unit):
    return value * PERMEABILITY[from_unit] / PERMEABILITY[to_unit]


# ==========================
# LENGTH (base = m)
# ==========================

LENGTH = {
    "m": 1,
    "cm": 0.01,
    "mm": 0.001,
    "ft": 0.3048,
    "in": 0.0254,
}


def convert_length(value, from_unit, to_unit):
    return value * LENGTH[from_unit] / LENGTH[to_unit]


# ==========================
# AREA (base = m²)
# ==========================

AREA = {
    "m²": 1,
    "ft²": 0.09290304,
    "acre": 4046.8564224,
}


def convert_area(value, from_unit, to_unit):
    return value * AREA[from_unit] / AREA[to_unit]


# ==========================
# FLOW RATE (base = m³/day)
# ==========================

FLOWRATE = {
    "m³/day": 1,
    "bbl/day": 0.158987295,
    "STB/day": 0.158987295,
}


def convert_flowrate(value, from_unit, to_unit):
    return value * FLOWRATE[from_unit] / FLOWRATE[to_unit]

# ==========================
# TEMPERATURE
# ==========================

def convert_temperature(value, from_unit, to_unit):

    # Convert to Kelvin
    if from_unit == "K":
        value = value
    elif from_unit == "°C":
        value += 273.15
    elif from_unit == "°F":
        value = (value - 32) * 5 / 9 + 273.15
    elif from_unit == "°R":
        value *= 5 / 9
    else:
        raise ValueError(f"Unsupported temperature unit: {from_unit}")

    # Convert from Kelvin
    if to_unit == "K":
        return value
    elif to_unit == "°C":
        return value - 273.15
    elif to_unit == "°F":
        return (value - 273.15) * 9 / 5 + 32
    elif to_unit == "°R":
        return value * 9 / 5

    raise ValueError(f"Unsupported temperature unit: {to_unit}")

# ==========================
# API ↔ Specific Gravity
# ==========================

def api_to_specific_gravity(api):
    return 141.5 / (api + 131.5)


def specific_gravity_to_api(sg):
    return 141.5 / sg - 131.5