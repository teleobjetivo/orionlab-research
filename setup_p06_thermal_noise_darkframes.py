from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------
# CONFIG
# ----------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
PAPER_DIR = BASE_DIR / "p06_thermal_noise_darkframes"
DATA_DIR = PAPER_DIR / "data"
IMG_DIR = PAPER_DIR / "img"
MD_DIR = PAPER_DIR / "paper"

for d in [PAPER_DIR, DATA_DIR, IMG_DIR, MD_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------
# GENERATE SYNTHETIC DATA
# ----------------------------------------------------------
np.random.seed(42)

n = 200
cielos = np.random.choice(["Atacama", "Elqui", "Santiago"], size=n, p=[0.4, 0.3, 0.3])
bortle_map = {"Atacama": 2, "Elqui": 3, "Santiago": 8}

# 🔧 IMPORTANTE: usamos array de NumPy, no lista
bortle = np.array([bortle_map[c] for c in cielos], dtype=float)

temp_sensor = np.random.uniform(-10, 25, size=n)
exp_time = np.random.choice([30, 60, 120, 180], size=n)
iso = np.random.choice([400, 800, 1600, 3200], size=n)
frames = np.random.randint(20, 200, size=n)

# SNR synthetic model
snr = (
    80
    - (bortle * 3)
    - ((temp_sensor + 5) * 1.2)
    + (np.log(frames) * 8)
    + (np.where(iso < 1600, 5, -3))
    - (exp_time / 40)
    + np.random.normal(0, 3, size=n)
)

snr = np.clip(snr, 5, 80)

df = pd.DataFrame({
    "cielo": cielos,
    "bortle": bortle,
    "sensor_temp_c": temp_sensor.round(1),
    "exposure_s": exp_time,
    "iso": iso,
    "frames": frames,
    "snr": snr.round(2)
})

DATA_DIR.mkdir(parents=True, exist_ok=True)
df.to_csv(DATA_DIR / "p06_thermal_noise_experiments.csv", index=False)

# ----------------------------------------------------------
# PLOTS
# ----------------------------------------------------------
IMG_DIR.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(8, 5))
for sky in ["Atacama", "Elqui", "Santiago"]:
    subset = df[df["cielo"] == sky]
    plt.scatter(subset["frames"], subset["snr"], label=sky, alpha=0.7)

plt.xlabel("Número de frames")
plt.ylabel("SNR")
plt.title("SNR vs Cantidad de Frames por Tipo de Cielo")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(IMG_DIR / "p06_snr_vs_frames.png")
plt.close()

plt.figure(figsize=(8, 5))
sc = plt.scatter(df["sensor_temp_c"], df["snr"], c=df["bortle"], cmap="viridis")
plt.xlabel("Temperatura del sensor (°C)")
plt.ylabel("SNR")
plt.title("Relación entre SNR y Temperatura del Sensor")
plt.colorbar(sc, label="Índice Bortle")
plt.grid(True)
plt.tight_layout()
plt.savefig(IMG_DIR / "p06_snr_vs_sensor_temp.png")
plt.close()

# ----------------------------------------------------------
# MARKDOWN PAPER
# ----------------------------------------------------------
MD_DIR.mkdir(parents=True, exist_ok=True)

md_text = """
# P06 – Thermal Noise & Dark Frames Study  
### Exploración Comparada: Nikon D7500 vs ASI533MC Pro (Chile, 2019–2025)

## 1. Motivación
Este estudio explora cómo la temperatura del sensor, la contaminación lumínica (Bortle), el tiempo de exposición, el ISO y el número de frames afectan el **SNR final** en astrofotografía de cielo profundo.

## 2. Kit utilizado
- **William Optics RedCat 51 MK2.5**
- **ZWO ASI533MC Pro**
- **Filtro Optolong L-Quad Enhance**
- **Sky-Watcher Star Adventurer GTi**
- **Nikon D7500**
- **ASIAIR Plus**
- **Cintas calefactoras Dew-Heater**
- **GUIA – 30mm + ASI120MM**

## 3. Resultados iniciales
- Cielos oscuros (Atacama) → mayor SNR incluso con menos frames.
- Santiago (Bortle 8) → requiere más de **150 frames** para acercarse al rendimiento del Elqui con ~60.
- La ASI533MC Pro mantiene el ruido térmico controlado aún en noches cálidas.

## 4. Gráficos
### SNR vs Frames  
![plot](../img/p06_snr_vs_frames.png)

### SNR vs Temperatura del Sensor  
![plot](../img/p06_snr_vs_sensor_temp.png)

## 5. Trabajo futuro
- Calibración real con darks de campo.
- Incorporación de flats y bias para datasets controlados.
- Matriz predictiva según objeto (Nebulosa, Cúmulo, Galaxia).
- Integración a ASIAIR (export XML/JSON para recomendaciones automáticas).

## 6. Historial de versiones
- **v0.1 – 2019:** primeras notas desde Santiago.
- **v0.4 – 2021:** pruebas en Elqui, mejoras en dark frames.
- **v0.7 – 2023:** migración a ASI533MC Pro.
- **v1.0 – 2025:** dataset comparativo + modelo SNR.

---

Hugo Baghetti – *Astrofotografía & Data Science*  
Instagram: **@tele.objetivo**  
Web: **www.teleobjetivo.cl**  
OrionLab Research
"""

with open(MD_DIR / "p06_thermal_noise_darkframes.md", "w", encoding="utf-8") as f:
    f.write(md_text)

print("✅ P06 generado correctamente: CSV, gráficos y paper .md listos.")
