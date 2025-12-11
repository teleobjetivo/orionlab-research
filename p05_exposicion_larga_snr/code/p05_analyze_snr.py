
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1] / "p05_long_exposure_snr"
DATA_DIR = BASE_DIR / "data"
IMG_DIR = BASE_DIR / "img"

df = pd.read_csv(DATA_DIR / "p05_snr_simulation_data.csv")

# Ejemplo 1: curva SNR vs tiempo de exposición para Nikon D7500, Bortle 5
subset_dslr = df[
    (df["camera"] == "Nikon D7500") &
    (df["bortle_class"] == 5) &
    (df["filter"] == "Optolong L-Quad Enhance") &
    (df["iso_gain"] == 1600)
]

subset_dslr = subset_dslr.sort_values("exposure_s")

plt.figure()
plt.plot(subset_dslr["exposure_s"], subset_dslr["snr_single_sub"], marker="o")
plt.xlabel("Tiempo de exposición (s)")
plt.ylabel("SNR por sub")
plt.title("P05 – SNR vs Exposición (Nikon D7500, Bortle 5, Optolong L-Quad)")
plt.grid(True)
IMG_DIR.mkdir(parents=True, exist_ok=True)
out_path = IMG_DIR / "p05_snr_vs_exposure_dslr.png"
plt.savefig(out_path, bbox_inches="tight")
plt.close()
print(f"✅ Gráfico guardado en: {out_path}")

# Ejemplo 2: comparación DSLR vs ASI533MC Pro a 180 s, Bortle 5
subset_180 = df[
    (df["exposure_s"] == 180) &
    (df["bortle_class"] == 5) &
    (df["filter"] == "Optolong L-Quad Enhance") &
    (df["iso_gain"] == 1600)
]

plt.figure()
plt.bar(subset_180["camera"], subset_180["snr_single_sub"])
plt.ylabel("SNR por sub")
plt.title("P05 – Comparación DSLR vs ASI533MC Pro (180s, Bortle 5, Optolong L-Quad)")
plt.xticks(rotation=15)
plt.grid(axis="y")
out_path2 = IMG_DIR / "p05_snr_dslr_vs_asi533.png"
plt.savefig(out_path2, bbox_inches="tight")
plt.close()
print(f"✅ Gráfico guardado en: {out_path2}")
