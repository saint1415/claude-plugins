# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Pre-Tool Use Hook - Security validation before tool execution.
Blocks dangerous commands and protects sensitive files.

Windows Compatible.
"""

import json
import sys
import re
from pathlib import Path
from datetime import datetime

# Dangerous command patterns
DANGEROUS_PATTERNS = [
    r'rm\s+(-rf|-fr|--recursive.*--force|--force.*--recursive)',
    r'rm\s+.*[/\\]$',  # rm on root paths
    r'rmdir\s+/s\s+/q',  # Windows recursive delete
    r'del\s+/s\s+/q',  # Windows delete
    r'format\s+[a-z]:',  # Format drive
    r'rd\s+/s\s+/q',  # Windows remove directory
]

# Protected file patterns
PROTECTED_FILES = [
    r'\.env$',
    r'\.env\.local$',
    r'\.env\.production$',
    r'credentials',
    r'secrets?\.ya?ml$',
    r'\.pem$',
    r'\.key$',
]

def is_dangerous_command(command: str) -> tuple[bool, str]:
    """Check if command matches dangerous patterns."""
    command_lower = command.lower()
    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, command_lower):
            return True, f"Blocked dangerous command pattern: {pattern}"
    return False, ""

def is_protected_file(file_path: str) -> tuple[bool, str]:
    """Check if file is protected."""
    for pattern in PROTECTED_FILES:
        if re.search(pattern, file_path.lower()):
            # Allow .env.example and .env.sample
            if '.example' in file_path.lower() or '.sample' in file_path.lower():
                return False, ""
            return True, f"Blocked access to protected file: {file_path}"
    return False, ""

def log_event(event_type: str, data: dict, blocked: bool = False):
    """Log the event to logs directory."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    log_file = log_dir / "pre_tool_use.json"

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "blocked": blocked,
        "data": data
    }

    # Append to log file
    logs = []
    if log_file.exists():
        try:
            logs = json.loads(log_file.read_text())
        except:
            logs = []

    logs.append(log_entry)

    # Keep last 1000 entries
    logs = logs[-1000:]
    log_file.write_text(json.dumps(logs, indent=2))

def main():
    # Read input from stdin
    try:
        input_data = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        sys.exit(0)  # Allow if can't parse

    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})

    # Check Bash commands
    if tool_name == "Bash":
        command = tool_input.get("command", "")
        is_dangerous, reason = is_dangerous_command(command)
        if is_dangerous:
            log_event("bash_blocked", {"command": command, "reason": reason}, blocked=True)
            print(f"BLOCKED: {reason}")
            sys.exit(2)  # Exit code 2 blocks the tool

    # Check file access
    if tool_name in ["Read", "Write", "Edit"]:
        file_path = tool_input.get("file_path", "")
        is_protected, reason = is_protected_file(file_path)
        if is_protected:
            log_event("file_blocked", {"file": file_path, "reason": reason}, blocked=True)
            print(f"BLOCKED: {reason}")
            sys.exit(2)

    # Log allowed operation
    log_event("allowed", {"tool": tool_name, "input": tool_input})
    sys.exit(0)  # Allow

if __name__ == "__main__":
    main()
