# Find job roles that match a user's existing skills.
CAREER_RECOMMENDATIONS = """
MATCH (u:User {id: $user_id})-[:HAS_SKILL]->(s:Skill)
MATCH (s)-[:REQUIRED_FOR]->(j:Job)
WITH u, j, count(DISTINCT s) AS matching_skills
MATCH (j)<-[:REQUIRED_FOR]-(required:Skill)
WITH u, j, matching_skills, count(DISTINCT required) AS total_required
RETURN
    j.id AS job_id,
    j.title AS job_title,
    matching_skills,
    total_required,
    round(100.0 * matching_skills / total_required) AS match_percentage
ORDER BY match_percentage DESC, matching_skills DESC
"""


# Find skills a user is missing for a selected job.
MISSING_SKILLS = """
MATCH (u:User {id: $user_id})
MATCH (j:Job {id: $job_id})
MATCH (required:Skill)-[:REQUIRED_FOR]->(j)
OPTIONAL MATCH (u)-[:HAS_SKILL]->(user_skill:Skill)
WHERE user_skill.id = required.id
WITH required, user_skill
WHERE user_skill IS NULL
RETURN
    required.id AS skill_id,
    required.name AS skill_name,
    required.category AS category
ORDER BY required.name
"""


# Multi-hop career exploration:
# User -> Skill -> Job -> Technology -> Project
CAREER_PATH = """
MATCH (u:User {id: $user_id})-[:HAS_SKILL]->(s:Skill)
MATCH (s)-[:REQUIRED_FOR]->(j:Job)
MATCH (j)-[:USES_TECHNOLOGY]->(t:Technology)
MATCH (p:Project)-[:BUILT_WITH]->(t)
RETURN DISTINCT
    u.name AS user_name,
    s.name AS skill,
    j.title AS job,
    t.name AS technology,
    p.name AS project
ORDER BY job, technology, project
"""


# Search across jobs, skills, technologies and projects.
SEARCH = """
OPTIONAL MATCH (j:Job)
WHERE toLower(j.title) CONTAINS toLower($term)
OPTIONAL MATCH (s:Skill)
WHERE toLower(s.name) CONTAINS toLower($term)
OPTIONAL MATCH (t:Technology)
WHERE toLower(t.name) CONTAINS toLower($term)
OPTIONAL MATCH (p:Project)
WHERE toLower(p.name) CONTAINS toLower($term)
RETURN
    collect(DISTINCT {
        type: 'Job',
        id: j.id,
        name: j.title
    }) +
    collect(DISTINCT {
        type: 'Skill',
        id: s.id,
        name: s.name
    }) +
    collect(DISTINCT {
        type: 'Technology',
        id: t.id,
        name: t.name
    }) +
    collect(DISTINCT {
        type: 'Project',
        id: p.id,
        name: p.name
    }) AS results
"""