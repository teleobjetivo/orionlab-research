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
