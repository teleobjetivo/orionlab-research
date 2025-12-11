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

- v1.0 (2025-12-11): Initial synthetic dataset and paper structure.

## 7. References

- Manufacturer documentation (Muse, OpenBCI).
- Introductory papers on EEG-based stress detection.
- Future links to OrionLab experiments and Git repositories.
