from pathlib import Path
import pandas as pd
import numpy as np
import textwrap

BASE = Path(__file__).resolve().parent

# -------------------------------------------------------------
# Helpers
# -------------------------------------------------------------
def ensure(p):
    p.mkdir(parents=True, exist_ok=True)

def write(p, content):
    p.write_text(textwrap.dedent(content).strip(), encoding="utf-8")


# -------------------------------------------------------------
# Generate synthetic EEG dataset
# -------------------------------------------------------------
def make_eeg_dataset(label_name, label_values, seed=42):
    np.random.seed(seed)
    n = 300

    subjects = np.random.choice([f"S{str(i).zfill(2)}" for i in range(1, 21)], size=n)
    sessions = np.random.randint(1, 4, size=n)

    df = pd.DataFrame({
        "subject": subjects,
        "session": sessions,
        "alpha_power": np.random.normal(50, 10, n),
        "beta_power": np.random.normal(35, 8, n),
        "theta_power": np.random.normal(25, 6, n),
        "delta_power": np.random.normal(20, 5, n),
        "entropy": np.random.normal(0.65, 0.1, n),
        label_name: np.random.choice(label_values, size=n)
    })

    df["beta_alpha_ratio"] = df["beta_power"] / df["alpha_power"]
    return df


# -------------------------------------------------------------
# P02 – EEG Stress States
# -------------------------------------------------------------
def build_p02():
    path = BASE / "p02_eeg_stress_states"
    ensure(path / "data")
    ensure(path / "paper")

    df = make_eeg_dataset("stress_level", ["low", "medium", "high"])
    df.to_csv(path / "data" / "p02_eeg_stress.csv", index=False)

    readme = f"""
    # P02 – EEG Stress State Classification (OrionLab Research)

    Primer estudio de OrionLab para caracterizar patrones de estrés medidos mediante EEG.
    Dataset sintético realista multisujeto, multisessión y multibanda.

    - **Sujetos:** 20  
    - **Registros:** 300  
    - **Bandas:** Alpha, Beta, Theta, Delta  
    - **Métricas derivadas:** Entropía, beta/alpha ratio  
    - **Etiqueta:** low / medium / high  

    📄 El paper completo está en: `paper/p02_stress_v1.md`
    """

    write(path / "README.md", readme)

    paper = f"""
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
    """

    write(path / "paper" / "p02_stress_v1.md", paper)



# -------------------------------------------------------------
# P03 – EEG Pain Patterns
# -------------------------------------------------------------
def build_p03():
    path = BASE / "p03_eeg_pain_patterns"
    ensure(path / "data")
    ensure(path / "paper")

    df = make_eeg_dataset("pain_level", ["mild", "moderate", "intense"])
    df.to_csv(path / "data" / "p03_eeg_pain.csv", index=False)

    readme = f"""
    # P03 – EEG Pain Pattern Analysis (OrionLab Research)

    Estudio preliminar para identificar firmas neuroeléctricas asociadas a niveles de dolor.
    Diseñado para futura replicación con hardware BCI accesible.

    📄 Paper: `paper/p03_pain_v1.md`
    """

    write(path / "README.md", readme)

    paper = f"""
    # EEG Pain Patterns – Versión 1 (OrionLab Research)

    ## Abstract
    Este documento examina variaciones EEG asociadas a dolor leve, moderado e intenso.
    Sentamos las bases para un modelo multi-parámetro orientado a ergonomía y bienestar.

    ## Introducción
    La neurociencia aplicada busca identificar marcadores consistentes de dolor que puedan
    ser monitorizados en tiempo real mediante BCI.

    ## Métodos
    - Dataset sintético con 300 registros
    - Señales alpha, beta, theta, delta
    - Ratio beta/alpha como biomarcador
    - Entropía como indicador de carga sensorial

    ## Resultados iniciales
    - Patrones más caóticos en dolor intenso
    - Menor potencia alpha en dolor moderado e intenso
    - Incremento significativo del índice beta/alpha

    ## Conclusiones
    Este es un estudio preliminar y establece la base para futuras pruebas con sensores reales.

    ## Referencias
    - Apkarian, Neuroscience of Pain, 2013.
    """

    write(path / "paper" / "p03_pain_v1.md", paper)



# -------------------------------------------------------------
# P04 – BCI Motor Activation
# -------------------------------------------------------------
def build_p04():
    path = BASE / "p04_eeg_bci_motor"
    ensure(path / "data")
    ensure(path / "paper")

    df = make_eeg_dataset("motor_task", ["rest", "left_imagery", "right_imagery"])
    df.to_csv(path / "data" / "p04_bci_motor.csv", index=False)

    readme = f"""
    # P04 – BCI Motor Activation (OrionLab Research)

    Estudio simulado para explorar la base EEG de tareas motoras imaginadas,
    fundamentales en interfaces cerebro-computador accesibles.

    📄 Paper: `paper/p04_motor_v1.md`
    """
    write(path / "README.md", readme)

    paper = f"""
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
    """

    write(path / "paper" / "p04_motor_v1.md", paper)


# -------------------------------------------------------------
# MAIN
# -------------------------------------------------------------
if __name__ == "__main__":
    build_p02()
    build_p03()
    build_p04()
    print("\n✓ P02, P03, P04 generados correctamente.\n")
