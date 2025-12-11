from pathlib import Path
import csv
import textwrap
from datetime import date

# Asume que este script vive en la carpeta raíz de OrionLab_Research
BASE_DIR = Path(__file__).resolve().parent


def write_p02_eeg_stress():
    proj_dir = BASE_DIR / "p02_eeg_stress_states"
    data_dir = proj_dir / "data"
    paper_dir = proj_dir / "paper"

    data_dir.mkdir(parents=True, exist_ok=True)
    paper_dir.mkdir(parents=True, exist_ok=True)

    csv_path = data_dir / "eeg_stress_sessions.csv"

    rows = [
        # subject_id, session_date, device, condition, label, mean_alpha, mean_beta, hr_bpm, notes
        ["S01", "2022-11-10", "Muse 2", "rest_eyes_closed", "relaxed", 12.5, 7.1, 64, "Sesión base, ambiente silencioso"],
        ["S01", "2022-11-10", "Muse 2", "mental_arithmetic", "stressed", 8.7, 12.9, 82, "Suma mental continua 7 en 7"],
        ["S02", "2023-01-05", "Muse 2", "reading_neutral_text", "relaxed", 11.9, 7.9, 70, "Lectura tranquila 10 min"],
        ["S02", "2023-01-05", "Muse 2", "mental_arithmetic", "stressed", 9.1, 13.2, 85, "Tarea mental moderada"],
        ["S03", "2023-06-21", "OpenBCI", "breathing_exercise", "relaxed", 13.4, 6.8, 60, "Respiración 4-4-8"],
        ["S03", "2023-06-21", "OpenBCI", "time_pressure_task", "stressed", 8.3, 14.1, 90, "Tarea con límite de tiempo"],
        ["S04", "2024-03-14", "Muse S", "music_relaxing", "relaxed", 12.8, 7.4, 67, "Música ambiental suave"],
        ["S04", "2024-03-14", "Muse S", "email_overload", "stressed", 9.0, 13.8, 88, "Simulación de trabajo con muchos estímulos"],
        ["S05", "2024-09-02", "OpenBCI", "baseline", "relaxed", 12.2, 7.6, 66, "Referencia en reposo"],
        ["S05", "2024-09-02", "OpenBCI", "multitasking_screen", "stressed", 8.9, 14.5, 92, "Varias tareas en pantalla"],
    ]

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "subject_id",
            "session_date",
            "device",
            "condition",
            "label",
            "mean_alpha",
            "mean_beta",
            "hr_bpm",
            "notes",
        ])
        writer.writerows(rows)

    paper_path = paper_dir / "p02_eeg_stress_states_v1.md"

    paper_content = textwrap.dedent(f"""
    # EEG Stress States Classification using Low-Cost Devices
    **Author:** Hugo Baghetti Calderón (Chile)  
    **Affiliation:** OrionLab Research – tele.objetivo  

    ## Abstract

    Stress is typically measured through subjective scales or clinical interviews, but low-cost EEG devices
    and simple physiological markers (heart rate) make it possible to approximate stress states in everyday
    environments. In this preliminary study, we explore whether basic EEG band power (alpha and beta) combined
    with heart rate can distinguish relaxed vs. stressed conditions in a small set of controlled tasks.

    We collected synthetic-yet-realistic data inspired by sessions using devices such as Muse 2, Muse S
    and OpenBCI boards, across different tasks (mental arithmetic, breathing exercises, neutral reading).
    The dataset in `data/eeg_stress_sessions.csv` reflects plausible patterns seen in the literature:
    increased beta power and heart rate under cognitive load, and increased alpha power during relaxation.

    The goal is not to build a clinical-grade classifier, but to document a reproducible pipeline that
    can be used in teaching, prototyping BCI ideas, and designing experiments around stress and workload.

    ## 1. Introduction

    Measuring stress in real time is a recurring goal in applied neuroscience and human–computer interaction.
    While medical EEG systems and full polysomnography are out of reach for most users, a new generation of
    low-cost headsets has made it possible to experiment at home, in the lab, or in the classroom.

    This project proposes:

    - A small, structured dataset representing relaxed vs. stressed conditions.
    - A simple feature set (mean alpha, mean beta, heart rate).
    - A starting point for building logistic regression or tree-based models to classify states.

    The study is framed as part of **OrionLab Research**, connecting data science, neuroscience and
    engineering practice, and is intended to be reproducible with open-source tools (Python, Jupyter).

    ## 2. Materials and Methods

    ### 2.1 Devices

    The synthetic data is inspired by the capabilities of the following devices:

    - Muse 2 / Muse S (consumer EEG, dry electrodes).
    - OpenBCI board with standard EEG cap.

    For the purposes of this version, we focus on summary-level features:

    - Mean alpha band power (8–12 Hz).
    - Mean beta band power (13–30 Hz).
    - Heart rate (beats per minute, BPM).

    ### 2.2 Experimental Conditions

    Sessions are organized in pairs per subject:

    - **Relaxed conditions:** resting with eyes closed, controlled breathing, relaxing music, neutral reading.
    - **Stressed conditions:** mental arithmetic, multitasking, simulated email overload, time-pressure tasks.

    Each row in `eeg_stress_sessions.csv` represents a session-level summary:

    - `subject_id` – anonymized participant code.
    - `session_date` – date of recording (2019–2025 range in extended versions).
    - `device` – type of EEG hardware used.
    - `condition` – type of task performed.
    - `label` – target class (`relaxed` or `stressed`).
    - `mean_alpha`, `mean_beta` – normalized band power.
    - `hr_bpm` – average heart rate.
    - `notes` – short qualitative note.

    ### 2.3 Analysis Pipeline (Proposed)

    A typical pipeline using this dataset would:

    1. Load the CSV into a Pandas DataFrame.
    2. Explore distributions of alpha, beta and heart rate by label.
    3. Train a simple classifier (e.g., logistic regression, random forest).
    4. Evaluate accuracy, precision/recall, and interpret feature importances.

    This structure is designed to be used in teaching environments where students can run experiments
    locally, even with limited connectivity or hardware.

    ## 3. Results (Preliminary)

    Qualitative inspection of the synthetic data suggests:

    - Relaxed conditions show higher alpha power and lower heart rate.
    - Stressed conditions show higher beta power and elevated heart rate.
    - A linear decision boundary in the (alpha, beta, hr) space would separate most points.

    In a full implementation, these observations would be complemented with actual model training and
    cross-validation metrics.

    ## 4. Discussion

    This study defines a small but coherent schema for stress-related EEG data, aligned with the constraints
    of low-cost devices and small student projects. It is not a clinical dataset; instead, it acts as a
    scaffold for:

    - Teaching basic EEG data handling.
    - Prototyping BCI applications around stress detection.
    - Exploring multimodal features (EEG + heart rate).

    ## 5. Conclusions

    - Low-cost EEG devices combined with simple features can approximate stress vs. relaxation states.
    - A structured dataset and a clear schema are essential for reproducible teaching and experimentation.
    - This project will evolve towards including real recordings, more channels and time-resolved features.

    ## 6. Version History

    - v1.0 ({date.today().isoformat()}): Initial synthetic dataset and paper structure.

    ## 7. References

    - Manufacturer documentation (Muse, OpenBCI).
    - Introductory papers on EEG-based stress detection.
    - Future links to OrionLab experiments and Git repositories.
    """).strip() + "\n"

    paper_path.write_text(paper_content, encoding="utf-8")
    print("✅ P02 EEG stress content written.")


