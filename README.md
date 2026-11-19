# Inventory Management System (MySQL & Python)

A modular Command Line Interface (CLI) application built with Python and MySQL to manage product inventory. This project demonstrates database integration, modular software design, and environment security.

## Features
- **Add Products:** Insert new products with name, price, and quantity into the MySQL database.
- **View Inventory:** Fetch and display all products currently stored in the database.
- **Update Stock:** Modify the quantity of existing products using their unique ID.
- **Delete Products:** Remove products from the database by their ID.
- **Auto-Setup:** Automatically creates the `products` table if it doesn't exist.

## Tech Stack
- **Language:** Python 3
- **Database:** MySQL
- **Libraries:** `mysql-connector-python`, `python-dotenv`
- **Architecture:** Modular structure (Separation of Database, Logic, and UI)

## Project Structure
```text
inventory_system/
│
├── .env                  # Environment variables (DB credentials) - NOT pushed to GitHub
├── .gitignore            # Ignores venv/ and .env
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
│
└── src/
    ├── __init__.py
    ├── database.py       # Handles MySQL connection and table creation
    ├── product.py        # Handles CRUD operations (Add, View, Update, Delete)
    └── main.py           # The CLI user interface