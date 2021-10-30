import sqlite3
import json
from models import Employee

EMPLOYEES = []

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:

        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    # Get the id value of the last employee in the list
        max_id = EMPLOYEES[-1]["id"]

        # Add 1 to whatever that number is
        new_id = max_id + 1

        # Add an `id` property to the employee dictionary
        employee["id"] = new_id

    # Add the employee dictionary to the list
        EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
        return employee


def get_all_employees():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        """)

        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

          
            employee = Employee(row['id'], row['name'], row['address'],
                            row['location_id']
                        )

            employees.append(employee.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(employees)


def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
    db_cursor.execute("""
            SELECT
                e.id,
                e.name,
                e.address,
                e.location_id
            FROM employee e
            WHERE e.id = ?
            """, ( id, ))

        # Load the single result into memory
    data = db_cursor.fetchone()

    employee = Employee(data['id'], data['name'], data['address'],
                            data['loaction_id'])

    return json.dumps(employee.__dict__)
