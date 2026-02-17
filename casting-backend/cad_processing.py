import trimesh
import tempfile
import os

def process_stl(file):

    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".stl") as temp:
        temp.write(file)
        temp_path = temp.name

    mesh = trimesh.load(temp_path, force='mesh')

    if not mesh.is_watertight:
        mesh = mess.convex_hull

    volume_mm3 = mesh.volume
    surface_area_mm2 = mesh.area

    os.remove(temp_path)

    return volume_mm3, surface_area_mm2
