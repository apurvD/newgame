# Customer Management Dictionary
customer_data = {}

# Function to add a new customer record
def add_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone number: ")
    customer_data[name] = {"email": email, "phone": phone}
    print("Customer record added successfully!")

# Function to remove an existing customer record
def remove_customer():
    name = input("Enter customer name: ")
    if name in customer_data:
        del customer_data[name]
        print("Customer record removed successfully!")
    else:
        print("Customer not found!")

# Function to retrieve customer details
def get_customer_details():
    name = input("Enter customer name: ")
    if name in customer_data:
        details = customer_data[name]
        print("Customer Name:", name)
        print("Email:", details["email"])
        print("Phone:", details["phone"])
    else:
        print("Customer not found!")

def pattern():
    n=int(input("Enter the numbre of stars :"))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
    


# Main loop
choice=0
while(choice!=9):
    print("Welcome, I am a simple ChatBot. How may I assist you today dear sir/madam?")
    print("1. Introduce Yourself to the Chatbot")
    print("2. Features of the Chatbot")
    print("3. View Customer Details")
    print("4. Insert Customer Details")
    print("5. Remove Customer Details")
    print("6. Display Date and Time")
    print("7. Display unique pattern")
    print("8. Display remainder of division of two numbers")
    print("9. Exit...")

    choice=int(input("Kindly Enter your choice!\n"))

    if choice==1:
        name=input("Hi, I am Chatbot. \n What is your good name?\n")
        print("\nHello ",name, " Nice to meet you. \n Hope you have a wonderful day!\n")

    elif choice==2:
        print("\nHey, this is the demonstration of a simple cutomer details management system. You can add, delete or view records as per your preference.\n")

    elif choice == 3:
        get_customer_details()

    elif choice == 4:
        add_customer()

    elif choice == 5:
        remove_customer()

    elif choice==6:
        import datetime
        current_datetime = datetime.datetime.now()
        print("\nCurrent date and time:\n", current_datetime)

    elif choice==7:
        print("\nDisplaying a triangular star pattern")
        pattern()

    elif choice==8:
        dividend = 17
        divisor = 5
        remainder = dividend % divisor
        print("Remainder:", remainder)      

    elif choice==9:
        print("\nSee you later, GoodBye for now!\n")

    else:
        print("\nInvalid choice. Please try again.\n")

