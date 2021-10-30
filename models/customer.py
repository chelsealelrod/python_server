class Customer():

    def __init__(self, id, name, email, password, address):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password

new_customer = Customer(1, "Mo Silvera", "201 Created St", "mo@silvera.com", "password")