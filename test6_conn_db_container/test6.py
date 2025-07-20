import psycopg2

DB_HOST = "pgsql_container"  #For Docker Desktop (macOS/Windows) Gemini Response
DB_NAME = "praveen"
DB_USER = "postgres"
DB_PASSWORD = "Praveen1#"


def connect_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except psycopg2.Error as e:
        print("❌ Could not connect to the database.")
        print("Error:", e)
        return None
def create_table_if_not_exists(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS names (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL
            );
        """)
        conn.commit()
        cursor.close()
        print("✅ Table 'names' is ready.\n")
    except psycopg2.Error as e:
        conn.rollback()
        print("❌ Error creating table:", e)



def add_name(conn, name):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO names (name) VALUES (%s);", (name,))
        conn.commit()
        print(f"✅ Name '{name}' added successfully.\n")
        cursor.close()
    except psycopg2.Error as e:
        conn.rollback()                                                                #Reseting the failed transaction
        print("❌ Error inserting name:", e)



def show_all_names(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM names;")
        rows = cursor.fetchall()
        print("\n📋 List of all names:")
        print("-" * 30)
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]}")
        print("-" * 30 + "\n")
        cursor.close()
    except psycopg2.Error as e:
        print("❌ Error fetching names:", e)


def main():
    conn = connect_db()
    if not conn:
        return

    # 🔧 Ensure table exists
    create_table_if_not_exists(conn)

    while True:
        print("Choose an option:")
        print("1. Add name")
        print("2. Show all names")
        print("3. Quit")
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            name = input("Enter name to add: ").strip()
            if name:
                add_name(conn, name)
            else:
                print("❌ Name cannot be empty.\n")
        elif choice == "2":
            show_all_names(conn)
        elif choice == "3":
            print("👋 Goodbye!")
            conn.close()
            break
        else:
            print("❌ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()