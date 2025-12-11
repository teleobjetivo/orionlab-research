# P05 – Long Exposure SNR Model for DSLR & Cooled Cameras

**Autor:** Hugo Baghetti Calderón – OrionLab Research (Chile)  
**Fecha versión:** 2025-12-11  
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

