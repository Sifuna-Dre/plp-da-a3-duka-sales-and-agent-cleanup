# PLP DA A3 - Duka Sales and Agent Cleanup

## Project Summary

This project contains two analytics engagements. The first explores Duka Electronics sales data for the January–June 2026 period and provides business insights on sales performance, products, branches and channels. The second audits, cleans and analyzes mobile money agent transactions before producing reliable summary reports and data-quality documentation.

## How To Run

1. Run `generate_data.py` to generate datasets.
2. Open and run all cells in `duka_sales_exploration.ipynb`.
3. Open and run all cells in `agent_cleanup.ipynb`.
4. Review exported outputs and Excel summaries.

## Duka Executive Summary

- The dataset contains 1,000 sales orders covering January to June 2026.
- Nairobi contributes the largest share of generated transactions.
- Premium products priced at KES 28,000 and above contribute significantly to overall revenue.
- Sales performance differs across products, branches and channels.
- Revenue rankings and order rankings are not always identical because product prices vary.

## Agent Data Cleaning Summary

Raw transaction records: 612

Cleaned transaction records: 600

Duplicate transaction records removed: 12