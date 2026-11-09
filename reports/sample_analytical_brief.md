# Sample analytical brief
## Victorian Public Service Demand & Performance Analysis
**Audience:** Senior program and service-delivery managers  
**Period:** January 2024 – December 2025  
**Data status:** Synthetic demonstration data — not official Victorian Government data

### Purpose
This demonstration examines service requests received and completed, open requests, overdue requests and median waiting times across 12 illustrative regions. It shows how descriptive analysis can help managers ask better questions about demand, throughput and service pressure.

### Illustrative findings
The supplied synthetic dataset contains 288 region-month records. The analysis calculates monthly incoming demand, completed requests, completion rate, net demand, open requests and waiting-time indicators. Regional summaries enable comparison of average open requests and completion rates.

Run `python src/analyse.py` to generate the exact summary tables from the included dataset. Because the data are simulated, any patterns or values are instructional only and must not be interpreted as evidence about actual Victorian services.

### Interpretation framework
- **Demand:** Are requests received increasing, decreasing or seasonal?
- **Throughput:** Are completions keeping pace with incoming requests?
- **Backlog:** Are open requests accumulating in particular regions?
- **Timeliness:** Do waiting-time indicators suggest service pressure?
- **Equity and context:** Do regional differences reflect population, eligibility, service complexity, workforce capacity or data capture practices?

### Assumptions
1. Each row represents one region in one month.
2. Request counts are non-negative and use consistent definitions across regions and months.
3. The completion rate is calculated as requests completed divided by requests received in the same period. This is a throughput indicator, not a cohort-based resolution rate.
4. Median waiting days are treated as a monthly regional summary and are not averaged as if they were individual-level observations.
5. End-of-month open requests are taken as supplied; they are not reconstructed from monthly receipts and completions.

### Limitations
- All data are synthetic and do not represent a real service or government dataset.
- The sample has no population denominators, so raw regional counts should not be interpreted as relative need or performance.
- The dataset does not include case complexity, eligibility, priority, staffing, service outcomes or repeat requests.
- A same-month completion ratio does not track whether the completed requests are the same requests received in that month.
- Regional comparisons may be affected by different service mixes and recording practices.

### Recommendations for a real analysis
1. Confirm definitions, coverage, data lineage and reporting periods with the data owner.
2. Add population or eligible-client denominators where appropriate.
3. Segment by service type, priority and complexity before drawing conclusions.
4. Validate whether backlog and waiting-time measures are comparable across regions.
5. Discuss findings with program-area stakeholders and document alternative explanations.
6. Use the analysis as one input to decisions, alongside service context, costs, outcomes and lived-experience evidence.

### Suggested management questions
- Which service types contribute most to changes in demand?
- Is backlog growth persistent or seasonal?
- Are long waits concentrated among particular cohorts or locations?
- What additional data are needed before considering resource allocation changes?

**Conclusion:** Descriptive analytics can identify patterns and questions for investigation. It cannot, on its own, establish causes or prove that a particular funding intervention will improve outcomes.
