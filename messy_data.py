import csv
import json
from datetime import datetime

with open("data/messy_transactions.csv", "r") as file:
    transactions = list(csv.DictReader(file))

invalid_transactions = []
unique_transactions = {}

for transaction in transactions:
    transaction_id = transaction["id"]

    if transaction_id not in unique_transactions:
        unique_transactions[transaction_id] = transaction

    else:
        print("Duplicate transaction:", transaction_id)

        current = unique_transactions[transaction_id]

    
        current_filled = sum(
            1 for value in current.values() if value.strip()
        )

        new_filled = sum(
            1 for value in transaction.values() if value.strip()
        )

        if new_filled > current_filled:
            unique_transactions[transaction_id] = transaction


transactions = list(unique_transactions.values())


cleaned_transactions = []

for transaction in transactions:

    transaction["type"] = transaction["type"].lower()

    
    if transaction["type"] not in ["income", "expense"]:
        print("Invalid transaction type:", transaction["type"])

        invalid_transactions.append({
            "id": transaction["id"],
            "reason": "Invalid transaction type"
        })

        continue

   
    try:
        amount = float(
            transaction["amount"]
            .replace(",", "")
            .replace("â‚¦", "")
        )

        transaction["amount"] = amount

    except ValueError:
        print("Invalid amount:", transaction["amount"])

        invalid_transactions.append({
            "id": transaction["id"],
            "reason": "Invalid amount"
        })

        continue

    if not transaction["description"].strip():
        print("Missing description")
        transaction["description"] = "Unknown"

    
    if not transaction["category"].strip():
        print("Missing category")
        transaction["category"] = "Other"

    try:
        date = datetime.strptime(transaction["date"], "%Y-%m-%d")

    except ValueError:
        try:
            date = datetime.strptime(transaction["date"], "%d/%m/%Y")

        except ValueError:
            print("Invalid date:", transaction["date"])

            invalid_transactions.append({
                "id": transaction["id"],
                "reason": "Invalid date"
            })

            continue

    transaction["date"] = date.strftime("%Y-%m-%d")

    
    cleaned_transactions.append(transaction)


transactions = cleaned_transactions


total_income = 0

for transaction in transactions:
    if transaction["type"] == "income":
        total_income += transaction["amount"]

print("Total income:", total_income)


total_expenses = 0

for transaction in transactions:
    if transaction["type"] == "expense":
        total_expenses += transaction["amount"]

print("Total expenses:", total_expenses)


balance = total_income - total_expenses

print("Balance:", balance)



expenses_by_category = {}

for transaction in transactions:
    if transaction["type"] == "expense":
        category = transaction["category"]

        if category not in expenses_by_category:
            expenses_by_category[category] = 0

        expenses_by_category[category] += transaction["amount"]


output = {
    "transactions": transactions,
    "summary": {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "balance": balance,
        "expenses_by_category": expenses_by_category,
        "invalid_transactions": invalid_transactions,
        "transactions_processed": len(transactions)
    }
}

with open("output/messy_transactions.json", "w") as file:
    json.dump(output, file, indent=4)

print("Cleaned data saved to output/messy_transactions.json")