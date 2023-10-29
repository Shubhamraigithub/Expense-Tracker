import csv
import os

# Define the CSV file to store expenses
expenses_file = "expenses.csv"

# Check if the expenses file exists and create it if not
if not os.path.exists(expenses_file):
    with open(expenses_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Description", "Amount"])

# Function to add an expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter a description for the expense: ")
    amount = float(input("Enter the expense amount: $"))

    with open(expenses_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount])

    print("Expense added successfully!")

# Function to view expenses
def view_expenses():
    with open(expenses_file, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for i, row in enumerate(reader, 1):
            date, description, amount = row
            print(f"{i}. Date: {date}, Description: {description}, Amount: ${amount}")

# Function to calculate the total expenses
def calculate_total_expenses():
    total = 0
    with open(expenses_file, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            total += float(row[2])
    print(f"Total Expenses: ${total:.2f}")

# Main program loop
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add an Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total_expenses()
    elif choice == "4":
        print("Exiting Expense Tracker.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
