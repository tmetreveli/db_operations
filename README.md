# Fake Book Data Generator

This Python script generates fake book data and stores it in an SQLite in-memory database. It uses the Faker library to create realistic book names, page numbers, cover types, and categories. This script is an excellent tool for testing database-related applications, learning SQLite operations, or generating dummy data for any book-related project.

## Features

- Generates fake data for books, including name, page number, cover type, and category.
- Uses SQLite to store and manage this data in an in-memory database.
- Performs basic SQL queries to retrieve all books, calculate the average page number, and find the book with the maximum page number.

## Requirements

To run this script, you need Python installed on your system along with the following Python packages:

- sqlite3 - Comes pre-installed with Python.
- Faker - Can be installed via pip.

### To install dependencies, run:
```
  pip install requirements.txt
```

## How It Works

1 The script performs the following operations:

2 Database Setup: Initializes an SQLite in-memory database and creates a table named book with columns for name, page number, cover type, and category.

3 Data Generation and Insertion: Generates fake data for 10 books using the Faker library and inserts this data into the book table.

4 Data Retrieval: Executes SQL queries to:

- Retrieve and display all records from the book table.
- Calculate and display the average number of pages across all books.
- Find and display the book with the maximum number of pages.
- Cleanup: Commits any pending transactions to the database and closes the connection.

## Usage

Ensure you have Python and the required packages installed, then run the script:
```
  python db.py
```
