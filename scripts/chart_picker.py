#!/usr/bin/env python3
"""Recommend chart type based on data characteristics."""
import json, sys

def recommend(data):
    cols = data.get("columns", 1)
    rows = data.get("rows", 1)
    has_time = data.get("has_time_axis", False)
    categories = data.get("category_count", 1)
    if has_time:
        return {"chart": "line", "reason": "Time series → line chart"}
    if categories <= 6 and cols == 1:
        return {"chart": "pie", "reason": "Few categories, single measure → pie"}
    if categories > 6:
        return {"chart": "bar", "reason": "Many categories → horizontal bar"}
    return {"chart": "column", "reason": "Category comparison → column chart"}

if __name__ == "__main__":
    print(json.dumps(recommend(json.loads(sys.argv[1])), indent=2))
