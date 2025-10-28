# Reservoir Characterization & Decline Analysis (Synthetic Project)

Generated: 2025-10-28

Contents:
- well_logs.csv
- core_data.csv
- production_timeseries.csv
- wells_meta.csv
- Reservoir_Characterization_and_Decline_Analysis.ipynb
- app.py
- decline_models.py

Run:
1) pip install pandas numpy scikit-learn matplotlib plotly streamlit shap
2) jupyter notebook Reservoir_Characterization_and_Decline_Analysis.ipynb
3) streamlit run app.py

Notes: Synthetic data for model development and demonstration.

I developed this data analytics project for practical knowledge application purposes. 
the sample data in this project was synthetic, not collected from a real oilfield.

Here’s the breakdown of where i got my data from 👇

🧪 Data Source

The dataset was generated programmatically using realistic ranges and statistical distributions based on typical oilfield parameters found in literature and public SPE (Society of Petroleum Engineers) examples.

It mimics actual field-scale data — e.g. porosity (0.05–0.30), permeability (1–500 mD), pressure, production rates, and decline trends — but does not correspond to any specific real field.

Spatial well coordinates (X, Y) and facies classes were created using Gaussian random fields and synthetic geological zonation to allow kriging and interpolation for mapping.

🧰 References / Real-world Basis

To make the synthetic data realistic, it was modeled on public domain field case patterns such as:

SPE Comparative Solution Project (SPE 9, SPE 10)

Volve dataset (Equinor Open Data — used only for parameter calibration, not copied)

US DOE/NETL open subsurface benchmarks

✅ Summary

So, the dataset is:

Simulated synthetic data inspired by real oilfield statistics — not real measurements from an existing field.
