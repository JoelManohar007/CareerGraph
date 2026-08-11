from app.db import create_driver


def main():
    driver = create_driver()

    try:
        with driver.session() as session:
            result = session.run(
                """
                MATCH (n)
                RETURN labels(n)[0] AS type, count(n) AS count
                ORDER BY type
                """
            )

            print("\n=== NODE COUNTS ===")
            for record in result:
                print(f"{record['type']}: {record['count']}")

            result = session.run(
                """
                MATCH ()-[r]->()
                RETURN type(r) AS relationship, count(r) AS count
                ORDER BY relationship
                """
            )

            print("\n=== RELATIONSHIP COUNTS ===")
            for record in result:
                print(f"{record['relationship']}: {record['count']}")

    finally:
        driver.close()


if __name__ == "__main__":
    main()