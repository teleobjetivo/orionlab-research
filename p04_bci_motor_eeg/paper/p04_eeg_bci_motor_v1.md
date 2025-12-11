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

- v1.0 (2025-12-11): Initial synthetic dataset and paper outline.

## 7. References

- Introductory BCI literature on motor imagery.
- Technical documentation for open-source BCI toolkits.
- Future OrionLab research notes and implementations.
