    # Thermal Noise Model for ASI533MC Pro

    **Short Title:** Thermal Noise Model for ASI533MC Pro  
    **Project ID:** P20_ASI533_THERMAL_NOISE_MODEL  
    **Author:** Hugo Baghetti Calderón (OrionLab, Chile)  
    **Version:** 0.1 – 2025-12-11

    ---

    ## Abstract

    We model the thermal noise behaviour of the ZWO ASI533MC Pro camera under different cooling temperatures and exposure times, illustrating how dark current and read noise combine.

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

    **Author – Hugo Baghetti Calderón (Chile)**  
Independent researcher in data, neurotech and astrophotography.  
- M.Sc. in IT Management, Computer Engineer  
- Specialised in data architectures, analytics and astro imaging from Chile  
- Instagram: [@tele.objetivo](https://www.instagram.com/tele.objetivo)  
- Web: [www.teleobjetivo.cl](https://www.teleobjetivo.cl)  
- GitHub: [teleobjetivo](https://github.com/teleobjetivo)


