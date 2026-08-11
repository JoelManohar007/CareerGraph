from app.db import create_driver
from app.queries import (
    CAREER_RECOMMENDATIONS,
    MISSING_SKILLS,
    CAREER_PATH,
    SEARCH,
)


def main():
    driver = create_driver()

    try:
        with driver.session() as session:

            print("\n=== 1. CAREER RECOMMENDATIONS ===")

            result = session.run(
                CAREER_RECOMMENDATIONS,
                user_id="U001",
            )

            for record in result:
                print(
                    f"{record['job_title']} | "
                    f"Match: {record['match_percentage']}% | "
                    f"{record['matching_skills']}/{record['total_required']} skills"
                )

            print("\n=== 2. MISSING SKILLS ===")

            result = session.run(
                MISSING_SKILLS,
                user_id="U001",
                job_id="J003",
            )

            for record in result:
                print(
                    f"{record['skill_name']} "
                    f"({record['category']})"
                )

            print("\n=== 3. MULTI-HOP CAREER PATH ===")

            result = session.run(
                CAREER_PATH,
                user_id="U001",
            )

            count = 0

            for record in result:
                print(
                    f"{record['skill']} → "
                    f"{record['job']} → "
                    f"{record['technology']} → "
                    f"{record['project']}"
                )

                count += 1

                if count >= 10:
                    break

            print("\n=== 4. SEARCH ===")

            result = session.run(
                SEARCH,
                term="Python",
            )

            for record in result:
                for item in record["results"]:
                    if item["id"] is not None:
                        print(
                            f"{item['type']}: "
                            f"{item['name']}"
                        )

    finally:
        driver.close()


if __name__ == "__main__":
    main()