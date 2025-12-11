"""
Script de limpieza de nombres para OrionLab Research
----------------------------------------------------
Renombra carpetas pXX_* y los archivos .md principales de cada paper
a una convención profesional, sin tildes ni espacios.

Uso sugerido (desde la carpeta OrionLab_Research en tu Mac):

    python fix_orionlab_names.py

El script:
- Busca cada proyecto P01–P20.
- Detecta la carpeta actual (aunque tenga tildes/espacios).
- La renombra a un nombre estándar.
- Dentro de /paper, si existe un único .md, lo renombra a un nombre estándar.

No borra nada. Si algo no cuadra, muestra un WARNING y sigue.
"""

from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent

# Definimos el mapeo ideal PXX -> (lista de posibles nombres actuales, nuevo nombre estándar, nuevo nombre de paper)
PROJECTS = [
    # P01
    (1,
     ["p01_astro_subs_optimos", "p01_astro_subs_optimos".lower()],
     "p01_optimo_subs",
     "p01_optimo_subs.md"),
    # P02
    (2,
     ["p02_eeg_stress_states", "p02_estados_de_estres_eeg", "p02_eeg_estres"],
     "p02_estres_eeg",
     "p02_estres_eeg.md"),
    # P03
    (3,
     ["p03_eeg_pain_patterns", "p03_patrones_de_dolor_eeg", "p03_dolor_eeg"],
     "p03_dolor_eeg",
     "p03_dolor_eeg.md"),
    # P04
    (4,
     ["p04_eeg_bci_motor", "p04_bci_motor_eeg"],
     "p04_bci_motor_eeg",
     "p04_bci_motor_eeg.md"),
    # P05
    (5,
     ["p05_exposición_larga_snr", "p05_exposicion_larga_snr", "p05_long_exposure_snr"],
     "p05_exposicion_larga_snr",
     "p05_exposicion_larga_snr.md"),
    # P06
    (6,
     ["p06_ruido_térmico_marcos_oscuros", "p06_ruido_termico_marcos_oscuros", "p06_thermal_noise_darkframes"],
     "p06_ruido_termico_darkframes",
     "p06_ruido_termico_darkframes.md"),
    # P07
    (7,
     ["p07_planificación_óptima_de_marcos", "p07_planificacion_optima_de_marcos", "p07_optimal_frames_planning"],
     "p07_planificacion_capturas",
     "p07_planificacion_capturas.md"),
    # P08
    (8,
     ["p08_fotometría_grupos_abiertos", "p08_fotometria_grupos_abiertos", "p08_photometry_open_clusters"],
     "p08_fotometria_cumulos_abiertos",
     "p08_fotometria_cumulos_abiertos.md"),
    # P09
    (9,
     ["p09_contaminación_lumínica_las_condes", "p09_contaminacion_luminica_las_condes", "p09_light_pollution_las_condes"],
     "p09_contaminacion_luminica_las_condes",
     "p09_contaminacion_luminica_las_condes.md"),
    # P10
    (10,
     ["p10_canalización_de_reducción_de_python", "p10_canalizacion_de_reduccion_de_python", "p10_python_reduction_pipeline"],
     "p10_pipeline_reduccion",
     "p10_pipeline_reduccion.md"),
    # P11
    (11,
     ["p11_detección_de_gradiente_lp", "p11_deteccion_de_gradiente_lp", "p11_gradient_detection_lp"],
     "p11_detec_gradiente",
     "p11_detec_gradiente.md"),
    # P12
    (12,
     ["p12_sesiones_de_planificación_chile", "p12_sesiones_de_planificacion_chile", "p12_planning_sessions_chile"],
     "p12_planificacion_sesiones_chile",
     "p12_planificacion_sesiones_chile.md"),
    # P13
    (13,
     ["p13_variación_del_color_de_las_estrellas", "p13_variacion_del_color_de_las_estrellas", "p13_star_colour_variation"],
     "p13_color_estelar",
     "p13_color_estelar.md"),
    # P14
    (14,
     ["p14_algoritmos_de_apilamiento_osc", "p14_stacking_algorithms_osc"],
     "p14_algoritmos_apilado",
     "p14_algoritmos_apilado.md"),
    # P15
    (15,
     ["p15_ruido de impacto de tramado", "p15_ruido_de_impacto_de_tramado", "p15_dithering_impact_noise"],
     "p15_dithering_ruido_snr",
     "p15_dithering_ruido_snr.md"),
    # P16
    (16,
     ["p16_estadísticas del sendero starlink", "p16_estadisticas_del_sendero_starlink", "p16_starlink_trail_stats"],
     "p16_trazas_starlink",
     "p16_trazas_starlink.md"),
    # P17
    (17,
     ["p17_snr_modelo_multibanda", "p17_snr_model_multiband"],
     "p17_snr_multibanda",
     "p17_snr_multibanda.md"),
    # P18
    (18,
     ["p18_messier_ngc_de_chile", "p18_messier_ngc_from_chile"],
     "p18_messier_ngc_chile",
     "p18_messier_ngc_chile.md"),
    # P19
    (19,
     ["p19_nebulosas_de_ondículas_detalle", "p19_nebulosas_de_ondiculas_detalle", "p19_wavelets_nebulae_detail"],
     "p19_wavelets_nebulosas",
     "p19_wavelets_nebulosas.md"),
    # P20
    (20,
     ["p20_asi533_modelo_de_ruido_térmico", "p20_asi533_modelo_de_ruido_termico", "p20_asi533_thermal_noise_model"],
     "p20_asi533_ruido_termico",
     "p20_asi533_ruido_termico.md"),
]


