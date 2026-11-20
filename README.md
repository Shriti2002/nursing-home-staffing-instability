# Nursing Home Staffing Instability vs Care Quality

> **Status:** In progress. Step 1: data profiling.

## Approach
Exploring the data first. Research questions will be written once the data is understood.

## Data (all public, U.S. Centers for Medicare & Medicaid Services)
| Dataset | What it gives | Source |
|---|---|---|
| Payroll-Based Journal (PBJ) Daily Nurse Staffing | Nurse hours per home per day, employee vs contract, daily resident count | [data.cms.gov](https://data.cms.gov/quality-of-care/payroll-based-journal-daily-nurse-staffing) |
| Nursing Home Provider Information | Ownership type, beds, state, chain | [data.cms.gov](https://data.cms.gov/provider-data/dataset/4pq5-n9py) |
| Health Deficiencies | Inspection citations and severity | [data.cms.gov](https://data.cms.gov/provider-data/dataset/r5ix-sfxw) |
| Penalties | Fines and payment denials | [data.cms.gov](https://data.cms.gov/provider-data/dataset/g6vv-u9sr) |

## Tools
- **BigQuery (SQL):** loading, cleaning, joins, window functions
- **Python (pandas, scipy, statsmodels):** exploration and statistics
- **Tableau Public:** dashboard

## Related research
- Mukamel et al. (2023), *JAMA Network Open*: staffing instability and quality, 2017-2019 data.
- Mukamel et al. (2024), *JAMDA*: staffing and health outcomes revisited, correcting for hidden bias.

## Repository structure
```
sql/         BigQuery queries, run in numbered order
notebooks/   Python profiling and analysis
data/raw/    downloaded CMS files (not committed, too large)
data/processed/  small exported tables
figures/     charts
docs/        data dictionary and notes
```

## Findings
_To be added._

## Limitations
_To be added._
