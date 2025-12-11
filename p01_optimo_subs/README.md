# P01 – Modelo empírico para estimar el número óptimo de subs en astrofotografía de cielo profundo

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
