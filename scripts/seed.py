from app.db import create_driver


USERS = [
    {"id": "U001", "name": "Joel", "experience_level": "Fresher"},
    {"id": "U002", "name": "Ananya", "experience_level": "Fresher"},
    {"id": "U003", "name": "Rahul", "experience_level": "Junior"},
    {"id": "U004", "name": "Priya", "experience_level": "Junior"},
    {"id": "U005", "name": "Arjun", "experience_level": "Fresher"},
]

SKILLS = [
    {"id": "S001", "name": "Python", "category": "Programming"},
    {"id": "S002", "name": "Java", "category": "Programming"},
    {"id": "S003", "name": "JavaScript", "category": "Programming"},
    {"id": "S004", "name": "SQL", "category": "Database"},
    {"id": "S005", "name": "React", "category": "Frontend"},
    {"id": "S006", "name": "HTML/CSS", "category": "Frontend"},
    {"id": "S007", "name": "FastAPI", "category": "Backend"},
    {"id": "S008", "name": "Flask", "category": "Backend"},
    {"id": "S009", "name": "Machine Learning", "category": "AI"},
    {"id": "S010", "name": "OpenCV", "category": "Computer Vision"},
    {"id": "S011", "name": "Data Structures", "category": "Computer Science"},
    {"id": "S012", "name": "Docker", "category": "DevOps"},
    {"id": "S013", "name": "Git", "category": "Development Tools"},
    {"id": "S014", "name": "REST APIs", "category": "Backend"},
    {"id": "S015", "name": "PostgreSQL", "category": "Database"},
]

JOBS = [
    {
        "id": "J001",
        "title": "Python Developer",
        "experience_level": "Entry Level",
        "description": "Build backend applications and automation using Python."
    },
    {
        "id": "J002",
        "title": "Backend Developer",
        "experience_level": "Entry Level",
        "description": "Build APIs and server-side applications."
    },
    {
        "id": "J003",
        "title": "Full Stack Developer",
        "experience_level": "Entry Level",
        "description": "Build complete web applications across frontend and backend."
    },
    {
        "id": "J004",
        "title": "AI/ML Engineer",
        "experience_level": "Entry Level",
        "description": "Build machine learning solutions and intelligent applications."
    },
    {
        "id": "J005",
        "title": "Computer Vision Engineer",
        "experience_level": "Entry Level",
        "description": "Develop image and video processing systems."
    },
    {
        "id": "J006",
        "title": "Software Engineer",
        "experience_level": "Entry Level",
        "description": "Design and develop reliable software systems."
    },
    {
        "id": "J007",
        "title": "Data Analyst",
        "experience_level": "Entry Level",
        "description": "Analyze data and produce useful business insights."
    },
    {
        "id": "J008",
        "title": "Frontend Developer",
        "experience_level": "Entry Level",
        "description": "Build responsive and interactive web interfaces."
    },
]

TECHNOLOGIES = [
    {"id": "T001", "name": "Python", "category": "Programming"},
    {"id": "T002", "name": "React", "category": "Frontend"},
    {"id": "T003", "name": "FastAPI", "category": "Backend"},
    {"id": "T004", "name": "Flask", "category": "Backend"},
    {"id": "T005", "name": "PostgreSQL", "category": "Database"},
    {"id": "T006", "name": "Docker", "category": "DevOps"},
    {"id": "T007", "name": "TensorFlow", "category": "AI"},
    {"id": "T008", "name": "OpenCV", "category": "Computer Vision"},
    {"id": "T009", "name": "Git", "category": "Development Tools"},
    {"id": "T010", "name": "Node.js", "category": "Backend"},
]

PROJECTS = [
    {
        "id": "P001",
        "name": "AI Chatbot",
        "difficulty": "Intermediate",
        "description": "A conversational assistant using Python and machine learning."
    },
    {
        "id": "P002",
        "name": "Face Detection System",
        "difficulty": "Intermediate",
        "description": "Detect faces from images and video using computer vision."
    },
    {
        "id": "P003",
        "name": "E-Commerce Platform",
        "difficulty": "Advanced",
        "description": "A complete online shopping web application."
    },
    {
        "id": "P004",
        "name": "Traffic Detection System",
        "difficulty": "Advanced",
        "description": "Detect and analyze traffic using computer vision."
    },
    {
        "id": "P005",
        "name": "Job Portal",
        "difficulty": "Intermediate",
        "description": "A platform connecting candidates with job opportunities."
    },
    {
        "id": "P006",
        "name": "Expense Tracker",
        "difficulty": "Beginner",
        "description": "Track personal expenses through a web application."
    },
    {
        "id": "P007",
        "name": "Recommendation Engine",
        "difficulty": "Advanced",
        "description": "Recommend items based on user preferences."
    },
    {
        "id": "P008",
        "name": "Inventory Management System",
        "difficulty": "Intermediate",
        "description": "Manage products, stock and inventory records."
    },
]


