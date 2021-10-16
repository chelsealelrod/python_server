EMPLOYEES = [
    {
      "id": 1,
      "name": "Jeremy Bakker",
      "locationId": 2
    },
    {
      "id": 2,
      "name": "Pine Hodorowicz",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Sarah Potts",
      "locationId": 2
    }
  ]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:

        if employee["id"] == id:
            requested_employee = employee

    return requested_employee