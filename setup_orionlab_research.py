from pathlib import Path
import csv
import textwrap

# === 1. Configuración base ===
BASE_DIR = Path("/Users/hugobaghetti/Desktop/PROYECTOS/OrionLab_Research")

PROJECTS = [
    # EEG / Neuro
    ("p02_eeg_stress_states", "EEG Stress States Classification"),
    ("p03_eeg_pain_patterns", "EEG Pain Pattern Detection"),
    ("p04_eeg_bci_motor", "EEG BCI Motor Control Prototype"),

    # Astro / Foto científica (solo plantillas por ahora)
    ("p05_optolong_vs_narrowband", "Optolong L-Quad vs Narrowband in Bortle 7"),
    ("p06_guiding_star_adventurer", "Guiding Accuracy in Star Adventurer GTi"),
    ("p07_fwhm_seeing_estimation", "Seeing Estimation from FWHM with ASI533MC"),
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


def write_root_readme():
    content = textwrap.dedent("""
    # OrionLab Research – Independent Data & Astro Science

    Colección de estudios y experimentos de **OrionLab**, liderados por **Hugo Baghetti Calderón** (Chile),
    en la intersección de:

    - Neurociencia de datos (EEG, BCI, señales temporales)
    - Astrofotografía científica y análisis cuantitativo de cielo profundo
    - Ingeniería de datos aplicada a observación, modelos y simulación

    Cada carpeta `pXX_*` representa un estudio con:

    - `README.md` – Resumen ejecutivo del paper.
    - `data/` – Datos sintéticos o muestreados para reproducir gráficos.
    - `paper/` – Versión del paper en formato markdown (tipo revista científica).

    ## Índice de estudios

    - **P01 – Astro** – Modelo empírico de número óptimo de subs según cielo, objeto y cámara.
    - **P02 – Neuro** – Clasificación de estados de estrés / relajación usando EEG de bajo costo.
    - **P03 – Neuro** – Patrones EEG asociados a dolor y estímulos nociceptivos.
    - **P04 – Neuro/BCI** – Prototipo de interfaz cerebro–computador para control de motor.
    - **P05–P20 – Astro** – Estudios sobre filtros, SNR, guiado, contaminación lumínica,
      visibilidad desde Chile, ruido térmico de la ASI533MC Pro y técnicas de procesado.

    ## About Me – Hugo Baghetti Calderón

    Ingeniero en Informática y Magíster en Gestión TI, con más de 15 años liderando proyectos de tecnología,
    analítica y transformación digital. Mi trabajo combina estrategia, ciencia de datos y operación real de negocio,
    integrando capacidades técnicas con visión ejecutiva.

    Exploro, investigo y construyo soluciones. Mi enfoque une el método científico, la ingeniería y la narrativa visual:
    desde modelos analíticos hasta proyectos de cielo profundo.

    - 📧 Email: **teleobjetivo.boutique@gmail.com**
    - 🌐 Web: **https://www.teleobjetivo.cl**
    - 📸 Instagram: **[@tele.objetivo](https://www.instagram.com/tele.objetivo)**
    - 💻 GitHub (Analytics): **https://github.com/teleobjetivo/analytics-tech-portfolio**
    """).strip() + "\n"

    (BASE_DIR / "README.md").write_text(content, encoding="utf-8")


def create_project_skeleton(code: str, title: str):
    proj_dir = BASE_DIR / code
    data_dir = proj_dir / "data"
    paper_dir = proj_dir / "paper"

    data_dir.mkdir(parents=True, exist_ok=True)
    paper_dir.mkdir(parents=True, exist_ok=True)

    # README básico del proyecto
    readme_content = textwrap.dedent(f"""
    # {code.upper()} – {title}

    Este directorio forma parte de **OrionLab Research**.

    - 📂 **Código**: `{code}`
    - 📄 **Paper**: ver `paper/`
    - 📊 **Datos**: ver `data/`

    El objetivo de este estudio es documentar, de forma reproducible, un experimento de
    investigación aplicado a neurociencia de datos o astrofotografía científica, usando
    herramientas abiertas (Python, Jupyter, Git) y equipamiento accesible.

    ## Estructura

    - `data/` – CSV con datos de ejemplo para reproducir gráficos o análisis.
    - `paper/` – Versión 1 del paper (`*_v1.md`), en formato markdown tipo artículo científico.

    ## Estado

    - Versión inicial del esqueleto: pendiente completar paper y análisis detallado.
    """).strip() + "\n"

    (proj_dir / "README.md").write_text(readme_content, encoding="utf-8")

    # Template de paper en blanco
    paper_template = textwrap.dedent(f"""
    # {title}
    **Autor:** Hugo Baghetti Calderón (Chile)  
    **Afiliación:** OrionLab Research – tele.objetivo  

    ## Resumen

    *(Versión 1 – borrador)*  
    Incluir un resumen breve (150–250 palabras) que responda:  
    **Qué se estudia, cómo se mide, qué se encontró y por qué importa.**

    ## 1. Introducción

    - Contexto del problema.
    - Motivación científica / técnica.
    - Qué vacío de conocimiento se intenta abordar.
    - Qué aporta este estudio a la comunidad (neuro / astro / data).

    ## 2. Materiales y Métodos

    - Equipamiento o datasets utilizados.
    - Ubicación / condiciones (si aplica, por ejemplo observación desde Chile).
    - Descripción del pipeline de análisis paso a paso.
    - Supuestos y limitaciones.

    ## 3. Resultados

    - Principales hallazgos.
    - Gráficos clave (que pueden generarse a partir de `data/`).
    - Métricas relevantes.

    ## 4. Discusión

    - Interpretación de los resultados.
    - Comparación con trabajos previos (cuando corresponda).
    - Implicancias prácticas para la comunidad (observadores, clínicos, ingenieros).

    ## 5. Conclusiones

    - Qué se logró demostrar.
    - Recomendaciones concretas.
    - Próximos pasos.

    ## 6. Referencias

    - Añadir artículos, documentación, bases de datos o manuales relevantes.
    """).strip() + "\n"

    (paper_dir / f"{code}_v1.md").write_text(paper_template, encoding="utf-8")


def create_p01_full():
    """Crea P01 con CSV realista + paper completo v1."""
    code = "p01_astro_subs_optimos"
    title = "Modelo empírico para estimar el número óptimo de subs en astrofotografía de cielo profundo"

    proj_dir = BASE_DIR / code
    data_dir = proj_dir / "data"
    paper_dir = proj_dir / "paper"

    data_dir.mkdir(parents=True, exist_ok=True)
    paper_dir.mkdir(parents=True, exist_ok=True)

    # CSV de ejemplo: distintas combinaciones de cielo, objeto, equipo, etc.
    csv_path = data_dir / "p01_experimentos_subs.csv"
    rows = [
        # cielo, objeto, tipo, bortle, exp_seg, num_subs, snr_medio, camara, filtro
        ["Atacama", "NGC 3372", "Nebulosa de emisión", 1, 180, 40, 35.2, "ASI533MC Pro", "Optolong L-Quad"],
        ["Atacama", "NGC 3372", "Nebulosa de emisión", 1, 300, 30, 37.8, "ASI533MC Pro", "Optolong L-Quad"],
        ["Valle Central", "M42", "Nebulosa brillante", 5, 120, 60, 28.5, "ASI533MC Pro", "Optolong L-Quad"],
        ["Valle Central", "M42", "Nebulosa brillante", 5, 180, 40, 29.1, "ASI533MC Pro", "Optolong L-Quad"],
        ["Las Condes", "Roseta", "Nebulosa de emisión", 7, 180, 80, 22.3, "ASI533MC Pro", "Optolong L-Quad"],
        ["Las Condes", "Roseta", "Nebulosa de emisión", 7, 240, 60, 23.0, "ASI533MC Pro", "Optolong L-Quad"],
        ["Farellones", "NGC 253", "Galaxia", 3, 180, 90, 31.4, "ASI533MC Pro", "Sin filtro"],
        ["Farellones", "NGC 253", "Galaxia", 3, 240, 60, 32.1, "ASI533MC Pro", "Sin filtro"],
        ["Costa", "NGC 2070", "Región HII", 4, 180, 70, 29.8, "ASI533MC Pro", "Optolong L-Quad"],
        ["Costa", "NGC 2070", "Región HII", 4, 240, 50, 30.2, "ASI533MC Pro", "Optolong L-Quad"],
    ]

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "region", "objeto", "tipo_objeto", "bortle",
            "exposicion_seg", "num_subs", "snr_medio",
            "camara", "filtro"
        ])
        writer.writerows(rows)

    # README específico de P01
    readme_content = textwrap.dedent(f"""
    # P01 – {title}

    Estudio empírico para responder una pregunta práctica clave en astrofotografía de cielo profundo:

    > **¿Cuántas imágenes (subs) necesito realmente, con mi equipo y mi cielo, para obtener una señal aceptable
    en nebulosas y galaxias?**

    El foco está puesto en un setup real:

    - **Telescopio principal:** William Optics RedCat 51 MK2.5  
    - **Cámara:** ZWO ASI533MC Pro (refrigerada)  
    - **Montura:** Sky-Watcher Star Adventurer GTi  
    - **Filtro:** Optolong L-Quad Enhance Filter  
    - **Control:** ZWO ASIAIR Plus  
    - Observación desde Chile: cielos urbanos (Las Condes), valle, costa y zonas oscuras (Atacama, cordillera).

    ## Archivos

    - `data/p01_experimentos_subs.csv` – Tabla con experimentos sintéticos realistas, combinando:
      - Clase de cielo (Bortle 1–7)
      - Tipo de objeto (nebulosa, galaxia, región HII)
      - Exposición por sub (segundos)
      - Número de subs
      - SNR promedio aproximado
    - `paper/p01_subs_optimos_v1.md` – Versión 1 del paper en formato markdown.

    ## Objetivo del paper

    Proponer una **regla práctica** para planificar sesiones de astrofotografía en función de:

    - Bortle del sitio
    - Tipo de objeto
    - Equipo utilizado (setup de Hugo)
    - Tiempo total disponible en la noche

    El output buscado es del tipo:

    > “Desde Las Condes (Bortle 7) para una nebulosa de emisión con el setup RedCat 51 + ASI533MC Pro + L-Quad,
    > apuntando a SNR aceptable para procesado, necesitas aproximadamente *N* subs de *T* segundos.”

    Esto sirve tanto a la comunidad chilena como a cualquier usuario de equipo similar.

    ## Autor

    - **Hugo Baghetti Calderón** – OrionLab Research / tele.objetivo (Chile)
    """).strip() + "\n"

    (proj_dir / "README.md").write_text(readme_content, encoding="utf-8")

    # Paper completo V1 en markdown
    paper_content = textwrap.dedent("""
    # Modelo empírico para estimar el número óptimo de subs en astrofotografía de cielo profundo
    **Autor:** Hugo Baghetti Calderón (Chile)  
    **Afiliación:** OrionLab Research – tele.objetivo  

    ## Resumen

    La planificación de sesiones de astrofotografía de cielo profundo suele apoyarse en reglas empíricas poco
    documentadas: “tira todo lo que puedas”, “mínimo dos horas”, “mejor muchas subs cortas que pocas largas”.
    En este trabajo se propone un modelo empírico sencillo para orientar el número de subs necesarios en función
    del brillo del cielo (Bortle), el tipo de objeto y el setup utilizado, basado en el equipo real del autor
    (William Optics RedCat 51 MK2.5, ZWO ASI533MC Pro, filtro Optolong L-Quad y montura Sky-Watcher
    Star Adventurer GTi), observando desde distintos cielos de Chile (urbano, valle, costa y zonas oscuras).

    A partir de un conjunto de escenarios sintéticos realistas, se exploran combinaciones de exposición por sub,
    número de subs y cielo para derivar una regla práctica que pueda usarse en planificación: cuántos minutos
    o horas de integración son razonables para obtener una señal aceptable para procesado visual.

    ## 1. Introducción

    La mejora de sensores, filtros y software ha hecho que la astrofotografía de cielo profundo sea accesible
    incluso desde cielos urbanos altamente contaminados (por ejemplo, Las Condes, Santiago de Chile, Bortle ~7).
    Sin embargo, la pregunta operativa sigue siendo la misma:

    > ¿Cuánto tiempo tengo que integrar para que valga la pena salir?

    La literatura técnica y la experiencia de la comunidad sugieren que la señal-ruido (SNR) mejora con la
    raíz cuadrada del número de subs, pero rara vez se ofrece una guía concreta adaptada a un setup específico
    y a condiciones reales de observación desde un país determinado.

    En este trabajo se aborda el problema desde un enfoque práctico:

    - Se fija un setup realista (RedCat 51 + ASI533MC Pro + Optolong L-Quad + Star Adventurer GTi).
    - Se consideran distintos cielos típicos de Chile (desierto, cordillera, valle central, costa, ciudad).
    - Se modela de forma sintética una SNR promedio resultante de distintas combinaciones de exposición y número de subs.
    - Se propone una regla orientativa para planificar sesiones en función de Bortle, tipo de objeto y tiempo disponible.

    El objetivo no es reemplazar simulaciones físicas detalladas, sino ofrecer una herramienta intuitiva para
    astrofotógrafos que usan equipos portátiles similares y desean tomar decisiones informadas antes de salir.

    ## 2. Materiales y Métodos

    ### 2.1 Setup observacional

    El modelo y las recomendaciones se centran en el siguiente equipamiento:

    - Telescopio **William Optics RedCat 51 MK2.5** (refractor APO de campo amplio).
    - Cámara refrigerada **ZWO ASI533MC Pro** (sensor cuadrado, bajo ruido de lectura).
    - Filtro **Optolong L-Quad Enhance Filter**, optimizado para nebulosas en cielos contaminados.
    - Montura **Sky-Watcher Star Adventurer GTi**, en modo guiado.
    - Guía: **ZWO ASI120MM Mini** + mini telescopio de 30 mm.
    - Control y automatización mediante **ZWO ASIAIR Plus**.

    Se asume un guiado correctamente calibrado, con errores de seguimiento compatibles con exposiciones
    de 120–300 segundos sin elongación significativa de las estrellas.

    ### 2.2 Cielos considerados

    Se modelan los siguientes entornos típicos de observación en Chile:

    - **Atacama** – Bortle 1 (cielo excepcionalmente oscuro).
    - **Farellones / cordillera** – Bortle 3.
    - **Costa** – Bortle 4.
    - **Valle Central** – Bortle 5.
    - **Las Condes (Santiago)** – Bortle 7 (urbano brillante).

    ### 2.3 Dataset sintético

    El archivo `data/p01_experimentos_subs.csv` contiene escenarios sintéticos realistas combinando:

    - Región / cielo (`region`, `bortle`)
    - Objeto (`objeto`, `tipo_objeto`)
    - Exposición individual (`exposicion_seg`)
    - Número de subs (`num_subs`)
    - SNR media estimada (`snr_medio`)

    Estos valores no provienen de medidas fotométricas exactas, sino de una parametrización cualitativa que
    respeta tendencias razonables:

    - El SNR crece aproximadamente con la raíz del tiempo total de integración.
    - El SNR empeora con cielos más brillantes (mayor Bortle).
    - Nebulosas de emisión con filtro L-Quad se comportan mejor que galaxias sin filtro en cielos brillantes.

    Esto permite explorar patrones de manera reproducible, aun cuando el objetivo principal es metodológico.

    ### 2.4 Métrica principal

    Se trabaja con una SNR promedio adimensional `snr_medio`, que se interpreta cualitativamente como:

    - **SNR < 20** → Difícil de procesar; ruido muy dominante.
    - **SNR 20–30** → Aceptable para procesado cuidadoso; resultado “decente”.
    - **SNR > 30** → Muy buen punto de partida; detalle y contraste aprovechables.

    El interés práctico es identificar qué combinaciones cruzan el umbral de **SNR ≈ 25–30**.

    ## 3. Resultados

    A partir de los escenarios sintéticos del CSV, se observan patrones coherentes:

    1. En **Atacama (Bortle 1)**, con nebulosas de emisión y L-Quad, se alcanzan SNR > 35 con:
       - 40 subs de 180 s (2 horas) o
       - 30 subs de 300 s (2,5 horas).

    2. En el **Valle Central (Bortle 5)**, para M42 con filtro L-Quad:
       - 60 subs de 120 s (2 horas) dan SNR ≈ 28,5.
       - 40 subs de 180 s (2 horas) dan SNR ≈ 29,1.
       La ganancia adicional por alargar la exposición individual es marginal en este rango.

    3. En **Las Condes (Bortle 7)**, apuntando a Roseta:
       - 80 subs de 180 s (~4 horas) dan SNR ≈ 22,3.
       - 60 subs de 240 s (4 horas) dan SNR ≈ 23,0.
       Incluso con 4 horas, el SNR sigue limitado por el brillo del cielo.

    4. En **Farellones (Bortle 3)** con galaxias sin filtro:
       - 90 subs de 180 s (4,5 horas) → SNR ≈ 31,4.
       - 60 subs de 240 s (4 horas) → SNR ≈ 32,1.
       De nuevo, la diferencia entre muchas subs cortas y menos subs largas es secundaria frente al tiempo total.

    En resumen, el tiempo total de integración domina el resultado, como era esperable, pero se observan
    diferencias significativas entre cielos.

    ## 4. Discusión

    Los resultados apoyan varias conclusiones prácticas:

    1. **El cielo manda:** desde Las Condes, incluso 4 horas de integración con filtro L-Quad dejan el SNR
       en la zona 22–23, que es utilizable pero exigente en procesado. En Atacama, tiempos similares superan SNR 35.

    2. **Exposición individual razonable:** dentro de rangos estándar para la ASI533MC Pro (120–300 s),
       la diferencia entre muchos subs algo más cortos o menos subs algo más largos es secundaria para el SNR final,
       siempre que el histograma no se “pegue” al fondo ni a la saturación.

    3. **Regla de oro local:** para el setup descrito, parecen razonables las siguientes guías:

       - **Bortle 7 (Las Condes), nebulosas de emisión con L-Quad:**  
         - Mínimo razonable: 3 horas  
         - Recomendado: 4–5 horas

       - **Bortle 5 (Valle Central), nebulosas brillantes:**  
         - 2 horas ya permiten SNR cerca de 30.

       - **Bortle 3–4 (cordillera / costa), galaxias y regiones HII:**  
         - 3–4 horas producen datos muy sólidos.

       - **Bortle 1 (Atacama):**  
         - 2–3 horas pueden equivaler, en términos de SNR, a 4–5 horas en Bortle 5–7.

    4. **Equipo reproducible:** la combinación RedCat 51 + ASI533MC Pro + L-Quad es hoy un estándar de facto
       en astrofotografía portátil; por lo tanto, estas reglas son útiles para una gran cantidad de usuarios.

    ## 5. Conclusiones

    Este estudio propone una primera aproximación empírica para orientar la **cantidad de subs** necesaria en
    función del cielo, objeto y equipo, usando un setup realista operado desde Chile.

    No se trata de un modelo físico ni exhaustivo, sino de una herramienta práctica para:

    - Dimensionar el tiempo total de integración antes de salir.
    - Ajustar expectativas según Bortle y tipo de objeto.
    - Comunicar de forma honesta a la comunidad qué se puede esperar desde cielos urbanos versus cielos oscuros.

    Trabajos futuros pueden incorporar:

    - Medidas reales de SNR derivadas de datos brutos.
    - Modelos más precisos de ruido de lectura, dark current y banda estrecha.
    - Extensión del análisis a otros sensores (por ejemplo, ASI2600MC) y a telescopios de mayor focal.

    ## 6. Referencias

    - Manuales y documentación de ZWO (ASI533MC Pro, ASIAIR Plus).
    - Material técnico de William Optics sobre el RedCat 51 MK2.5.
    - Documentación de Optolong sobre el filtro L-Quad Enhance.
    - Experiencia de campo del autor, publicada en:
      - Instagram: [@tele.objetivo](https://www.instagram.com/tele.objetivo)  
      - Web: https://www.teleobjetivo.cl
    """).strip() + "\n"

    (paper_dir / "p01_subs_optimos_v1.md").write_text(paper_content, encoding="utf-8")


def main():
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    write_root_readme()

    # P01 completo
    create_p01_full()

    # Resto de proyectos en modo plantilla
    for code, title in PROJECTS:
        create_project_skeleton(code, title)

    print(f"✅ OrionLab Research creado en: {BASE_DIR}")


if __name__ == "__main__":
    main()
