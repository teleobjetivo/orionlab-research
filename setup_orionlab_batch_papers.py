"""
setup_orionlab_batch_papers.py

Genera contenido base (README, paper .md y un CSV simple) para los estudios
P08–P20 del repositorio OrionLab_Research.

Uso:
    python setup_orionlab_batch_papers.py

Debe ejecutarse desde la raíz del repo OrionLab_Research.
"""

from pathlib import Path
import textwrap
import csv
import random
from datetime import date

ROOT = Path(__file__).resolve().parent

PROJECTS = [
    ("p08_photometry_open_clusters", "Simple Photometry of Southern Open Clusters"),
    ("p09_light_pollution_las_condes", "Light Pollution Impact in Las Condes"),
    ("p10_python_reduction_pipeline", "Python Reduction Pipeline for OSC Cameras"),
    ("p11_gradient_detection_lp", "Gradient Detection of Light Pollution"),
    ("p12_planning_sessions_chile", "Planning Astro Sessions in Chile by Region"),
    ("p13_star_colour_variation", "Star Colour Variation in Broadband Imaging"),
    ("p14_stacking_algorithms_osc", "Comparing Stacking Algorithms for OSC Cameras"),
    ("p15_dithering_impact_noise", "Dithering Impact on Thermal Noise"),
    ("p16_starlink_trail_stats", "Starlink Trails Statistics from Santiago"),
    ("p17_snr_model_multiband", "SNR Model with Multiband Filters in Bright Skies"),
    ("p18_messier_ngc_from_chile", "Messier & NGC Visibility from Chile"),
    ("p19_wavelets_nebulae_detail", "Wavelets for Enhancing Nebula Detail"),
    ("p20_asi533_thermal_noise_model", "Thermal Noise Model for ASI533MC Pro"),
]

TODAY = date.today().isoformat()

ABOUT_AUTHOR = textwrap.dedent("""\
    **Author – Hugo Baghetti Calderón (Chile)**  
    Independent researcher in data, neurotech and astrophotography.  
    - M.Sc. in IT Management, Computer Engineer  
    - Specialised in data architectures, analytics and astro imaging from Chile  
    - Instagram: [@tele.objetivo](https://www.instagram.com/tele.objetivo)  
    - Web: [www.teleobjetivo.cl](https://www.teleobjetivo.cl)  
    - GitHub: [teleobjetivo](https://github.com/teleobjetivo)
""")


def ensure_dirs(project_root: Path):
    (project_root / "data").mkdir(parents=True, exist_ok=True)
    (project_root / "paper").mkdir(parents=True, exist_ok=True)
    (project_root / "notebooks").mkdir(parents=True, exist_ok=True)


