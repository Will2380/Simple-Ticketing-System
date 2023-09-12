# Define the Ticket class to represent individual tickets
class Ticket:
    def __init__(self, title, description, status="Open"):
        # Initialize ticket attributes: title, description, and status (default is "Open")
        self.title = title
        self.description = description
        self.status = status
