# DDS + SEQACS Data-Driven Reproducibility Package

This package uses the **five attached SEQACS CSV files (520,000 total rows)** as its empirical/simulation dataset.

Paper: *Dual-Domain Security: A Formal Theory of Hybrid Cryptographic Optimality in Quantum-Classical Systems*

## Important distinction
The dataset is synthetic/simulation data. It can provide numerical consistency checks and empirical illustrations of the DDS formulation, but it does not by itself prove a cryptographic theorem. The formal proof and its assumptions remain logically separate.

## Run
`pip install -r requirements.txt`
`jupyter lab`
Run notebooks 00 through 08 in order, or run `python run_all.py`.

## Data
The package contains normalized copies:
`data/seqacs_part_1.csv` ... `data/seqacs_part_5.csv`.
