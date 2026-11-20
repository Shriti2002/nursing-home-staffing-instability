# Data Dictionary

Fill this in during profiling. One row per column you actually use.

## PBJ Daily Nurse Staffing
**One row = one nursing home on one day.**

| Column | Plain meaning | Type | Issues found |
|---|---|---|---|
| PROVNUM | Home ID (CMS Certification Number). Must stay text, has leading zeros | string | |
| STATE | State | string | |
| WorkDate | Date, stored as YYYYMMDD number | int → date | |
| MDScensus | Residents in the home that day | int | |
| Hrs_RN | Registered nurse hours (excl. director/admin) | float | |
| Hrs_LPN | Licensed practical nurse hours | float | |
| Hrs_CNA | Certified nurse aide hours | float | |
| Hrs_NAtrn | Nurse aide in training hours | float | |
| Hrs_MedAide | Medication aide hours | float | |
| *_emp / *_ctr | Employee vs contract (agency) split of each | float | |

## Provider Information
**One row = one nursing home.**

| Column | Plain meaning | Type | Issues found |
|---|---|---|---|
| CMS Certification Number (CCN) | Home ID, joins to PROVNUM | string | |
| Ownership Type | For profit / Non profit / Government (with sub-types) | string | |
| Number of Certified Beds | Size | int | |
| State | State | string | |