USER_SKILLS = {
    "U001": ["S001", "S004", "S009", "S010", "S011", "S013"],
    "U002": ["S002", "S003", "S004", "S005", "S006", "S013"],
    "U003": ["S001", "S004", "S007", "S012", "S013", "S014"],
    "U004": ["S003", "S005", "S006", "S004", "S013"],
    "U005": ["S001", "S004", "S011", "S014", "S015"],
}


JOB_SKILLS = {
    "J001": ["S001", "S004", "S011", "S013"],
    "J002": ["S001", "S004", "S007", "S014", "S015"],
    "J003": ["S001", "S003", "S004", "S005", "S006", "S014"],
    "J004": ["S001", "S004", "S009", "S011"],
    "J005": ["S001", "S009", "S010", "S011"],
    "J006": ["S001", "S002", "S003", "S004", "S011", "S013"],
    "J007": ["S004", "S011", "S015"],
    "J008": ["S003", "S005", "S006", "S013"],
}


JOB_TECHNOLOGIES = {
    "J001": ["T001", "T004", "T009"],
    "J002": ["T001", "T003", "T005", "T006", "T009"],
    "J003": ["T001", "T002", "T003", "T005", "T009"],
    "J004": ["T001", "T007", "T009"],
    "J005": ["T001", "T007", "T008", "T009"],
    "J006": ["T001", "T002", "T005", "T009", "T010"],
    "J007": ["T001", "T005", "T009"],
    "J008": ["T002", "T010", "T009"],
}


PROJECT_TECHNOLOGIES = {
    "P001": ["T001", "T004", "T007"],
    "P002": ["T001", "T008"],
    "P003": ["T002", "T005", "T010"],
    "P004": ["T001", "T007", "T008"],
    "P005": ["T001", "T003", "T005", "T002"],
    "P006": ["T001", "T004", "T005"],
    "P007": ["T001", "T007", "T005"],
    "P008": ["T001", "T003", "T005"],
}


def seed_database():
    driver = create_driver()

    try:
        with driver.session() as session:

            for user in USERS:
                session.run(
                    """
                    MERGE (u:User {id: $id})
                    SET u.name = $name,
                        u.experience_level = $experience_level
                    """,
                    **user
                )

            for skill in SKILLS:
                session.run(
                    """
                    MERGE (s:Skill {id: $id})
                    SET s.name = $name,
                        s.category = $category
                    """,
                    **skill
                )

            for job in JOBS:
                session.run(
                    """
                    MERGE (j:Job {id: $id})
                    SET j.title = $title,
                        j.experience_level = $experience_level,
                        j.description = $description
                    """,
                    **job
                )

            for technology in TECHNOLOGIES:
                session.run(
                    """
                    MERGE (t:Technology {id: $id})
                    SET t.name = $name,
                        t.category = $category
                    """,
                    **technology
                )

            for project in PROJECTS:
                session.run(
                    """
                    MERGE (p:Project {id: $id})
                    SET p.name = $name,
                        p.difficulty = $difficulty,
                        p.description = $description
                    """,
                    **project
                )

            for user_id, skill_ids in USER_SKILLS.items():
                for skill_id in skill_ids:
                    session.run(
                        """
                        MATCH (u:User {id: $user_id})
                        MATCH (s:Skill {id: $skill_id})
                        MERGE (u)-[:HAS_SKILL]->(s)
                        """,
                        user_id=user_id,
                        skill_id=skill_id
                    )

            for job_id, skill_ids in JOB_SKILLS.items():
                for skill_id in skill_ids:
                    session.run(
                        """
                        MATCH (s:Skill {id: $skill_id})
                        MATCH (j:Job {id: $job_id})
                        MERGE (s)-[:REQUIRED_FOR]->(j)
                        """,
                        skill_id=skill_id,
                        job_id=job_id
                    )

            for job_id, technology_ids in JOB_TECHNOLOGIES.items():
                for technology_id in technology_ids:
                    session.run(
                        """
                        MATCH (j:Job {id: $job_id})
                        MATCH (t:Technology {id: $technology_id})
                        MERGE (j)-[:USES_TECHNOLOGY]->(t)
                        """,
                        job_id=job_id,
                        technology_id=technology_id
                    )

            for project_id, technology_ids in PROJECT_TECHNOLOGIES.items():
                for technology_id in technology_ids:
                    session.run(
                        """
                        MATCH (p:Project {id: $project_id})
                        MATCH (t:Technology {id: $technology_id})
                        MERGE (p)-[:BUILT_WITH]->(t)
                        """,
                        project_id=project_id,
                        technology_id=technology_id
                    )

        print("SUCCESS: Seed data loaded into CognoDB!")

    finally:
        driver.close()


if __name__ == "__main__":
    seed_database()