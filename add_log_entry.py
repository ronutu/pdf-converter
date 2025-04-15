import sqlite3


def add_log_entry():
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    # Create the logs table if it doesn't exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            message TEXT
        )
    """
    )

    # Insert a test log entry
    cursor.execute(
        """
        INSERT INTO logs (message) 
        VALUES ('Test log entry')
    """
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    add_log_entry()
