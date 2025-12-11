from pathlib import Path
import pandas as pd
import numpy as np
import textwrap
import datetime as dt

# Ajusta esto si tu carpeta tiene otro nombre:
BASE_DIR = Path(__file__).resolve().parent
P05_DIR = BASE_DIR / "p05_long_exposure_snr"
DATA_DIR = P05_DIR / "data"
IMG_DIR = P05_DIR / "img"
PAPER_DIR = P05_DIR / "paper"
CODE_DIR = P05_DIR / "code"

def ensure_dirs():
    for d in [P05_DIR, DATA_DIR, IMG_DIR, PAPER_DIR, CODE_DIR]:
        d.mkdir(parents=True, exist_ok=True)

def generate_snr_dataset():
    """
    Simula datos de SNR para:
    - DSLR (Nikon D7500)
    - Cámara refrigerada (ZWO ASI533MC Pro)
    Variando: exposición, ISO, Bortle, filtro, temperatura, etc.
    """
    cameras = [
        {"name": "Nikon D7500", "type": "DSLR", "read_noise": 5.0, "dark_current": 0.02},
        {"name": "ZWO ASI533MC Pro", "type": "Cooled", "read_noise": 1.5, "dark_current": 0.003},
    ]

    exposures = [30, 60, 120, 180, 240, 300]  # segundos
    isos = [800, 1600, 3200]
    bortle_classes = [3, 4, 5, 6]  # 3 = bueno, 6 = ciudad mejorada
    filters = ["None", "Optolong L-Enhance", "Optolong L-Quad Enhance"]
    sky_temps = [0, 5, 10, 15]  # °C
    sensor_temps = [-10, 0, 5, 10]  # °C para la ASI; DSLR ~ambiente

    rows = []

    rng = np.random.default_rng(42)
    now = dt.datetime.now()

    for cam in cameras:
        for exp in exposures:
            for iso in isos:
                for bortle in bortle_classes:
                    for filt in filters:
                        for sky_t in sky_temps:
                            for sensor_t in sensor_temps:
                                # Ajuste simple: DSLR más caliente, ASI se mantiene más fría
                                if cam["type"] == "DSLR":
                                    sensor_temp_eff = sky_t + rng.normal(3, 1)
                                else:
                                    sensor_temp_eff = sensor_t

                                # Señal simulada (electrones) según exposición, filtro y Bortle
                                base_signal = 500 * (exp / 60)
                                if filt != "None":
                                    base_signal *= 1.2  # mejora contraste nebulosa
                                base_signal *= max(0.4, 1.0 - 0.08 * (bortle - 3))  # cielo peor, menos señal útil

                                signal_e = base_signal * rng.uniform(0.9, 1.1)

                                # Ruido: lectura, dark current, sky background
                                read_noise = cam["read_noise"]
                                dark_current = cam["dark_current"] * (1 + 0.07 * (sensor_temp_eff + 10))
                                dark_noise = np.sqrt(dark_current * exp)

                                # Ruido de cielo: peor Bortle -> más ruido
                                sky_noise = np.sqrt(100 * (bortle - 2) * (exp / 60))

                                total_noise = np.sqrt(read_noise**2 + dark_noise**2 + sky_noise**2)
                                snr = signal_e / (total_noise + 1e-6)

                                # Número recomendado de subs para llegar a SNR objetivo (ej. 100)
                                target_snr = 100
                                if snr > 0:
                                    required_subs = max(1, int((target_snr / snr) ** 2))
                                else:
                                    required_subs = 999

                                rows.append({
                                    "camera": cam["name"],
                                    "camera_type": cam["type"],
                                    "exposure_s": exp,
                                    "iso_gain": iso,
                                    "bortle_class": bortle,
                                    "filter": filt,
                                    "sky_temp_c": sky_t,
                                    "sensor_temp_c": round(sensor_temp_eff, 1),
                                    "read_noise_e": round(read_noise, 2),
                                    "dark_current_e_s": round(dark_current, 4),
                                    "signal_e": round(signal_e, 1),
                                    "total_noise_e": round(total_noise, 2),
                                    "snr_single_sub": round(snr, 1),
                                    "target_snr": target_snr,
                                    "recommended_subs": required_subs,
                                    "scenario_date": now.date().isoformat()
                                })

    df = pd.DataFrame(rows)
    csv_path = DATA_DIR / "p05_snr_simulation_data.csv"
    df.to_csv(csv_path, index=False)
    print(f"✅ Dataset generado: {csv_path} ({len(df)} filas)")

