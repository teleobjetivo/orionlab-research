# P07 – Planificación de lights & darks según cielo y tipo de objeto

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
