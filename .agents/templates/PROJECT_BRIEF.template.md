---
description: Schema definition for the core $PROJECT_BRIEF object holding intake parameters
---

# PROJECT BRIEF SCHEMA

During `/project-init` (Step 0 Intake), the agent MUST compile the user's answers into exactly this JSON schema in memory before proceeding to scaffolding. This robust structure guarantees no details are lost across initialization steps.

```json
{
  "name": "Project Name",
  "tagline": "A short, one-sentence description of the product",
  "density": "lean | startup",
  "monetization": "e.g., freemium, B2B SaaS, ads",
  "persona": "Target audience description",
  "detected_state": "fresh | legacy | blueprint",
  "features": [
    "Core feature 1",
    "Core feature 2",
    "..."
  ]
}
```