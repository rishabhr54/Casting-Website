import math

def design_gating(volume_mm3, weight_kg):
    """
    Designs unpressurized gating system (1:4:4)
    """

    # Convert volume to m³
    volume_m3 = volume_mm3 * 1e-9

    # Pouring time estimation
    pouring_time = 2.97 * math.sqrt(weight_kg)

    # Volumetric flow rate
    Q = volume_m3 / pouring_time   # m³/s

    # Assume sprue height = 0.15 m
    g = 9.81
    h = 0.15

    velocity = math.sqrt(2 * g * h)

    # Sprue area (m²)
    sprue_area = Q / velocity

    # Convert to mm²
    sprue_area_mm2 = sprue_area * 1e6

    # Gating ratio 1:4:4    
    runner_area_mm2 = 4 * sprue_area_mm2
    ingate_area_mm2 = 4 * sprue_area_mm2

    return {
        "pouring_time_sec": round(pouring_time, 2),
        "sprue_area_mm2": round(sprue_area_mm2, 2),
        "runner_area_mm2": round(runner_area_mm2, 2),
        "ingate_area_mm2": round(ingate_area_mm2, 2)
    }