def find_existing_dir(candidates):
    """Devuelve el Path de la carpeta que exista de la lista de posibles nombres."""
    for name in candidates:
        candidate = BASE_DIR / name
        if candidate.exists() and candidate.is_dir():
            return candidate
    return None


def rename_project_dir(old_path: Path, new_name: str) -> Path:
    """Renombra la carpeta de un proyecto si el nombre es distinto."""
    if old_path.name == new_name:
        print(f"  ✓ Carpeta ya tenía nombre estándar: {new_name}")
        return old_path

    new_path = BASE_DIR / new_name
    if new_path.exists():
        print(f"  ⚠ WARNING: ya existe {new_name}, no se renombra {old_path.name}. Revisa manualmente.")
        return old_path

    print(f"  → Renombrando carpeta: {old_path.name}  →  {new_name}")
    shutil.move(str(old_path), str(new_path))
    return new_path


def rename_paper_md(project_path: Path, new_md_name: str):
    """Renombra el archivo .md dentro de paper/ si hay uno claro."""
    paper_dir = project_path / "paper"
    if not paper_dir.exists() or not paper_dir.is_dir():
        print("    - Sin carpeta paper/ → nada que renombrar.")
        return

    md_files = list(paper_dir.glob("*.md"))
    if not md_files:
        print("    - Sin archivos .md dentro de paper/ → nada que renombrar.")
        return
    if len(md_files) > 1:
        # No adivinamos, solo informamos
        print("    ⚠ WARNING: Hay varios .md en paper/ → no se renombra automáticamente:")
        for f in md_files:
            print(f"       · {f.name}")
        return

    current_md = md_files[0]
    if current_md.name == new_md_name:
        print(f"    ✓ Paper ya tenía nombre estándar: {new_md_name}")
        return

    target = paper_dir / new_md_name
    if target.exists():
        print(f"    ⚠ WARNING: Ya existe {new_md_name} en paper/ → no se renombra {current_md.name}.")
        return

    print(f"    → Renombrando paper: {current_md.name}  →  {new_md_name}")
    current_md.rename(target)


def main():
    print("🚀 Limpieza de nombres OrionLab Research")
    print(f"Base: {BASE_DIR}")
    print("-" * 70)

    for pnum, candidates, new_dir, new_md in PROJECTS:
        print(f"\nP{pnum:02d} – objetivo: carpeta='{new_dir}', paper='{new_md}'")

        old_path = find_existing_dir(candidates)
        if not old_path:
            print("  ⚠ WARNING: No se encontró ninguna carpeta para este proyecto. Candidatos:")
            for c in candidates:
                print(f"     · {c}")
            continue

        project_path = rename_project_dir(old_path, new_dir)
        rename_paper_md(project_path, new_md)

    print("\n✅ Proceso completado.")
    print("Revisa la estructura en Git, y si todo se ve bien, ejecuta:")
    print("   git status")
    print("   git add .")
    print('   git commit -m \"Refactor: nombres estándar OrionLab Research\"')
    print("   git push origin main")


if __name__ == '__main__':
    main()
