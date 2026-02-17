from materials import materials
from riser import design_riser
from gating import design_gating

def calculate_casting(data):

    L = data.length
    B = data.breadth
    H = data.height

    material_data = materials[data.material]
    shrinkage = material_data["shrinkage"]
    density = material_data["density"]

    # Apply shrinkage
    pattern_L = L * (1 + shrinkage)
    pattern_B = B * (1 + shrinkage)
    pattern_H = H * (1 + shrinkage)

    # Casting Volume (mm³)
    volume = L * B * H

    # Surface Area (mm²)
    surface_area = 2 * (L*B + B*H + L*H)

    # Modulus
    modulus = volume / surface_area

    # Weight (convert mm³ to m³)
    volume_m3 = volume * 1e-9
    weight = volume_m3 * density

    # Riser Design
    riser = design_riser(modulus)

    # Gating Design
    gating = design_gating(volume, weight)

    return {
        "pattern_dimensions_mm": {
            "length": round(pattern_L, 2),
            "breadth": round(pattern_B, 2),
            "height": round(pattern_H, 2)
        },
        "casting_volume_mm3": round(volume, 2),
        "casting_weight_kg": round(weight, 2),
        "casting_modulus_mm": round(modulus, 2),
        "riser": riser,
        "gating": gating
    }
