# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Stop Hook - Runs when agent completes. Used for self-validation.

Windows Compatible.
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime

def log_event(event_type: str, data: dict):
    """Log the event."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    log_file = log_dir / "stop.json"

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "data": data
    }

    logs = []
    if log_file.exists():
        try:
            logs = json.loads(log_file.read_text())
        except:
            logs = []

    logs.append(log_entry)
    logs = logs[-1000:]
    log_file.write_text(json.dumps(logs, indent=2))

def validate_file_exists(file_pattern: str, directory: str = ".") -> tuple[bool, str]:
    """Check if a file matching pattern exists."""
    dir_path = Path(directory)
    if not dir_path.exists():
        return False, f"Directory not found: {directory}"

    # Simple glob matching
    matches = list(dir_path.glob(file_pattern))
    if matches:
        return True, f"Found: {matches[0]}"
    return False, f"No file matching '{file_pattern}' in {directory}"

def validate_file_contains(file_path: str, required_content: list[str]) -> tuple[bool, list[str]]:
    """Check if file contains required content."""
    path = Path(file_path)
    if not path.exists():
        return False, [f"File not found: {file_path}"]

    content = path.read_text()
    missing = []

    for required in required_content:
        if required not in content:
            missing.append(required)

    if missing:
        return False, missing
    return True, []

def main():
    try:
        input_data = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        input_data = {}

    stop_reason = input_data.get("stop_reason", "unknown")

    log_event("agent_stopped", {
        "reason": stop_reason,
        "cwd": os.getcwd()
    })

    # Check for validation instructions in environment or args
    # This hook can be extended to read validation rules

    # Example validation (customize as needed):
    # validation_rules = os.environ.get("VALIDATION_RULES", "")
    # if validation_rules:
    #     rules = json.loads(validation_rules)
    #     for rule in rules:
    #         if rule["type"] == "file_exists":
    #             passed, msg = validate_file_exists(rule["pattern"], rule.get("dir", "."))
    #             if not passed:
    #                 print(f"Validation failed: {msg}")
    #                 sys.exit(2)

    print("✓ Agent completed successfully")
    sys.exit(0)

if __name__ == "__main__":
    main()
