import csv
import json
from datetime import datetime

with open("data/clean_transactions.csv", "r") as file:
    transactions = list(csv.DictReader(file))

for transaction in transactions:

    if transaction["type"] not in ["income", "expense"]:
        print("Invalid transaction type:", transaction["type"])

    try:
        amount = float(transaction["amount"])
    except ValueError:
        print("Invalid amount:", transaction["amount"])

    if not transaction["description"].strip():
        print("Missing description")

    try:
        datetime.strptime(transaction["date"], "%Y-%m-%d")
    except ValueError:
        print("Invalid date:", transaction["date"])


total_income = 0

for transaction in transactions:
    if transaction["type"] == "income":
        total_income += float(transaction["amount"])

print("Total income:", total_income)

total_expenses = 0

for transaction in transactions:
    if transaction["type"] == "expense":
        total_expenses += float(transaction["amount"])

print("Total expenses:", total_expenses)
balance = total_income - total_expenses

print("Balance:", balance)

output = {
    "transactions": transactions,
    "summary": {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "balance": balance
    }
}

with open("output/transactions.json", "w") as file:
    json.dump(output, file, indent=4)