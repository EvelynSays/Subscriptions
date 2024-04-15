import json

# Variable to keep track of whether the program is running
not_done = True

# Empty list to store subscriptions
subscriptions = []

class Subscription:
    def __init__(self, name, cost, category, active=True):
        self.name = name
        self.cost = cost
        self.category = category
        self.active = active

    def __str__(self):
        return f"Name: {self.name}, Cost: £{self.cost}, Category: {self.category}, Active: {self.active}"

    def to_dict(self):
        return {
            'name': self.name,
            'cost': self.cost,
            'category': self.category,
            'active': 'Yes' if self.active else 'No'
        }

    @staticmethod
    def from_dict(source):
        return Subscription(source['name'], source['cost'], source['category'], source['active'])

# Function to save the subscriptions to a json file
def save_subscriptions():
    global subscriptions
    with open('FILE_PATH_HERE', 'w') as file:
        json.dump([subscription.to_dict() for subscription in subscriptions], file)

# Function to load the subscriptions from a json file
def load_subscriptions():
    global subscriptions
    import os.path
    if os.path.isfile('FILE_PATH_HERE'):
        with open('FILE_PATH_HERE', 'r') as file:
            subscriptions = [Subscription.from_dict(s) for s in json.load(file)]
    else:
        with open('FILE_PATH_HERE', 'w') as file:
            file.write('[]')
            subscriptions = []

# Function to add a subscription to the list    
def add_subscription(name, cost, category):
    global subscriptions
    subscriptions.append(Subscription(name, cost, category))
    save_subscriptions()

#Load the subscriptions from the json file and display the welcome text.
load_subscriptions()
print("Welcome to Subscriptions")
print("What would you like to do?")

# Main loop to run the program
while not_done:
    print("1. Add a subscription")
    print("2. View all subscriptions")
    print("3. Manage Subscriptions")
    print("4. Exit")
    choice = input("Enter a choice: ")

    if choice == '1':
        name = input("Enter the name of the subscription: ")
        cost = float(input("Enter the cost of the subscription: "))
        category = input("Enter the category of the subscription: ")
        add_subscription(name, cost, category)
    elif choice == '2':
        if not subscriptions:
            print("No subscriptions")
        for subscription in subscriptions:
            print(subscription)
    elif choice == '3':
        print("1. Activate a subscription")
        print("2. Deactivate a subscription")
        print("3. Delete a subscription")
        print("These are your current subscriptions:")
        for index, subscription in enumerate(subscriptions):
            print(f"{index + 1}. {subscription}")
        manage_choice = input("Enter a choice: ")
        if manage_choice == '1':
            for index, subscription in enumerate(subscriptions):
                print(f"{index + 1}. {subscription}")
            activate_choice = int(input("Enter the number of the subscription to activate: "))
            subscriptions[activate_choice - 1].active = True
            save_subscriptions()
        elif manage_choice == '2':
            for index, subscription in enumerate(subscriptions):
                print(f"{index + 1}. {subscription}")
            deactivate_choice = int(input("Enter the number of the subscription to deactivate: "))
            subscriptions[deactivate_choice - 1].active = False
            save_subscriptions()
        elif manage_choice == '3':
            for index, subscription in enumerate(subscriptions):
                print(f"{index + 1}. {subscription}")
            delete_choice = int(input("Enter the number of the subscription to delete: "))
            subscriptions.pop(delete_choice - 1)
            save_subscriptions()
    elif choice == '4':
        print("Would you like to save before exiting?")
        save = input("Enter 'yes' or 'no': ")
        if save == 'yes':
            save_subscriptions()
            not_done = False
        elif save == 'no':
            print("Thank you for using Subscriptions. Goodbye!")
            not_done = False
    else:
        print("Invalid choice")