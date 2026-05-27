# Excel Tool Sequences (74 tools)

## Workbook Lifecycle (5)
| Tool | Purpose |
|------|---------|
| `create_workbook` | New empty workbook |
| `open_workbook` | Open existing xlsx |
| `save_workbook` | Save to disk |
| `close_workbook` | Free memory |
| `configure_workbook` | Calc mode, properties |

## Sheet Management (6)
| Tool | Purpose |
|------|---------|
| `list_sheets` | All sheet names |
| `get_sheet_dimensions` | Used range, rows, cols |
| `describe_workbook` | Overview + sample data |
| `add_sheet` | New worksheet |
| `rename_sheet` | Rename |
| `delete_sheet` | Remove |

## Reading (5)
| Tool | Purpose |
|------|---------|
| `read_sheet` | Read with range/pagination |
| `read_cell` | Value, type, formula |
| `search_cells` | Find by value/pattern |
| `sheet_to_csv` | Export as CSV |
| `read_cell_format` | Get formatting |

## Writing (7)
| Tool | Purpose |
|------|---------|
| `write_cells` | Batch write |
| `write_row` | Write rightward |
| `write_column` | Write downward |
| `write_rich_text` | Bold/italic/color runs |
| `write_json_rows` | JSON → rows with headers |
| `write_formula` | Regular, array, dynamic |
| `manage_cell` | Clear/format blank |

## Formatting (8)
| Tool | Purpose |
|------|---------|
| `set_cell_format` | Bold, colors, borders, alignment |
| `merge_cells` | Merge range |
| `set_row_column_format` | Entire row/col format |
| `set_dimensions` | Width, height |
| `freeze_panes` | Freeze for scrolling |
| `autofit_columns` | Auto-width |
| `set_visibility` | Hide/unhide |
| `set_sheet_settings` | Zoom, gridlines, tab color |

## Charts (10)
| Tool | Purpose |
|------|---------|
| `add_chart` | Bar/column/line/pie/scatter/area/doughnut |
| `add_waterfall_chart` | Financial waterfall |
| `add_funnel_chart` | Sales funnel |
| `add_treemap_chart` | Hierarchical |
| `add_sunburst_chart` | Multi-level hierarchy |
| `add_histogram_chart` | Distribution + Pareto |
| `add_box_whisker_chart` | Statistical |
| `add_map_chart` | Geographic |
| `add_sparkline` | Inline mini-chart |
| `add_chart_sheet` | Dedicated chart sheet |

## Data Features (7)
| Tool | Purpose |
|------|---------|
| `add_table` | Excel Table with autofilter |
| `add_conditional_format` | Color scales, data bars, icons |
| `add_data_validation` | Dropdowns, ranges |
| `add_pivot_table` | Summarize with grouping |
| `add_slicer` | Interactive pivot filter |
| `add_timeline` | Date-based filter |
| `add_form_control` | Button, checkbox, dropdown |

## Structure (6)
| Tool | Purpose |
|------|---------|
| `modify_rows` | Insert/delete rows |
| `modify_columns` | Insert/delete columns |
| `group` | Outline grouping |
| `manage_autofilter` | Column filtering |
| `manage_defined_names` | Named ranges |
| `add_link` | URLs or sheet refs |
