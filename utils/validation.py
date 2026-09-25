

def safe_float(value):
    """
    Convert user input to float.

    Returns:
        float if valid
        None if invalid or empty
    """

    if value is None:
        return None

    value = str(value).strip()

    if value == "":
        return None

    # Accept both comma and dot
    value = value.replace(",", ".")

    try:
        return float(value)
    except ValueError:
        return None