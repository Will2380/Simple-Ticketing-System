
# Simple-Ticketing-System Simulation (Python)

The "Python Ticketing System Simulation" is a practice project that simulates the basic functionalities of a ticketing system. This project allows users to practice creating, viewing, and closing support tickets through a command-line interface. It serves as an educational tool for learning about ticketing systems and Python programming.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Creating a Ticket](#creating-a-ticket)
  - [Viewing Tickets](#viewing-tickets)
  - [Closing a Ticket](#closing-a-ticket)
- [Contributing](#contributing)

## Introduction

A ticketing system is a crucial tool for tracking and managing support requests or issues. In a real-world scenario, it helps support teams efficiently handle and resolve customer queries, software bugs, or other service requests. This simulation project allows you to understand the fundamental concepts of such systems and practice your Python skills.

## Features

- Create new support tickets with titles and descriptions.
- View a list of all open tickets.
- Close tickets to mark them as resolved.
- A simple and intuitive command-line interface.

## Folder Structure

The project is organized with a clear folder structure:

- `model/`: Contains the data model for the tickets.
- `presenter/`: Manages the application's business logic.
- `view/`: Provides the command-line interface for user interaction.
- `main.py`: The entry point of the simulation.

## Getting Started

### Prerequisites

Before you can run this simulation, you need the following:

- Python 3.x installed on your system.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Will2380/Simple-Ticketing-System.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Simple-Ticketing-System
   ```

3. Run the simulation:

   ```bash
   python main.py
   ```

## Usage

### Creating a Ticket

1. Select "Create Ticket" from the main menu.
2. Enter the title and description for the new ticket.
3. The system will confirm that the ticket was created successfully.

### Viewing Tickets

1. Select "View Tickets" from the main menu.
2. If there are open tickets, you will see a list of ticket titles and their current statuses (open or closed).
3. If there are no tickets, a message indicating that there are no tickets available will be displayed.

### Closing a Ticket

1. Select "Close Ticket" from the main menu.
2. If there are open tickets, you will see a list of ticket titles and their current statuses (open or closed).
3. Enter the index of the ticket you want to close.
4. The selected ticket's status will be changed to "Closed," and you will receive a confirmation message.

## Contributing

Contributions to this project are welcome! If you have any ideas, improvements, or bug fixes, feel free to open an issue or create a pull request. Let's learn and improve together.