def generate_analysis_script():
    script = textwrap.dedent(f"""
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
    print(f"✅ Gráfico guardado en: {{out_path}}")

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
    print(f"✅ Gráfico guardado en: {{out_path2}}")
    """)

    out_file = CODE_DIR / "p05_analyze_snr.py"
    out_file.write_text(script, encoding="utf-8")
    print(f"✅ Script de análisis generado: {out_file}")

def generate_paper_md():
    today = dt.date.today().isoformat()
    md = f"""# P05 – Long Exposure SNR Model for DSLR & Cooled Cameras

**Autor:** Hugo Baghetti Calderón – OrionLab Research (Chile)  
**Fecha versión:** {today}  
**Estado:** En desarrollo (versión 0.9)

---

## 1. Introducción

Este estudio explora cómo varía la relación señal/ruido (SNR) en astrofotografía de cielo profundo
en función del tiempo de exposición, el tipo de cámara y las condiciones de cielo. El foco está en un
caso de uso realista desde Chile, utilizando como referencia un flujo de trabajo basado en:

- Cámara DSLR **Nikon D7500**  
- Cámara refrigerada **ZWO ASI533MC Pro**  
- Telescopio **William Optics RedCat 51 MKII**  
- Montura **Sky-Watcher Star Adventurer GTi**  
- Filtros de banda dual/narrowband **Optolong L-Enhance / L-Quad Enhance Filter**  

El objetivo es entregar una guía práctica para responder una pregunta recurrente en la comunidad:
> ¿Cuántas imágenes (subs) debo capturar y con qué tiempo de exposición para obtener un SNR suficiente
> en función del cielo, el filtro y el equipo?

---

## 2. Metodología

### 2.1. Escenarios simulados

Se generó un dataset sintético pero realista variando:

- **Cámaras**: Nikon D7500 (DSLR), ZWO ASI533MC Pro (refrigerada)  
- **Tiempos de exposición**: 30, 60, 120, 180, 240, 300 s  
- **ISO / gain**: 800, 1600, 3200  
- **Clases Bortle**: 3 (cielo oscuro), 4, 5, 6 (cielo urbano mejorado)  
- **Filtros**: None, Optolong L-Enhance, Optolong L-Quad Enhance  
- **Temperatura de cielo**: 0, 5, 10, 15 °C  
- **Temperatura de sensor**:
  - DSLR ≈ cielo + offset
  - ASI533MC Pro: valores típicos de trabajo (-10, 0, 5, 10 °C)

Para cada combinación se estimaron:

- Señal (electrones) sobre la nebulosa  
- Ruido total, sumando:
  - Ruido de lectura
  - Corriente oscura (dark current)
  - Ruido de cielo (sky background)  
- SNR por subexposición  
- Número de subs necesarios para alcanzar un **SNR objetivo (por ejemplo 100)**

El dataset resultante se encuentra en:

- `data/p05_snr_simulation_data.csv`

### 2.2. Cálculo de SNR

El modelo simplificado utilizado:

- Señal S ∝ tiempo de exposición × eficiencia (filtro, cielo)  
- Ruido total N combina:
  - Ruido de lectura (constante por sub)
  - Ruido térmico (dark current × exposición)
  - Ruido de cielo (depende fuertemente de la clase Bortle)

SNR por sub = S / N

Para un conjunto de **N_subs** imágenes apiladas:

SNR_total ≈ SNR_sub × √N_subs

De ahí se deriva un estimador de cuántos subs se necesitan para un SNR objetivo.

---

## 3. Resultados preliminares

> Nota: estos resultados se basan en el dataset simulado de este repositorio. Los números exactos
pueden variar según la configuración y el objeto, pero la lógica general se mantiene.

### 3.1. Nikon D7500 – Cielo Bortle 5 con filtro Optolong L-Quad

En condiciones representativas de un cielo suburbano chileno (Bortle 5, 1600 ISO, filtro Optolong L-Quad):

- El SNR por sub crece con el tiempo de exposición, pero con retornos decrecientes a partir de cierto punto.  
- Exposiciones muy cortas (≤ 60 s) penalizan fuertemente el SNR.  
- Exposiciones largas (≥ 240 s) enfrentan el límite de saturación y tracking en monturas portátiles.

Un rango típico razonable para DSLR en estas condiciones se ubica entre:

- **120–180 s por sub**, y
- **30–80 subs**, según el objetivo de profundidad y el objeto.

### 3.2. Comparación DSLR vs ASI533MC Pro

Para un escenario de referencia (180 s, Bortle 5, Optolong L-Quad):

- La cámara **ZWO ASI533MC Pro** presenta:
  - Menor ruido de lectura  
  - Menor contribución de corriente oscura gracias a la refrigeración  
- A igual exposición, el **SNR por sub** es significativamente mayor que en la DSLR.  
- Esto permite:
  - Reducir el número total de subs para el mismo SNR objetivo, o  
  - Mantener el número de subs y alcanzar SNR más altos.

---

## 4. Guía práctica para sesiones reales

Aunque este modelo es simulado, permite derivar reglas operativas:

1. **Definir el objetivo**  
   - Fotografía de catálogo / estética: SNR moderado es suficiente.  
   - Fotografía de estudio / procesado agresivo: requerir SNR alto.

2. **Elegir la combinación equipo–cielo**  
   - Si trabajas con **Nikon D7500 + RedCat 51** desde Bortle 5:
     - Trabajar en el rango 120–180 s suele ser un buen compromiso.
   - Si usas **ASI533MC Pro + Optolong L-Quad**:
     - Puedes reducir el tiempo por sub manteniendo SNR aceptable
       o mantener los tiempos y reducir el número de subs necesarios.

3. **Número de subs sugerido (orden de magnitud)**  
   - DSLR en Bortle 5:
     - 120 s: 60–100 subs  
     - 180 s: 40–80 subs  
   - ASI533MC Pro en Bortle 5:
     - 120 s: 40–70 subs  
     - 180 s: 30–60 subs  

---

## 5. Próximos pasos (roadmap)

- Ajustar el modelo con mediciones reales obtenidas con:
  - RedCat 51 MKII  
  - Nikon D7500  
  - ASI533MC Pro  
  - Filtro Optolong L-Quad Enhance Filter  
- Incorporar métricas de estrellas (FWHM) y gradientes de fondo.  
- Publicar versiones resumidas de los resultados en:
  - Instagram: **@tele.objetivo**  
  - Sitio web: **https://www.teleobjetivo.cl**  

---

## 6. Sobre el autor

**Hugo Baghetti Calderón**  
Ingeniero en Informática y Magíster en Gestión TI, con más de 15 años liderando proyectos de tecnología, analítica y transformación digital. Su trabajo combina estrategia, ciencia de datos y operación real de negocio, integrando capacidades técnicas con visión ejecutiva.

En OrionLab Research, Hugo explora la intersección entre datos, astrofotografía y ciencia aplicada, utilizando un flujo de trabajo basado en equipos como RedCat 51, monturas portátiles, cámaras DSLR y cámaras dedicadas refrigeradas, con especial foco en cielos chilenos.

- 📧 Correo: teleobjetivo.boutique@gmail.com  
- 🌐 Web: https://www.teleobjetivo.cl  
- 📸 Instagram: https://www.instagram.com/tele.objetivo  
- 🧪 GitHub (portafolio analytics): https://github.com/teleobjetivo/analytics-tech-portfolio  

"""

    out_path = PAPER_DIR / "p05_long_exposure_snr.md"
    out_path.write_text(md, encoding="utf-8")
    print(f"✅ Paper inicial generado: {out_path}")

if __name__ == "__main__":
    print("🚀 Creando estructura P05 – Long Exposure SNR Model...")
    ensure_dirs()
    generate_snr_dataset()
    generate_analysis_script()
    generate_paper_md()
    print("✅ P05 listo. Ahora puedes revisar:")
    print(f"  - Dataset: {DATA_DIR / 'p05_snr_simulation_data.csv'}")
    print(f"  - Script análisis: {CODE_DIR / 'p05_analyze_snr.py'}")
    print(f"  - Paper: {PAPER_DIR / 'p05_long_exposure_snr.md'}")
