from pathlib import Path

from app.db import create_driver


def main():
    schema_path = Path(__file__).resolve().parent.parent / "schema.cypher"
    schema = schema_path.read_text(encoding="utf-8")

    statements = [
        statement.strip()
        for statement in schema.split(";")
        if statement.strip()
    ]

    driver = create_driver()

    try:
        with driver.session() as session:
            for statement in statements:
                session.run(statement).consume()

        print("SUCCESS: Schema applied to CognoDB!")

    except Exception as e:
        print(f"SCHEMA FAILED: {e}")

    finally:
        driver.close()


if __name__ == "__main__":
    main()