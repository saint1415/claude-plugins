# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Post-Tool Use Hook - Logging and validation after tool execution.
Runs code quality checks on modified files.

Windows Compatible.
"""

import json
import sys
import subprocess
from pathlib import Path
from datetime import datetime

def log_event(event_type: str, data: dict):
    """Log the event to logs directory."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    log_file = log_dir / "post_tool_use.json"

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

def run_python_validation(file_path: str) -> dict:
    """Run Python validation (ruff, syntax check)."""
    results = {"file": file_path, "checks": []}

    # Syntax check
    try:
        result = subprocess.run(
            ["python", "-m", "py_compile", file_path],
            capture_output=True,
            text=True,
            timeout=30
        )
        results["checks"].append({
            "check": "syntax",
            "passed": result.returncode == 0,
            "output": result.stderr if result.returncode != 0 else "OK"
        })
    except Exception as e:
        results["checks"].append({"check": "syntax", "passed": False, "error": str(e)})

    # Ruff check (if available)
    try:
        result = subprocess.run(
            ["python", "-m", "ruff", "check", file_path],
            capture_output=True,
            text=True,
            timeout=30
        )
        results["checks"].append({
            "check": "ruff",
            "passed": result.returncode == 0,
            "output": result.stdout or "OK"
        })
    except FileNotFoundError:
        results["checks"].append({"check": "ruff", "skipped": True, "reason": "ruff not installed"})
    except Exception as e:
        results["checks"].append({"check": "ruff", "passed": False, "error": str(e)})

    return results

def run_js_validation(file_path: str) -> dict:
    """Run JavaScript/TypeScript validation."""
    results = {"file": file_path, "checks": []}

    # Node syntax check
    try:
        result = subprocess.run(
            ["node", "--check", file_path],
            capture_output=True,
            text=True,
            timeout=30
        )
        results["checks"].append({
            "check": "syntax",
            "passed": result.returncode == 0,
            "output": result.stderr if result.returncode != 0 else "OK"
        })
    except FileNotFoundError:
        results["checks"].append({"check": "syntax", "skipped": True, "reason": "node not found"})
    except Exception as e:
        results["checks"].append({"check": "syntax", "passed": False, "error": str(e)})

    return results

def main():
    try:
        input_data = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        sys.exit(0)

    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})
    tool_output = input_data.get("tool_output", {})

    # Log the tool use
    log_event("tool_completed", {
        "tool": tool_name,
        "input": tool_input,
        "success": tool_output.get("success", True)
    })

    # Run validation for file modifications
    if tool_name in ["Write", "Edit"]:
        file_path = tool_input.get("file_path", "")

        if file_path.endswith(".py"):
            validation = run_python_validation(file_path)
            log_event("python_validation", validation)

            # Print validation results
            for check in validation.get("checks", []):
                if not check.get("passed", True) and not check.get("skipped", False):
                    print(f"⚠️ {check['check']}: {check.get('output', check.get('error', 'Failed'))}")

        elif file_path.endswith((".js", ".ts", ".jsx", ".tsx")):
            validation = run_js_validation(file_path)
            log_event("js_validation", validation)

    sys.exit(0)

if __name__ == "__main__":
    main()
