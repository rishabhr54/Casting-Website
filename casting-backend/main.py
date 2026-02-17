from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from models import CastingInput
from calculations import calculate_casting
from cad_processing import process_stl
from materials import materials
from riser import design_riser
from gating import design_gating

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})




@app.post("/calculate")
def calculate(data: CastingInput):
    return calculate_casting(data)


@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    material: str = Form(...)
):

    content = await file.read()

    volume_mm3, surface_area_mm2 = process_stl(content)

    shrinkage = materials[material]["shrinkage"]

    volume_mm3 = volume_mm3 * (1 + shrinkage) ** 3
    surface_area_mm2 = surface_area_mm2 * (1 + shrinkage) ** 2

    modulus = volume_mm3 / surface_area_mm2

    density = materials[material]["density"]

    volume_m3 = volume_mm3 * 1e-9
    weight = volume_m3 * density

    riser = design_riser(modulus)
    gating = design_gating(volume_mm3, weight)

    return {
        "volume_mm3": round(volume_mm3, 2),
        "surface_area_mm2": round(surface_area_mm2, 2),
        "modulus_mm": round(modulus, 2),
        "weight_kg": round(weight, 2),
        "riser": riser,
        "gating": gating
    }
