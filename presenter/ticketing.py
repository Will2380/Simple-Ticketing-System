# Import the Ticket class from the model module
from model.ticket import Ticket

# Define the TicketingSystem class to manage tickets
class TicketingSystem:
    def __init__(self):
        # Initialize the ticketing system with an empty list of tickets
        self.tickets = []

    def create_ticket(self, title, description):
        # Create a new ticket with the given title and description
        ticket = Ticket(title, description)
        # Add the new ticket to the list of tickets
        self.tickets.append(ticket)

    def view_tickets(self):
        # Return the list of tickets
        return self.tickets

    def close_ticket(self, ticket_index):
        if 1 <= ticket_index <= len(self.tickets):
            # Close the ticket at the specified index by changing its status to "Closed"
            self.tickets[ticket_index - 1].status = "Closed"
