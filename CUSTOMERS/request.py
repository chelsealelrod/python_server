import sqlite3
import json
from models import Customer

CUSTOMERS =[]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:

        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    # Get the id value of the last customer in the list
        max_id = CUSTOMERS[-1]["id"]

        # Add 1 to whatever that number is
        new_id = max_id + 1

        # Add an `id` property to the customer dictionary
        customer["id"] = new_id

    # Add the customer dictionary to the list
        CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
        return customer

def delete_customer(id):
    # Initial -1 value for customer index, in case one isn't found
    animal_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
            CUSTOMERS.pop(customer_index)


def get_all_customers():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        """)

        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

          
            customer = Customer(row['id'], row['name'], row['address'],
                            row['email'], row['password']
                        )

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)


def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
    db_cursor.execute("""
            SELECT
                c.id,
                c.name,
                c.address,
                c.email,
                c.password
            FROM customer c
            WHERE c.id = ?
            """, ( id, ))

        # Load the single result into memory
    data = db_cursor.fetchone()

    customer = Customer(data['id'], data['name'], data['address'],
                            data['email'], data['password'])

    return json.dumps(customer.__dict__)
