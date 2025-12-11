# EEG Stress States – Versión 1 (OrionLab Research)

## Abstract
Este estudio explora patrones de estrés humano mediante parámetros EEG basados
en potencias espectrales y métricas derivadas como la entropía y el índice beta/alpha.
El objetivo es sentar las bases para un clasificador robusto de estados cognitivo-emocionales,
con aplicaciones en educación, ergonomía digital y salud ocupacional.

## Introducción
La medición del estrés mediante EEG se ha vuelto relevante en sistemas modernos de
evaluación cognitiva y monitoreo continuo. Este paper establece la primera versión del
estudio OrionLab orientado a caracterizar la señal bajo escenarios de estrés “low/medium/high”.

## Métodos
- 20 sujetos
- 300 registros
- 4 bandas EEG principales
- Señales generadas con estructura realista
- Derivación del índice beta/alpha
- Dataset: `data/p02_eeg_stress.csv`

## Resultados preliminares
- Incremento del índice beta/alpha en niveles altos de estrés
- Mayor entropía en estados elevados
- Distribución diferenciada alpha/beta por nivel de estrés

## Discusión
Esta primera versión sirve como base para modelos supervisados.  
Próximas versiones incluirán ICA, extracción de ERPs y modelos deep learning básicos.

## Referencias
- Klimesch, W. EEG alpha and theta oscillations. *Brain Research Reviews*, 1999.