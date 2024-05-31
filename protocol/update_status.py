import mysql.connector

def update_test_statuses():
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="6810",
      database="schema_1"
  )
    cursor = connection.cursor()

    # Update status based on testdate
    query = """
    UPDATE date_table
    SET status = 
        CASE WHEN date = CURDATE() THEN 'Today'
            WHEN date < CURDATE() THEN 'Elapsed'
            ELSE 'Active'
        END;
    """
    cursor.execute(query)

    # Commit changes and close connection
    connection.commit()
    connection.close()

if __name__ == "__main__":
    update_test_statuses()
    print("Statuses updated successfully!")

