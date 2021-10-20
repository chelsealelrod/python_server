CUSTOMERS =[
{
    "id": 1,
    "name": "Hannah Hall",
    "address": "7002 Chestnut Ct",
    "email": "hannah@hannahhall.com"
    },
{
    "id": 2,
    "name": "Peter Parker",
    "address": "5002 Spider Lane",
    "email": "peter@peterparker.com"
},
{
    "id": 3,
    "name": "Luke Skywalker",
    "address": "247 Galaxy Way",
    "email": "luke@lukeskywalker.com"
}

]

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

