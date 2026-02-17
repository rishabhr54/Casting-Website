def design_riser(casting_modulus):
    """
    Designs cylindrical riser (H = D)
    Using modulus method.
    """

    D = 6 * casting_modulus
    H = D

    return {
        "riser_diameter_mm": round(D, 2),
        "riser_height_mm": round(H, 2)
    }
