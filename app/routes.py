from flask import Blueprint, jsonify, render_template, request

from app.db import create_driver
from app.queries import (
    CAREER_RECOMMENDATIONS,
    MISSING_SKILLS,
    CAREER_PATH,
    SEARCH,
)

main = Blueprint("main", __name__)


@main.get("/")
def index():
    return render_template("index.html")


@main.get("/api/users")
def users():
    driver = create_driver()

    try:
        with driver.session() as session:
            result = session.run(
                """
                MATCH (u:User)
                RETURN u.id AS id, u.name AS name,
                       u.experience_level AS experience_level
                ORDER BY u.name
                """
            )

            return jsonify([
                {
                    "id": record["id"],
                    "name": record["name"],
                    "experience_level": record["experience_level"],
                }
                for record in result
            ])

    finally:
        driver.close()


@main.get("/api/jobs")
def jobs():
    driver = create_driver()

    try:
        with driver.session() as session:
            result = session.run(
                """
                MATCH (j:Job)
                RETURN j.id AS id,
                       j.title AS title,
                       j.experience_level AS experience_level,
                       j.description AS description
                ORDER BY j.title
                """
            )

            return jsonify([
                {
                    "id": record["id"],
                    "title": record["title"],
                    "experience_level": record["experience_level"],
                    "description": record["description"],
                }
                for record in result
            ])

    finally:
        driver.close()


@main.get("/api/recommendations/<user_id>")
def recommendations(user_id):
    driver = create_driver()

    try:
        with driver.session() as session:
            result = session.run(
                CAREER_RECOMMENDATIONS,
                user_id=user_id,
            )

            return jsonify([
                {
                    "job_id": record["job_id"],
                    "job_title": record["job_title"],
                    "matching_skills": record["matching_skills"],
                    "total_required": record["total_required"],
                    "match_percentage": record["match_percentage"],
                }
                for record in result
            ])

    finally:
        driver.close()


@main.get("/api/missing-skills/<user_id>/<job_id>")
def missing_skills(user_id, job_id):
    driver = create_driver()

    try:
        with driver.session() as session:
            result = session.run(
                MISSING_SKILLS,
                user_id=user_id,
                job_id=job_id,
            )

            return jsonify([
                {
                    "skill_id": record["skill_id"],
                    "skill_name": record["skill_name"],
                    "category": record["category"],
                }
                for record in result
            ])

    finally:
        driver.close()


@main.get("/api/career-path/<user_id>")
def career_path(user_id):
    driver = create_driver()

    try:
        with driver.session() as session:
            result = session.run(
                CAREER_PATH,
                user_id=user_id,
            )

            return jsonify([
                {
                    "user_name": record["user_name"],
                    "skill": record["skill"],
                    "job": record["job"],
                    "technology": record["technology"],
                    "project": record["project"],
                }
                for record in result
            ])

    finally:
        driver.close()


@main.get("/api/search")
def search():
    term = request.args.get("q", "").strip()

    if not term:
        return jsonify([])

    driver = create_driver()

    try:
        with driver.session() as session:
            result = session.run(
                SEARCH,
                term=term,
            )

            results = []

            for record in result:
                for item in record["results"]:
                    if item["id"] is not None:
                        results.append(item)

            return jsonify(results)

    finally:
        driver.close()