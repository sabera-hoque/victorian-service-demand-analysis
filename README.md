# Victorian Public Service Demand & Performance Analysis (Sample Portfolio Project)

## Purpose
A portfolio-ready example showing how an analyst could examine service demand, throughput, backlog and waiting times across Victorian regions.

**Important:** `data/service_demand_synthetic.csv` is entirely synthetic demonstration data. It is not Victorian Government administrative data, does not describe real departmental performance, and must not be presented as official statistics. The project demonstrates an analytical workflow only.

## Questions
1. How does monthly demand change over time?
2. How does completion volume compare with incoming requests?
3. Which regions have the largest end-of-month open-request volumes?
4. How do median waiting times vary by region?
5. What limitations should decision-makers consider?

## Contents
- `data/service_demand_synthetic.csv` — synthetic monthly data for 12 illustrative regions across 2024–2025.
- `src/analyse.py` — Python cleaning, KPI calculation and summary outputs.
- `src/analysis.sql` — SQL examples for common analyst questions (SQLite-compatible).
- `reports/sample_analytical_brief.md` — example two-page-style briefing with findings, assumptions and recommendations.
- `powerbi/powerbi_build_guide.md` — instructions for creating a Power BI report.
- `requirements.txt` — Python dependencies.

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\\Scripts\\activate   # Windows
pip install -r requirements.txt
python src/analyse.py
```

Outputs are written to `outputs/`:
- `monthly_kpis.csv`
- `regional_summary.csv`
- `data_quality_checks.csv`

## Suggested portfolio description
Built an end-to-end public-service demand analytics demonstration using synthetic data: performed data-quality checks and KPI calculations in Python, wrote SQL queries for trend and regional analysis, and designed a Power BI dashboard specification with documented assumptions and limitations.

## Before using with real open data
Replace the synthetic CSV with a suitable public dataset from Data Vic or another authoritative Victorian Government source. Record the dataset title, publisher, URL, extraction date, field definitions and any caveats. Revisit all calculations to match the actual data dictionary. Do not imply that synthetic findings are real.
