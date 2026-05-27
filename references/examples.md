# Excel Examples

## Example 1: "Create a sales report with chart"
```
create_workbook() → {id: "wb_001"}
write_json_rows(id: "wb_001", sheet: "Sales", data: [
  {month: "Jan", revenue: 450000, target: 400000},
  {month: "Feb", revenue: 520000, target: 450000},
  {month: "Mar", revenue: 610000, target: 500000}
])
add_table(id: "wb_001", sheet: "Sales", range: "A1:C4", style: "TableStyleMedium9")
add_chart(id: "wb_001", type: "column", data_range: "A1:C4", title: "Q1 Revenue vs Target")
save_workbook(id: "wb_001", path: "/reports/q1-sales.xlsx")
```
Response: "Sales report created: 3 months data, table formatted, column chart added. Saved to q1-sales.xlsx"

## Example 2: "Open the budget file and summarize by department"
```
open_workbook(path: "/data/budget-2026.xlsx") → {id: "wb_002"}
describe_workbook(id: "wb_002") → {sheets: ["Expenses"], rows: 500, cols: 8}
add_pivot_table(id: "wb_002", source: "Expenses!A1:H500", rows: ["Department"], values: [{"field": "Amount", "function": "sum"}])
save_workbook(id: "wb_002", path: "/data/budget-2026.xlsx")
```
Response: "Pivot table added: spend by department. Engineering: KES 12M, Marketing: KES 8M, Sales: KES 6M."

## Example 3: "Add conditional formatting — green for above target, red for below"
```
add_conditional_format(id: "wb_001", sheet: "Sales", range: "B2:B4", rules: [
  {type: "cell", criteria: ">=", value: "C2", format: {bg_color: "#C6EFCE"}},
  {type: "cell", criteria: "<", value: "C2", format: {bg_color: "#FFC7CE"}}
])
save_workbook(id: "wb_001", path: "/reports/q1-sales.xlsx")
```
Response: "Conditional formatting applied: green when revenue ≥ target, red when below."