def write_csv(project_id: str, project_root: Path):
    """Genera un CSV muy simple pero verosímil según el tipo de estudio."""
    data_dir = project_root / "data"

    if project_id == "p08_photometry_open_clusters":
        path = data_dir / "photometry_open_clusters.csv"
        rows = []
        for cluster in ["NGC 4755", "NGC 2516", "IC 2602", "NGC 3532"]:
            for star_id in range(1, 31):
                rows.append({
                    "cluster": cluster,
                    "star_id": star_id,
                    "mag_V": round(random.uniform(8, 16), 3),
                    "mag_B": round(random.uniform(8.2, 16.5), 3),
                    "snr": round(random.uniform(15, 150), 1),
                    "fwhm_pix": round(random.uniform(1.8, 4.5), 2),
                })
        fieldnames = ["cluster", "star_id", "mag_V", "mag_B", "snr", "fwhm_pix"]

    elif project_id == "p09_light_pollution_las_condes":
        path = data_dir / "light_pollution_las_condes.csv"
        rows = []
        for month in range(1, 13):
            for bortle in [7, 8]:
                rows.append({
                    "month": month,
                    "bortle": bortle,
                    "sky_brightness_mag_arcsec2": round(random.uniform(17.5, 19.0), 2),
                    "cloud_cover_pct": random.choice([5, 10, 20, 30, 40]),
                    "moon_phase_pct": random.choice([0, 25, 50, 75, 100]),
                })
        fieldnames = ["month", "bortle", "sky_brightness_mag_arcsec2",
                      "cloud_cover_pct", "moon_phase_pct"]

    elif project_id == "p10_python_reduction_pipeline":
        path = data_dir / "reduction_pipeline_stages.csv"
        stages = ["bias_sub", "dark_sub", "flat_field", "register", "stack"]
        rows = []
        for i, stage in enumerate(stages, start=1):
            rows.append({
                "order": i,
                "stage": stage,
                "time_seconds": random.randint(10, 600),
                "median_snr": round(random.uniform(20, 120), 1),
                "frames_processed": random.randint(20, 200),
            })
        fieldnames = ["order", "stage", "time_seconds", "median_snr",
                      "frames_processed"]

    elif project_id == "p11_gradient_detection_lp":
        path = data_dir / "gradient_profiles.csv"
        rows = []
        for angle_deg in [0, 45, 90, 135]:
            for radius_pix in range(100, 1000, 100):
                rows.append({
                    "angle_deg": angle_deg,
                    "radius_pix": radius_pix,
                    "background_ADU": round(random.uniform(800, 5000), 1),
                })
        fieldnames = ["angle_deg", "radius_pix", "background_ADU"]

    elif project_id == "p12_planning_sessions_chile":
        path = data_dir / "planning_sessions_chile.csv"
        rows = []
        regions = ["RM", "IV", "II", "IX", "X"]
        for region in regions:
            for season in ["summer", "winter"]:
                rows.append({
                    "region": region,
                    "season": season,
                    "median_bortle": random.choice([2, 3, 4, 5, 6]),
                    "clear_nights_per_month": random.randint(5, 20),
                    "altitude_m": random.choice([300, 800, 1500, 2500, 4000]),
                })
        fieldnames = ["region", "season", "median_bortle",
                      "clear_nights_per_month", "altitude_m"]

    elif project_id == "p13_star_colour_variation":
        path = data_dir / "star_colour_variation.csv"
        rows = []
        for star in range(1, 101):
            rows.append({
                "star_id": star,
                "b_minus_v": round(random.uniform(-0.2, 1.8), 3),
                "g_minus_r": round(random.uniform(-0.1, 1.5), 3),
                "snr": round(random.uniform(20, 200), 1),
            })
        fieldnames = ["star_id", "b_minus_v", "g_minus_r", "snr"]

    elif project_id == "p14_stacking_algorithms_osc":
        path = data_dir / "stacking_algorithms_osc.csv"
        algos = ["mean", "median", "sigma_clip", "winsorized"]
        rows = []
        for algo in algos:
            for subs in [10, 20, 40, 80, 120]:
                rows.append({
                    "algo": algo,
                    "n_subs": subs,
                    "snr_result": round(random.uniform(25, 250), 1),
                    "background_noise_adu": round(random.uniform(5, 40), 2),
                })
        fieldnames = ["algo", "n_subs", "snr_result", "background_noise_adu"]

    elif project_id == "p15_dithering_impact_noise":
        path = data_dir / "dithering_impact_noise.csv"
        rows = []
        for pattern in ["none", "small", "medium", "large"]:
            for subs in [20, 40, 80, 120]:
                rows.append({
                    "pattern": pattern,
                    "n_subs": subs,
                    "noise_rms_adu": round(random.uniform(12, 40), 2),
                    "residual_band_noise": round(random.uniform(0.5, 3.0), 2),
                })
        fieldnames = ["pattern", "n_subs", "noise_rms_adu",
                      "residual_band_noise"]

    elif project_id == "p16_starlink_trail_stats":
        path = data_dir / "starlink_trails_stats.csv"
        rows = []
        for night in range(1, 31):
            rows.append({
                "night_index": night,
                "trails_detected": random.randint(0, 25),
                "total_exposure_min": random.randint(30, 300),
                "filter": random.choice(["L", "RGB", "Halpha", "OIII"]),
            })
        fieldnames = ["night_index", "trails_detected",
                      "total_exposure_min", "filter"]

    elif project_id == "p17_snr_model_multiband":
        path = data_dir / "snr_multiband_model.csv"
        rows = []
        for filt in ["L", "R", "G", "B", "Ha", "OIII", "SII"]:
            for bortle in [3, 4, 5, 6, 7]:
                rows.append({
                    "filter": filt,
                    "bortle": bortle,
                    "exposure_s": random.choice([60, 120, 180, 300]),
                    "snr_model": round(random.uniform(10, 200), 1),
                })
        fieldnames = ["filter", "bortle", "exposure_s", "snr_model"]

    elif project_id == "p18_messier_ngc_from_chile":
        path = data_dir / "messier_ngc_visibility_chile.csv"
        rows = []
        objects = ["M8", "M20", "M42", "M83", "NGC253", "NGC3372"]
        for obj in objects:
            for month in range(1, 13):
                rows.append({
                    "object": obj,
                    "month": month,
                    "max_altitude_deg": round(random.uniform(20, 85), 1),
                    "best_hour_local": random.choice([21, 22, 23, 0, 1, 2, 3]),
                })
        fieldnames = ["object", "month", "max_altitude_deg", "best_hour_local"]

    elif project_id == "p19_wavelets_nebulae_detail":
        path = data_dir / "wavelets_nebulae_detail.csv"
        rows = []
        layers = [1, 2, 3, 4, 5]
        for layer in layers:
            rows.append({
                "wavelet_layer": layer,
                "detail_gain_pct": random.randint(0, 80),
                "noise_amplification_pct": random.randint(0, 60),
            })
        fieldnames = ["wavelet_layer", "detail_gain_pct",
                      "noise_amplification_pct"]

    elif project_id == "p20_asi533_thermal_noise_model":
        path = data_dir / "asi533_thermal_noise_model.csv"
        rows = []
        temps = [-10, -5, 0, 5]
        exposures = [60, 120, 180, 300]
        for t in temps:
            for exp in exposures:
                rows.append({
                    "sensor_temp_c": t,
                    "exposure_s": exp,
                    "dark_current_e_s": round(random.uniform(0.01, 0.3), 3),
                    "read_noise_e": round(random.uniform(1.0, 2.5), 2),
                })
        fieldnames = ["sensor_temp_c", "exposure_s",
                      "dark_current_e_s", "read_noise_e"]

    else:
        # Fallback genérico
        path = data_dir / f"{project_id}_data.csv"
        rows = [{"x": i, "y": random.random()} for i in range(50)]
        fieldnames = ["x", "y"]

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_readme(project_id: str, title: str, project_root: Path):
    readme = project_root / "README.md"

    scope_tag = "Astrofotografía cuantitativa"
    if project_id.startswith("p0") and "eeg" in project_id:
        scope_tag = "Neurociencia de datos / EEG"

    content = textwrap.dedent(f"""\
    # {title}

    Proyecto de investigación independiente del repositorio **OrionLab Research**.
    Este estudio combina captura real en terreno con simulación y análisis reproducible.

    - **ID del estudio:** {project_id.upper()}
    - **Alcance:** {scope_tag}
    - **Estado:** En desarrollo (versión 0.1, {TODAY})
    - **Ubicación:** Observaciones y simulaciones basadas en cielos de Chile (Santiago, norte y sur).

    ## Objetivo general

    Explorar y cuantificar fenómenos relevantes para astrofotografía y ciencia ciudadana,
    utilizando un enfoque reproducible con datos tabulares (`data/`) y un paper técnico en `paper/`.

    ## Estructura del estudio

    - `data/` – Datos sintéticos o resumidos para reproducir análisis y gráficos.
    - `paper/` – Manuscrito en formato markdown listo para ser versionado.
    - `notebooks/` – Espacio reservado para cuadernos Jupyter con análisis adicionales.

    {ABOUT_AUTHOR}
    """)

    readme.write_text(content, encoding="utf-8")


