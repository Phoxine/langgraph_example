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

## Example Output

```bash
What email do you need?
> a email for inviting friend to come join the party next saturday night

===== AI GENERATED EMAIL =====

Subject: Join Us for a Fun Evening!

Hi [Friend's Name],

I hope this message finds you well! I’m reaching out to invite you to a party I’m hosting next Saturday night at my place. It will be a great opportunity to unwind, catch up, and enjoy some good food and music.

Date: [Insert Date]
Time: [Insert Start Time]
Location: [Your Address]

Please let me know if you can make it. I would love to see you there and share a fun evening together!

Looking forward to your reply.

Best,  
[Your Name]  
[Your Contact Information]  

Approve this email? (y/n): y

===== FINAL EMAIL =====

Subject: Join Us for a Fun Evening!

Hi [Friend's Name],

I hope this message finds you well! I’m reaching out to invite you to a party I’m hosting next Saturday night at my place. It will be a great opportunity to unwind, catch up, and enjoy some good food and music.

Date: [Insert Date]
Time: [Insert Start Time]
Location: [Your Address]

Please let me know if you can make it. I would love to see you there and share a fun evening together!

Looking forward to your reply.

Best,  
[Your Name]  
[Your Contact Information]
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
