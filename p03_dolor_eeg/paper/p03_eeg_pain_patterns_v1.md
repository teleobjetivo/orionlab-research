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

- v1.0 (2025-12-11): Initial dataset schema and paper structure.

## 7. References

- Review articles on EEG and nociception.
- Methodological papers on experimental pain paradigms.
- Future links to OrionLab EEG projects and repositories.
