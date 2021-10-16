LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "8422 Johnson Pike",
      "locationId": 2
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "209 Emory Drive",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Nashville East",
      "address": "5th Avenue",
      "locationId": 3
    }
]


def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    requested_location = None

    for location in LOCATIONS:

        if location["id"] == id:
            requested_location = location

    return requested_location