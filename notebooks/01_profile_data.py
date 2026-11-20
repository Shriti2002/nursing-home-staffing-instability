"""
Step 1: Profile the raw data before building anything.

Run from the project root:
    python notebooks/01_profile_data.py data/raw/<PBJ file>.csv data/raw/<Provider Info file>.csv

Goal: answer, in writing (docs/data_dictionary.md):
  - What does one row mean?
  - How many rows, columns, unique homes?
  - Missing values, zeros, impossible values?
  - Do home IDs match between the two files?
"""
import sys
import pandas as pd

pbj_path, prov_path = sys.argv[1], sys.argv[2]

# --- PBJ daily staffing -------------------------------------------------
# dtype=str for PROVNUM keeps leading zeros (e.g. "015009", not 15009)
pbj = pd.read_csv(pbj_path, dtype={"PROVNUM": str}, encoding="latin-1", low_memory=False)

print("=== PBJ: shape (rows, columns) ===")
print(pbj.shape)
print("\n=== PBJ: column types ===")
print(pbj.dtypes)
print("\n=== PBJ: first rows ===")
print(pbj.head())
print("\n=== PBJ: missing values per column ===")
print(pbj.isna().sum()[lambda s: s > 0])
print("\n=== PBJ: unique homes ===", pbj["PROVNUM"].nunique())
print("=== PBJ: unique dates ===", pbj["WorkDate"].nunique())
print("\n=== PBJ: summary of numbers ===")
print(pbj.describe().T)

# Sanity check: total nurse hours per resident day (expect roughly 3.5-4 on average)
hrs = pbj[["Hrs_RN", "Hrs_LPN", "Hrs_CNA", "Hrs_NAtrn", "Hrs_MedAide"]].sum(axis=1)
pbj["total_hprd"] = hrs / pbj["MDScensus"].where(pbj["MDScensus"] > 0)
print("\n=== Total nurse HPRD (sanity check) ===")
print(pbj["total_hprd"].describe())
print("Days with census = 0:", (pbj["MDScensus"] == 0).sum())
print("Days with 0 RN hours:", (pbj["Hrs_RN"] == 0).sum())

# --- Provider info ------------------------------------------------------
prov = pd.read_csv(prov_path, dtype=str, encoding="latin-1")
id_col = [c for c in prov.columns if "Certification Number" in c or c.upper() == "CCN"][0]

print("\n=== Provider: shape ===", prov.shape)
print("ID column:", id_col)
print("\n=== Ownership types ===")
print(prov["Ownership Type"].value_counts())

# --- Do the IDs match? --------------------------------------------------
pbj_ids, prov_ids = set(pbj["PROVNUM"]), set(prov[id_col])
print("\n=== ID match check ===")
print("Homes in PBJ:", len(pbj_ids))
print("Homes in Provider file:", len(prov_ids))
print("In both:", len(pbj_ids & prov_ids))
print("PBJ only (no provider info):", len(pbj_ids - prov_ids))
