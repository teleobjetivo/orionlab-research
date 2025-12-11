# BCI Motor Activation – Versión 1 (OrionLab Research)

## Abstract
Evaluamos patrones EEG vinculados a tareas motoras imaginadas (MI) como mover la mano
izquierda o derecha. Es la base de todo sistema BCI para control de dispositivos.

## Introducción
Los paradigmas MI permiten controlar dispositivos sin movimiento físico.
Este paper prepara terreno para modelos de clasificación MI-friendly.

## Métodos
- Etiquetas: rest, left_imagery, right_imagery
- Bandas alpha y beta claves en tareas motoras
- Índice beta/alpha como métrica central
- Dataset en `data/p04_bci_motor.csv`

## Resultados
- Reducción alpha en laterización imaginada
- Incremento beta en movimiento imaginado
- Diferencias claras entre hemisferios (simuladas)

## Conclusiones
Este es un pre-estudio para futura integración con hardware BCI real.

## Referencias
- Pfurtscheller & Lopes da Silva, *EEG motor imagery*, 1999.