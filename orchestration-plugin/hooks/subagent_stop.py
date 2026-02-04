# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Subagent Stop Hook - Triggered when a sub-agent completes its work.
Logs completion and optionally announces via TTS.

Windows Compatible.
"""

import json
import sys
from pathlib import Path
from datetime import datetime

def log_event(data: dict):
    """Log subagent completion."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    log_file = log_dir / "subagent_stop.json"

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        **data
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

def announce_completion(agent_id: str, summary: str):
    """Announce completion (optional TTS)."""
    # Check if TTS is enabled via environment variable
    import os
    if os.environ.get("ENABLE_TTS", "").lower() == "true":
        try:
            import pyttsx3
            engine = pyttsx3.init()
            engine.say(f"Agent {agent_id[:8]} completed: {summary[:50]}")
            engine.runAndWait()
        except:
            pass  # TTS not available

    # Always print
    print(f"✓ Agent {agent_id[:8]} completed: {summary}")

def main():
    try:
        input_data = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        input_data = {}

    agent_id = input_data.get("agent_id", "unknown")
    task_description = input_data.get("task_description", "")
    result_summary = input_data.get("result_summary", "Task completed")

    log_event({
        "agent_id": agent_id,
        "task": task_description,
        "summary": result_summary
    })

    # Check for --notify flag
    if "--notify" in sys.argv:
        announce_completion(agent_id, result_summary)

    sys.exit(0)

if __name__ == "__main__":
    main()
