# CampusMate — Autonomous Engineering Study Hub

## What this updated starter includes
- Multiple engineering departments: CSE, AIML, ECE, EEE, Mechanical, Civil, IT, Chemical, Biomedical
- Resource library filters for department, semester, resource type, and search
- Save resources for the current session
- Mixed-discipline practice quiz with scoring and explanations
- Lab preparation checklist and department-specific sample viva prompts
- Admin form to add resources for the current session
- Premium-plan preview (no real payments)

## Run
Install Python 3.10+ and run:
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy using a tablet browser
1. Download and extract the ZIP.
2. Upload `app.py` and `requirements.txt` to a GitHub repository.
3. Open https://share.streamlit.io/ and connect GitHub.
4. Create an app, choose the repository and `app.py`, then deploy.

Official documentation: https://docs.streamlit.io/deploy/streamlit-community-cloud

## Next implementation step
Choose one autonomous college as the pilot and gather:
- official regulation/year (for example, 2023 regulation)
- department names and semester structure
- course codes and official subject titles
- authorized notes/question papers/lab material

Then replace the sample resources with verified content. Autonomous syllabi vary by college, so this app deliberately does not claim the sample topics are official.

## Limitations
This is a prototype, not production-ready:
- no permanent database
- no real user login or roles
- saved items/custom resources only last for the current app session
- no AI API integration
- no payment integration or subscription enforcement
- use only original, licensed, or permissioned content
- never commit API keys, passwords, or payment secrets to GitHub
