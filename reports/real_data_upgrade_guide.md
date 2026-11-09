# Upgrade this sample with real Victorian Government open data

The starter project uses synthetic data so that you can practise safely and run the code immediately.

A relevant real-data starting point is the **Department of Families, Fairness and Housing Annual Report datasets – 2023-24** on DataVic:
https://discover.data.vic.gov.au/dataset/department-of-families-fairness-and-housing-annual-report-datasets-2023-24

The catalogue page lists machine-readable resources including Portfolio Performance Measures, Budget Portfolio Outcomes and Social Housing dwelling stock. Review the workbook, definitions, reporting period, licence and limitations before choosing a resource.

Suggested approach:
1. Open the DataVic dataset page and download one XLSX resource, preferably Portfolio Performance Measures for an initial performance-analysis exercise.
2. Record the exact dataset title, publisher, URL, download date, licence, reporting period and field definitions.
3. Inspect the workbook sheets and headers before writing analysis code.
4. Create a separate `data/raw/` folder for the original file and `data/processed/` for cleaned extracts.
5. Adapt the analysis to the actual fields. Do not assume that the synthetic columns in this starter project exist in the real workbook.
6. Cite the dataset in your README and report, and explain missing data, definitions and comparability limits.
7. Never infer individual outcomes or causal effects from aggregate annual-report measures.

DataVic is a discovery portal; the publishing agency hosts and maintains the underlying data. Public data should still be checked for context and limitations.
