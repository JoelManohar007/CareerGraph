# CareerGraph

CareerGraph is a graph-powered career exploration application built using Flask and CognoDB.

## What it does

CareerGraph helps users discover suitable career paths based on their existing skills.

It can:

- Recommend suitable job roles
- Show skill match percentages
- Identify missing skills
- Explore career connections
- Search jobs, skills, technologies and projects

## Technology

- Python
- Flask
- HTML
- CSS
- JavaScript
- CognoDB
- Cypher
- Neo4j Python Driver

## Graph Model

### Nodes

- User
- Skill
- Job
- Technology
- Project

### Relationships

- User HAS_SKILL Skill
- Skill REQUIRED_FOR Job
- Job USES_TECHNOLOGY Technology
- Project BUILT_WITH Technology

## How the application works

User
→ Skills
→ Job Roles
→ Technologies
→ Projects

The application uses graph traversal to discover these connections.

## Running the project

Install dependencies:

```text
pip install -r requirements.txt