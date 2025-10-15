# agents/efficiency_analyzer.py

from typing import Dict, Any
import json
import os

def update_dashboard(metrics: Dict[str, Any], output_path: str = "/app/dashboard/metrics.json") -> None:
    """
    Update the dashboard data with new efficiency metrics.

    Args:
        metrics (Dict[str, Any]): Dictionary of computed metrics.
        output_path (str): Path to the dashboard data file.
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(metrics, f, indent=2)
        print(f"[update_dashboard] Metrics written to {output_path}")
    except Exception as e:
        print(f"[update_dashboard] Failed to update dashboard: {e}")
        raise