def write_paper_md(project_id: str, title: str, project_root: Path):
    paper_dir = project_root / "paper"
    paper_dir.mkdir(parents=True, exist_ok=True)
    paper_md = paper_dir / f"{project_id}_paper.md"

    abstract = "This document describes a small, reproducible study using synthetic yet realistic data."
    if "light_pollution" in project_id:
        abstract = ("We present a compact empirical exploration of light pollution levels and their impact "
                    "on deep sky imaging from urban skies in Chile, using simplified yet realistic metrics.")
    elif "photometry" in project_id:
        abstract = ("We explore basic aperture photometry of southern open clusters using a synthetic dataset "
                    "designed to replicate typical noise, seeing and SNR conditions for DSLR / OSC cameras.")
    elif "asi533" in project_id or "thermal_noise" in project_id:
        abstract = ("We model the thermal noise behaviour of the ZWO ASI533MC Pro camera under different "
                    "cooling temperatures and exposure times, illustrating how dark current and read noise combine.")
    elif "stacking" in project_id or "dithering" in project_id:
        abstract = ("We compare stacking strategies and dithering patterns for one-shot colour cameras, showing "
                    "their impact on SNR, background noise and residual patterns under bright skies.")
    elif "starlink" in project_id:
        abstract = ("We provide a small observational-style dataset on Starlink satellite trails as recorded "
                    "from Santiago, Chile, offering simple statistics for teaching and exploration.")

    content = textwrap.dedent(f"""\
    # {title}

    **Short Title:** {title}  
    **Project ID:** {project_id.upper()}  
    **Author:** Hugo Baghetti Calderón (OrionLab, Chile)  
    **Version:** 0.1 – {TODAY}

    ---

    ## Abstract

    {abstract}

    ## 1. Introduction

    This study is part of the **OrionLab Research** series, focused on the intersection between
    astrophotography, quantitative analysis and reproducible workflows.

    The goal of this manuscript is not to replace peer-reviewed work, but to provide a compact,
    transparent and **teachable** example of how data, models and observation planning can be combined
    using simple Python tooling.

    ## 2. Data and Methods

    - Synthetic or semi-synthetic data stored in `data/`
    - CSV structure documented directly in the repository
    - Intended for exploration via Jupyter notebooks or lightweight scripts
    - Designed to be small enough for classroom or workshop use

    ### 2.1 Instruments and context

    This project is conceptually aligned with a typical astro-imaging kit operated from Chile:

    - William Optics **RedCat 51** (o refractores cortos equivalentes)
    - Cámara ZWO **ASI533MC Pro** o DSLR Nikon
    - Montura **Sky-Watcher Star Adventurer GTi**
    - Filtro **Optolong L-Quad Enhance** u otros filtros de banda ancha/estrecha
    - Control y automatización vía **ASIAIR** u ordenadores ligeros

    These references are deliberately kept generic so that the study can be adapted to other setups.

    ## 3. Results (placeholder)

    At this stage, results are intentionally minimal. The CSV file in `data/` can be used to:

    - Recreate simple plots (distributions, correlations, trend lines)
    - Prototype simple models (SNR vs exposure, gradients, thermal noise, etc.)
    - Demonstrate good practices in documentation and versioning

    Future versions of this manuscript will incorporate:

    - Concrete figures generated from real sessions
    - Cross-comparisons between locations in Chile
    - More detailed model validation and error analysis

    ## 4. Discussion and Future Work

    This study is versioned as **0.1** to emphasise that it is a living document.
    The intent is to:

    - Provide a solid starting point for students and collaborators
    - Document design decisions early (filters, instruments, sky models)
    - Enable later integration with real-world datasets and observatory APIs

    Planned future extensions include:

    - Incorporating real sessions from @tele.objetivo on Instagram
    - Referencing public observatory data sets when available
    - Comparing results across Bortle classes within Chile

    ## 5. References (seed list)

    - Selected manufacturer documentation for William Optics, ZWO, Optolong, Sky-Watcher.
    - Public resources from professional observatories in Chile (ALMA, ESO, etc.).
    - Classic references on signal-to-noise modelling in CCD/CMOS imaging.

    ---

    {ABOUT_AUTHOR}

    """)

    paper_md.write_text(content, encoding="utf-8")


def main():
    for project_id, title in PROJECTS:
        project_root = ROOT / project_id
        ensure_dirs(project_root)
        write_csv(project_id, project_root)
        write_readme(project_id, title, project_root)
        write_paper_md(project_id, title, project_root)
        print(f"[OK] Scaffolded {project_id} – {title}")

    print("\nDone. P08–P20 now have README, CSV and paper skeletons.")


if __name__ == "__main__":
    main()
