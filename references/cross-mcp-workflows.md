# Excel Cross-MCP Workflows

## Excel + Analytics: Live Data Report
```
ANALYTICS: query_metric("monthly_revenue", "12m") → data
EXCEL: create_workbook → write_json_rows → add_chart("line") → save
```

## Excel + Finance: P&L Spreadsheet
```
FINANCE: get_income_statement("Q1") → line items
EXCEL: create_workbook → write_json_rows → add_table → write_formula("=SUM(...)") → save
```

## Excel + CRM: Pipeline Funnel
```
CRM: list_deals(stage: "all") → deals
EXCEL: write_json_rows → add_pivot_table(rows: ["stage"]) → add_funnel_chart → save
```

## Excel + Inventory: Stock Report
```
INVENTORY: item_list() → all items with levels
EXCEL: write_json_rows → add_conditional_format(red if below reorder) → save
```
