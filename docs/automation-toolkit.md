# Universal AI Automation Toolkit — initial prototype

A dependency-free Python 3 command workflow validator and runner. It defaults to validation only and executes argument arrays without a shell when explicitly requested.

Example workflow JSON: `[{"argv":["python","--version"],"timeout":10}]`

Validate: `python automation_toolkit.py workflow.json`

Execute: `python automation_toolkit.py workflow.json --execute`

Tests: `python -m unittest -v`

Security: execute only trusted workflows. Shell-free execution is not sandboxing; programs retain the current user's permissions. This prototype does not yet implement MCP, browser automation, or video editing. No adoption or external contribution claims are made.
