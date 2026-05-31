# Workbook Summary Template

Use this structure when presenting Excel workbook analysis results.

---

## 📊 {workbook_name}

**Sheets:** {sheet_count} | **Last Modified:** {last_modified} | **Size:** {file_size}

### Sheet Overview

| Sheet | Rows | Columns | Data Type |
|-------|------|---------|-----------|
| {sheet_name} | {row_count} | {col_count} | {data_type} |

### Key Metrics

| Metric | Value | Location |
|--------|-------|----------|
| {metric_name} | {metric_value} | {cell_ref} |

### Data Quality

| Check | Status | Details |
|-------|--------|---------|
| Empty Cells | {empty_status} | {empty_count} blanks |
| Duplicates | {dup_status} | {dup_count} found |
| Formulas | {formula_status} | {formula_count} cells |

{status indicators: ✅ Clean, ⚠️ Review, 🚨 Issues}

{if empty_count > 100: "⚠️ Significant missing data — review before processing"}
{if dup_count > 0: "⚠️ Duplicates detected — consider deduplication"}

---

*Generated from worksheet-mcp | {timestamp}*
