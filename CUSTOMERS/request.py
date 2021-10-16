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
