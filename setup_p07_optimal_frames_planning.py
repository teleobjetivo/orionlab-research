from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Base paths
BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR / "p07_optimal_frames_planning"
DATA_DIR = PROJECT_DIR / "data"
IMG_DIR = PROJECT_DIR / "img"

for d in (PROJECT_DIR, DATA_DIR, IMG_DIR):
    d.mkdir(parents=True, exist_ok=True)

# Synthetic planning dataset
targets = [
    # name,           type,        hemisphere, bortle, filter,   tempC
    ("Orion Nebula",  "Nebulosa",  "Sur",      6,      "L-Quad", -5),
    ("Carina Nebula", "Nebulosa",  "Sur",      4,      "L-Quad", -10),
    ("Omega Centauri","Cúmulo",    "Sur",      5,      "UV/IR",  -5),
    ("Andromeda",     "Galaxia",   "Norte",    4,      "UV/IR",  -10),
    ("Rosette",       "Nebulosa",  "Sur",      5,      "L-Quad", -10),
    ("Lagoon",        "Nebulosa",  "Sur",      6,      "L-Quad", -5),
]

rows = []
for name, obj_type, hemi, bortle, filt, temp in targets:
    # Rule-of-thumb targets
    if obj_type == "Nebulosa":
        target_snr = 35
    elif obj_type == "Galaxia":
        target_snr = 30
    else:  # cúmulo
        target_snr = 25

    # Base exposure by sky quality (in seconds)
    if bortle <= 3:
        exposure = 120
    elif bortle <= 5:
        exposure = 180
    else:
        exposure = 240

    # Adjust exposure for filter
    if filt == "L-Quad":
        exposure *= 1.2  # narrowband-like, requiere algo más
    else:
        exposure *= 1.0

    # Normalize exposure to nice round values (30s steps)
    exposure = int(round(exposure / 30) * 30)

    # Lights based on SNR target & bortle (más contaminación = más lights)
    base_lights = 40
    lights = base_lights + max(0, (bortle - 4) * 10)

    # Adjust by object difficulty
    if obj_type == "Nebulosa":
        lights += 10
    elif obj_type == "Galaxia":
        lights += 5

    # Round to nearest 10
    lights = int(round(lights / 10) * 10)

    # Darks: ~20–30% de los lights
    darks = max(15, int(round(lights * 0.25 / 5) * 5))

    total_integration_min = lights * exposure / 60.0

    rows.append(
        {
            "objeto": name,
            "tipo_objeto": obj_type,
            "hemisferio": hemi,
            "bortle": bortle,
            "filtro": filt,
            "temp_sensor_C": temp,
            "snr_objetivo": target_snr,
            "exposicion_seg": exposure,
            "lights_recomendados": lights,
            "darks_recomendados": darks,
            "integracion_total_min": round(total_integration_min, 1),
        }
    )

df = pd.DataFrame(rows)
csv_path = DATA_DIR / "p07_planificacion_lights_darks.csv"
df.to_csv(csv_path, index=False)

# Simple plot: integración total vs bortle
fig, ax = plt.subplots(figsize=(8, 5))
for obj_type, sub in df.groupby("tipo_objeto"):
    ax.scatter(
        sub["bortle"],
        sub["integracion_total_min"],
        label=obj_type,
    )

ax.set_xlabel("Clase de cielo (Bortle)")
ax.set_ylabel("Integración total recomendada (min)")
ax.set_title("P07 – Integración total vs calidad de cielo")
ax.grid(True, alpha=0.3)
ax.legend()

img_path = IMG_DIR / "p07_integracion_vs_bortle.png"
fig.tight_layout()
fig.savefig(img_path, dpi=150)
plt.close(fig)

# Minimal README skeleton
readme_path = PROJECT_DIR / "README.md"
readme_content = """# P07 – Planificación de lights & darks según cielo y tipo de objeto

**Estado:** En desarrollo (versión 0.1)  
**Línea:** Ciencia & Astrofotografía – OrionLab Research

Este proyecto explora una regla práctica para estimar cuántas tomas de **luz (lights)** y **oscuridad (darks)** conviene capturar en una salida de astrofotografía de cielo profundo, en función de:

- Clase de cielo (escala de Bortle).
- Tipo de objeto (nebulosa, galaxia, cúmulo).
- Filtro utilizado (por ejemplo, Optolong L-Quad Enhance).
- Temperatura del sensor.
- Relación señal/ruido (SNR) objetivo.

El dataset de ejemplo está pensado para un setup realista como:

- **Telescopio:** William Optics RedCat 51
- **Cámara principal:** ZWO ASI533MC Pro
- **Filtro:** Optolong L-Quad Enhance
- **Montura:** Sky-Watcher Star Adventurer GTi
- **Control:** ZWO ASIAIR

La tabla `data/p07_planificacion_lights_darks.csv` resume los escenarios y la recomendación de:

- `exposicion_seg`
- `lights_recomendados`
- `darks_recomendados`
- `integracion_total_min`

El gráfico `img/p07_integracion_vs_bortle.png` muestra cómo la integración total recomendada crece al empeorar la clase de cielo (Bortle más alto), diferenciando por tipo de objeto.

En versiones futuras, este modelo podrá refinarse incorporando:

- Medidas reales de SNR por objeto.
- Dependencia explícita de la temperatura del sensor y la corriente oscura.
- Diferencias entre filtros de banda ancha y banda estrecha.
- Casuística específica para el hemisferio sur y catálogos (Messier / NGC) observados desde Chile.
"""

readme_path.write_text(readme_content, encoding="utf-8")

print("✅ P07 creado en:", PROJECT_DIR)
print("   - CSV:", csv_path)
print("   - Plot:", img_path)
print("   - README:", readme_path)