def write_p03_eeg_pain():
    proj_dir = BASE_DIR / "p03_eeg_pain_patterns"
    data_dir = proj_dir / "data"
    paper_dir = proj_dir / "paper"

    data_dir.mkdir(parents=True, exist_ok=True)
    paper_dir.mkdir(parents=True, exist_ok=True)

    csv_path = data_dir / "eeg_pain_experiments.csv"

    rows = [
        # subject_id, session_date, stim_type, intensity_level, channel, band, power_db, label
        ["S01", "2021-08-11", "thermal", 1, "Cz", "beta", -15.2, "baseline"],
        ["S01", "2021-08-11", "thermal", 3, "Cz", "beta", -10.4, "mild_pain"],
        ["S01", "2021-08-11", "thermal", 5, "Cz", "beta",  -7.8, "high_pain"],
        ["S02", "2022-02-03", "pressure", 2, "C3", "gamma", -14.1, "baseline"],
        ["S02", "2022-02-03", "pressure", 4, "C3", "gamma",  -9.9, "mild_pain"],
        ["S02", "2022-02-03", "pressure", 5, "C3", "gamma",  -7.2, "high_pain"],
        ["S03", "2023-07-19", "thermal", 2, "Cz", "beta", -13.5, "baseline"],
        ["S03", "2023-07-19", "thermal", 4, "Cz", "beta", -9.2, "mild_pain"],
        ["S04", "2024-05-09", "pressure", 3, "C4", "gamma", -11.3, "mild_pain"],
        ["S04", "2024-05-09", "pressure", 5, "C4", "gamma", -8.1, "high_pain"],
    ]

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "subject_id",
            "session_date",
            "stim_type",
            "intensity_level",
            "channel",
            "band",
            "power_db",
            "label",
        ])
        writer.writerows(rows)

    paper_path = paper_dir / "p03_eeg_pain_patterns_v1.md"

    paper_content = textwrap.dedent(f"""
    # EEG Patterns Associated with Pain and Nociceptive Stimuli
    **Author:** Hugo Baghetti Calderón (Chile)  
    **Affiliation:** OrionLab Research – tele.objetivo  

    ## Abstract

    Pain perception is a multi-dimensional phenomenon with clear electrophysiological correlates.
    In research and clinical practice, controlled nociceptive stimuli (thermal, pressure) are used
    to study how the brain responds to increasing levels of pain.

    This project defines a small, structured dataset (`data/eeg_pain_experiments.csv`) representing
    EEG power in selected channels and bands under baseline, mild and high pain conditions.
    The goal is to provide a realistic starting point for experimentation with classification
    models and visualization of pain-related EEG patterns, without requiring access to clinical
    datasets.

    ## 1. Introduction

    Objective markers of pain are a major challenge in neurology, anesthesiology and chronic pain research.
    While no single biomarker has been universally accepted, EEG changes in beta and gamma bands over
    central channels (e.g., Cz, C3, C4) have been repeatedly reported in controlled experiments.

    OrionLab Research approaches this topic from a data-science perspective:

    - Define a clear schema for pain-related EEG experiments.
    - Provide synthetic-yet-coherent data for teaching and prototyping.
    - Enable small-scale modelling exercises around pain vs. non-pain states.

    ## 2. Materials and Methods

    ### 2.1 Experimental Paradigm (Synthetic)

    The dataset simulates:

    - Thermal and pressure stimuli.
    - Intensity levels from 1 (very low) to 5 (high).
    - Central channels (Cz, C3, C4).
    - Bands of interest: beta and gamma.
    - Labels: `baseline`, `mild_pain`, `high_pain`.

    Each row in `eeg_pain_experiments.csv` includes:

    - `subject_id` – anonymized participant.
    - `session_date` – date of experiment.
    - `stim_type` – `thermal` or `pressure`.
    - `intensity_level` – ordinal 1–5.
    - `channel` – EEG channel.
    - `band` – frequency band.
    - `power_db` – relative power in dB.
    - `label` – experimental condition.

    ### 2.2 Suggested Analysis

    - Exploratory plots of power vs. intensity per band and channel.
    - Boxplots comparing baseline vs. mild vs. high pain.
    - Simple classifiers distinguishing baseline vs. pain states.
    - Discussion of limitations and ethical constraints of real pain experiments.

    ## 3. Results (Conceptual)

    The synthetic patterns follow these expectations:

    - Power in beta/gamma bands increases with intensity in pain conditions.
    - Differences between baseline and high pain are clearly separable.
    - Mild pain overlaps partially with both extremes, mirroring ambiguity
      seen in real experiments.

    ## 4. Discussion

    This project is designed as a **teaching and prototyping tool**, not as a clinical reference.
    It provides:

    - A compact schema that can be extended with real data.
    - A bridge between theoretical reading on pain EEG and hands-on modelling.
    - A template for future OrionLab datasets using real recordings and more complex features.

    ## 5. Conclusions

    - EEG-based pain research can be approached systematically with small structured datasets.
    - Synthetic data, when carefully designed, is useful to practice analysis techniques before
      working with sensitive clinical material.
    - OrionLab Research will use this project as a stepping stone towards BCI and assistive
      technology for patients experiencing chronic pain.

    ## 6. Version History

    - v1.0 ({date.today().isoformat()}): Initial dataset schema and paper structure.

    ## 7. References

    - Review articles on EEG and nociception.
    - Methodological papers on experimental pain paradigms.
    - Future links to OrionLab EEG projects and repositories.
    """).strip() + "\n"

    paper_path.write_text(paper_content, encoding="utf-8")
    print("✅ P03 EEG pain content written.")


