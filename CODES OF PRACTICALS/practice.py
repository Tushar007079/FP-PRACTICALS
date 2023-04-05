# Define customer data structure with fields like name, address, contact no, pin code, hobbies, and life goal
class Customer:
    def __init__(self, name, address, contact_no, pin_code, hobbies, life_goal):
        self.name = name
        self.address = address
        self.contact_no = contact_no
        self.pin_code = pin_code
        self.hobbies = hobbies
        self.life_goal = life_goal

# Define function to check entered data type and match it with required data type
def validate_customer_details(customer):
    if not isinstance(customer.name, str):
        return "Name should be a string"
    if not isinstance(customer.address, str):
        return "Address should be a string"
    if not isinstance(customer.contact_no, int):
        return "Contact number should be an integer"
    if not isinstance(customer.pin_code, int):
        return "Pin code should be an integer"
    if not isinstance(customer.hobbies, list):
        return "Hobbies should be a list"
    if not isinstance(customer.life_goal, str):
        return "Life goal should be a string"
    return "Valid details"

# Define function to check customer age category and provide savings schemes accordingly
def provide_savings_scheme(customer, age):
    if age < 18:
        return "Education camp schemes"
    elif age >= 18 and age < 40:
        return "Educational scholarship schemes"
    else:
        return "Retirement plans"

# Create multiple customer accounts and check entered name and their age category
customers = [
    Customer("John", "ABC Road", 1234567890, 123456, ["Reading", "Travelling"], "Start a business"),
    Customer("Jane", "XYZ Road", 9876543210, 654321, ["Cooking", "Dancing"], "Buy a house"),
    Customer("Jim", "PQR Road", 1111111111, 111111, ["Gaming", "Singing"], "Early retirement")
]

for customer in customers:
    print("Name:", customer.name)
    print("Validation result:", validate_customer_details(Customer.name))
    name=(input("Enter Name: "))
    print("Validation result:", validate_customer_details(customer))
    age = int(input("Enter age: "))
    print("Savings scheme:", provide_savings_scheme(customer, age))
    print("\n")
    print("Validation result:", validate_customer_details(customer))
   
    
