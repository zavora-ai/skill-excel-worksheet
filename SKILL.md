---
name: excel-worksheet
description: Orchestrate Excel/spreadsheet operations — create workbooks, read/write cells, formulas, charts (12 types), pivot tables, conditional formatting, data validation, tables, images, shapes, comments, protection, page setup, and advanced features (slicers, timelines, form controls). Use when creating spreadsheets, reading Excel data, writing formulas, building charts, creating pivot tables, formatting cells, or generating reports.
license: Apache-2.0
compatibility: Requires worksheet-mcp server connected. Native xlsx read/write via zavora-xlsx (Rust). No Excel installation needed.
allowed-tools: [create_workbook, open_workbook, save_workbook, close_workbook, configure_workbook, list_sheets, get_sheet_dimensions, describe_workbook, add_sheet, rename_sheet, delete_sheet, read_sheet, read_cell, search_cells, sheet_to_csv, write_cells, write_row, write_column, write_rich_text, write_json_rows, write_formula, manage_cell, set_cell_format, merge_cells, set_row_column_format, set_dimensions, freeze_panes, autofit_columns, add_chart, add_waterfall_chart, add_funnel_chart, add_treemap_chart, add_sunburst_chart, add_histogram_chart, add_box_whisker_chart, add_map_chart, add_slicer, add_timeline, add_form_control, add_table, add_conditional_format, add_data_validation, add_sparkline, add_image, add_shape, add_pivot_table, set_page_setup, manage_comments, add_threaded_comment, add_link, manage_defined_names, modify_rows, modify_columns, group, protect, protect_sheet_advanced, manage_autofilter, set_doc_properties, save_workbook_advanced, open_workbook_encrypted]
metadata:
  author: Zavora AI
  mcp-server: worksheet-mcp
  category: mcp-enhancement
  success-criteria:
    trigger-rate: "95% on spreadsheet queries"
    formula-accuracy: "Formulas calculate correctly"
    chart-quality: "Appropriate chart type for data"
---

# Excel & Worksheet

You create and manipulate Excel spreadsheets — write data, build formulas, create charts (12 types), pivot tables, conditional formatting, and professional reports. No Excel installation needed. Always save after changes.

## Decision Tree

```
├── "create spreadsheet", "new workbook"? → create_workbook
├── "open", "read Excel"? → open_workbook → read_sheet
├── "write", "enter data"? → write_cells / write_row / write_json_rows
├── "formula", "SUM", "VLOOKUP"? → write_formula
├── "chart", "graph", "visualize"? → add_chart (pick type by data)
├── "pivot table", "summarize"? → add_pivot_table
├── "format", "bold", "color"? → set_cell_format
├── "conditional format", "color scale"? → add_conditional_format
├── "table", "filter"? → add_table
├── "validate", "dropdown"? → add_data_validation
├── "protect", "lock"? → protect / protect_sheet_advanced
├── "save"? → save_workbook
├── "export CSV"? → sheet_to_csv
```

## Key Workflows

### Create Report (5 calls)
1. `create_workbook()` → workbook_id
2. `write_json_rows(data, start: "A1")` → data with headers
3. `add_table(range: "A1:E20", style: "TableStyleMedium2")` → formatted table
4. `add_chart(type: "column", data_range, title)` → visualization
5. `save_workbook(path: "report.xlsx")` → saved

### Read & Analyze (3 calls)
1. `open_workbook(path: "data.xlsx")` → workbook_id
2. `read_sheet(sheet: "Sales")` → all data
3. `describe_workbook()` → sheets, dimensions, sample

### Build Dashboard (6 calls)
1. `create_workbook()` → id
2. `write_json_rows(data)` → raw data sheet
3. `add_pivot_table(rows: ["Region"], values: ["Revenue"])` → summary
4. `add_chart(type: "pie", data_range)` → pie chart
5. `add_conditional_format(range, type: "color_scale")` → heatmap
6. `save_workbook(path: "dashboard.xlsx")`

## MUST DO
- Always `save_workbook` after changes (data is in-memory until saved)
- Use `add_table` for structured data (enables filtering, totals)
- Pick chart type by data: bar (comparison), line (trend), pie (composition), scatter (correlation)
- Use `autofit_columns` for readability
- `close_workbook` when done (frees memory)

## MUST NOT DO
- Don't forget to save (changes lost on close)
- Don't use pie charts for > 6 categories
- Don't leave raw data without formatting (hard to read)
- Don't write formulas with hardcoded values (use cell references)

## Chart Type Guide

| Data Pattern | Chart Type | Tool |
|-------------|-----------|------|
| Compare categories | Bar/Column | `add_chart(type: "column")` |
| Trend over time | Line | `add_chart(type: "line")` |
| Part of whole | Pie/Doughnut | `add_chart(type: "pie")` |
| Correlation | Scatter | `add_chart(type: "scatter")` |
| Cumulative | Area | `add_chart(type: "area")` |
| Financial flow | Waterfall | `add_waterfall_chart` |
| Sales pipeline | Funnel | `add_funnel_chart` |
| Hierarchy | Treemap/Sunburst | `add_treemap_chart` |
| Distribution | Histogram/Box | `add_histogram_chart` |
| Geographic | Map | `add_map_chart` |

## Cross-MCP Orchestration

### Excel + Analytics: Export Dashboard
```
ANALYTICS: query_metric(name: "monthly_revenue", period: "12m") → data points
EXCEL: create_workbook → write_json_rows(data) → add_chart(type: "line") → save
→ Professional Excel report from live data
```

### Excel + Finance: Financial Report
```
FINANCE: get_income_statement(period: "Q1") → line items
EXCEL: create_workbook → write_json_rows → add_table → write_formula("=SUM(...)") → save
→ Formatted P&L spreadsheet
```

### Excel + CRM: Pipeline Export
```
CRM: list_deals(stage: "all") → deals with values
EXCEL: create_workbook → write_json_rows(deals) → add_pivot_table(rows: ["stage"], values: ["amount"]) → add_funnel_chart → save
→ Pipeline funnel report
```
