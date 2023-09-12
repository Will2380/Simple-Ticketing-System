# Import necessary classes from presenter and view modules
from presenter.ticketing import TicketingSystem
from view.cli import CommandLineInterface

def main():
    # Create an instance of the TicketingSystem class
    ticket_system = TicketingSystem()
    # Create an instance of the CommandLineInterface class
    cli = CommandLineInterface(ticket_system)
    # Start the command-line interface
    cli.run()

if __name__ == "__main__":
    main()
