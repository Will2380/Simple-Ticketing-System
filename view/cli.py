# Define the CommandLineInterface class for the command-line user interface
class CommandLineInterface:
    def __init__(self, ticketing_system):
        # Initialize the interface with a reference to the TicketingSystem
        self.ticketing_system = ticketing_system

    def run(self):
        while True:
            print("\nTicketing System Menu:")
            print("1. Create Ticket")
            print("2. View Tickets")
            print("3. Close Ticket")
            print("4. Quit")
            choice = input("Enter your choice: ")

            if choice == "1":
                # If the user chooses to create a ticket, prompt for title and description
                title = input("Enter ticket title: ")
                description = input("Enter ticket description: ")
                # Call the create_ticket method to create a new ticket
                self.ticketing_system.create_ticket(title, description)
                print(f"Ticket '{title}' created successfully.")
            elif choice == "2":
                # If the user chooses to view tickets, call the view_tickets method
                tickets = self.ticketing_system.view_tickets()
                if not tickets:
                    print("No tickets available.")
                else:
                    print("List of Tickets:")
                    for i, ticket in enumerate(tickets, start=1):
                        print(f"{i}. Title: {ticket.title}, Status: {ticket.status}")
            elif choice == "3":
                # If the user chooses to close a ticket, first view the list of tickets
                tickets = self.ticketing_system.view_tickets()
                if not tickets:
                    print("No tickets available.")
                else:
                    print("List of Tickets:")
                    for i, ticket in enumerate(tickets, start=1):
                        print(f"{i}. Title: {ticket.title}, Status: {ticket.status}")
                    ticket_index = int(input("Enter the ticket index to close: "))
                    self.ticketing_system.close_ticket(ticket_index)
                    print(f"Ticket {ticket_index} closed.")
            elif choice == "4":
                # If the user chooses to quit, exit the program
                print("Goodbye!")
                break
            else:
                # Handle invalid choices by displaying an error message
                print("Invalid choice. Please try again.")