def write_p04_eeg_bci():
    proj_dir = BASE_DIR / "p04_eeg_bci_motor"
    data_dir = proj_dir / "data"
    paper_dir = proj_dir / "paper"

    data_dir.mkdir(parents=True, exist_ok=True)
    paper_dir.mkdir(parents=True, exist_ok=True)

    csv_path = data_dir / "bci_motor_trials.csv"

    rows = [
        # subject_id, session_date, trial_id, command, predicted_command, correct, reaction_time_ms, confidence
        ["S01", "2022-10-01", 1, "left", "left", 1, 950, 0.82],
        ["S01", "2022-10-01", 2, "right", "right", 1, 910, 0.79],
        ["S01", "2022-10-01", 3, "up", "right", 0, 1200, 0.55],
        ["S02", "2023-02-15", 1, "left", "left", 1, 880, 0.87],
        ["S02", "2023-02-15", 2, "right", "right", 1, 930, 0.84],
        ["S02", "2023-02-15", 3, "down", "down", 1, 1020, 0.80],
        ["S03", "2024-06-07", 1, "up", "up", 1, 970, 0.81],
        ["S03", "2024-06-07", 2, "down", "down", 1, 990, 0.78],
        ["S03", "2024-06-07", 3, "left", "right", 0, 1300, 0.52],
        ["S04", "2025-01-12", 1, "neutral", "neutral", 1, 800, 0.88],
    ]

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "subject_id",
            "session_date",
            "trial_id",
            "command",
            "predicted_command",
            "correct",
            "reaction_time_ms",
            "confidence",
        ])
        writer.writerows(rows)

    paper_path = paper_dir / "p04_eeg_bci_motor_v1.md"

    paper_content = textwrap.dedent(f"""
    # Prototype EEG-based BCI for Simple Motor Control
    **Author:** Hugo Baghetti Calderón (Chile)  
    **Affiliation:** OrionLab Research – tele.objetivo  

    ## Abstract

    Brain–computer interfaces (BCI) for motor control typically rely on decoding motor imagery
    (imagined movements) or steady-state visual evoked potentials (SSVEP). In this project,
    we define the skeleton of a simple BCI experiment where users issue discrete commands
    ("left", "right", "up", "down", "neutral") and a classifier attempts to decode them
    from EEG features.

    The dataset `data/bci_motor_trials.csv` contains synthetic but realistic trial-level
    results: ground truth commands, predicted commands, correctness, reaction time and
    classifier confidence. The objective is to provide a compact basis for evaluating
    accuracy, latency and usability of simple BCI prototypes.

    ## 1. Introduction

    Assistive technologies based on BCI hold promise for users with severe motor impairments.
    Even simple discrete control (e.g., directional commands for a wheelchair or cursor)
    can have a major impact on autonomy.

    OrionLab Research approaches this from a practical engineering perspective:

    - Define clear metrics and data structures.
    - Start with a simple command vocabulary.
    - Focus on latency, confidence and accuracy as key variables.

    ## 2. Materials and Methods

    ### 2.1 Task

    Participants are instructed to issue one of five commands:

    - "left", "right", "up", "down", "neutral"

    The underlying assumption is that each command is associated with a distinct EEG pattern
    derived from motor imagery or specific visual cues. In this v1 dataset we abstract away
    raw EEG and store only the outputs of an imagined classifier.

    ### 2.2 Dataset Schema

    Each row in `bci_motor_trials.csv` contains:

    - `subject_id` – anonymized participant identifier.
    - `session_date` – date of recording (2019–2025 range in extended versions).
    - `trial_id` – trial number within the session.
    - `command` – intended command (ground truth).
    - `predicted_command` – classifier output.
    - `correct` – 1 if prediction matches command, 0 otherwise.
    - `reaction_time_ms` – latency from cue to classifier decision.
    - `confidence` – classifier confidence (0–1).

    ### 2.3 Evaluation

    This dataset supports basic analyses such as:

    - Overall accuracy and per-command accuracy.
    - Confusion matrices showing typical misclassifications.
    - Distribution of reaction times by correct vs. incorrect trials.
    - Relationship between confidence and correctness.

    ## 3. Results (Illustrative)

    In the synthetic sample:

    - Accuracy is high for some commands and lower for others.
    - Misclassifications often occur between "left" and "right".
    - Trials with longer reaction times tend to have lower confidence.

    These patterns are consistent with typical limitations of early BCI prototypes.

    ## 4. Discussion

    The goal of this project is not to report a finished BCI system, but to provide:

    - A **data structure** that can be extended with real EEG-derived features.
    - A **didactic example** for courses on data science, BCI and HCI.
    - A **testing ground** for exploring metrics beyond accuracy (e.g., information transfer rate).

    ## 5. Conclusions

    - Discrete-command BCI prototypes can be studied with compact trial-level datasets.
    - Careful recording of reaction times and confidence scores is crucial for evaluating usability.
    - Future versions will link this schema to real features derived from EEG recordings and
      motor imagery protocols.

    ## 6. Version History

    - v1.0 ({date.today().isoformat()}): Initial synthetic dataset and paper outline.

    ## 7. References

    - Introductory BCI literature on motor imagery.
    - Technical documentation for open-source BCI toolkits.
    - Future OrionLab research notes and implementations.
    """).strip() + "\n"

    paper_path.write_text(paper_content, encoding="utf-8")
    print("✅ P04 EEG BCI motor content written.")


def main():
    print(f"Using base directory: {BASE_DIR}")
    write_p02_eeg_stress()
    write_p03_eeg_pain()
    write_p04_eeg_bci()
    print("🎯 Done: P02, P03 and P04 updated with CSV + v1 papers.")


if __name__ == "__main__":
    main()
