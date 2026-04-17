# LangGraph Example

This repository contains a sample LangGraph-based application for building and running approval workflows. It demonstrates how to define state transitions, manage multi-step review flows, and integrate with external services in a minimal Python application.

## Overview

The project includes:
- `main.py`: application entry point
- `apps/agents.py`: agent integrations and workflow logic
- `apps/graph.py`: graph definitions and workflow state modeling
- `apps/state.py`: state management helpers
- `compose.yaml` and `dockerfile`: container orchestration and runtime setup

## Current Capabilities

- Create and run workflow graphs
- Manage approval states and transitions
- Execute actions based on user decisions

## Running the Project

Use Docker Compose to run the app in the contained environment:

```bash
docker compose run --rm langgraph-app
```

## Follow-up Enhancements

1. Gmail API integration and send-on-approve
   - Connect the workflow to Gmail API for email delivery
   - Add an approval step that triggers email sending only after review approval
   - Support OAuth2 authorization and secure token handling

2. Multi-role approval
   - Enable multiple reviewers to approve or reject a request
   - Support sequential and parallel review paths
   - Track approval status per role and require consensus before advancing

3. Auto remind
   - Send automated reminder notifications for pending approvals
   - Schedule reminders based on approval deadlines or inactivity
   - Provide configurable retry and escalation policies
