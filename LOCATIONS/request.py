import sqlite3
import json
from models import Location


LOCATIONS = []



def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    requested_location = None

    for location in LOCATIONS:

        if location["id"] == id:
            requested_location = location

    return requested_location


def create_location(location):
    # Get the id value of the last location in the list
        max_id = LOCATIONS[-1]["id"]

        # Add 1 to whatever that number is
        new_id = max_id + 1

        # Add an `id` property to the location dictionary
        location["id"] = new_id

    # Add the location dictionary to the list
        LOCATIONS.append(location)

    # Return the dictionary with `id` property added
        return location


def get_all_locations():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        """)

        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

          
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(locations)



def get_single_location(id):
    with sqlite3.connect("./kennel.db") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
    db_cursor.execute("""
            SELECT
                l.id,
                l.name,
                l.address
            FROM location l
            WHERE l.id = ?
            """, ( id, ))

        # Load the single result into memory
    data = db_cursor.fetchone()

    location = Location(data['id'], data['name'], data['address'])

    return json.dumps(location.__dict__)
