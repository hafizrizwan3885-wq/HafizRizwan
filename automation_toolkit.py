"""Validate and execute explicit, shell-free automation workflows."""
import argparse
import json
import subprocess
from pathlib import Path

def validate(workflow):
    if not isinstance(workflow, list) or not workflow:
        raise ValueError("Expected a nonempty list of steps")
    for step in workflow:
        if not isinstance(step, dict):
            raise ValueError("Expected step object")
        argv = step.get("argv")
        if not isinstance(argv, list) or not argv or any(not isinstance(x, str) or not x for x in argv):
            raise ValueError("Expected nonempty argv strings")
        timeout = step.get("timeout", 30)
        if type(timeout) is not int or not 1 <= timeout <= 3600:
            raise ValueError("Timeout must be 1–3600 seconds")
    return workflow

def run(workflow):
    for step in validate(workflow):
        subprocess.run(step["argv"], shell=False, check=True, timeout=step.get("timeout", 30))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workflow", type=Path)
    parser.add_argument("--execute", action="store_true", help="Execute trusted workflow; default validates only")
    args = parser.parse_args()
    workflow = validate(json.loads(args.workflow.read_text(encoding="utf-8")))
    if args.execute:
        run(workflow)
    else:
        print(f"Validated {len(workflow)} steps; nothing executed.")

if __name__ == "__main__":
    main()
