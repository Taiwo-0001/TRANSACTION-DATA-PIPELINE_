## How to run the project
1. Install python.
2. Open the project folder in VS Code.
3. Open the VS Code terminal.
4. Run the clean data program:
python main.py
5. Run the messy data program:
python messy_data.py
6. The program will save the results to the output folder.
The result for clean data is saved in:
output/transactions.json

The result for messy data is saved in:
output/messy_transactions.json

## Data Validation
The validation rule for the transactions are the following:
1. The date must be valid.
2. There is no empty description.
3. There are no invalid amounts.
4. Transaction type must be one of the two expected: 'expense' or 'income'. 
5. Transaction ID is used when calculating duplicate transactions. 
6. If a transaction has a problem that makes it invalid, it is not added to the cleaned transactions.
7. The invalid transaction is added to the invalid_transactions section of the output.

## Data Cleaning
I had some problems with the messy data, so I did the following:
1. Removed Currency Symbolsand commasfrom the amounts.
2. Conversions of amounts were to a numeric integer/float value.
3. Dates were standardized to a YYYY-MM-DD format.
4. If the description was empty, I used Unknown.
5. If the category was empty, I used Other.
6. Changed Income and other types to lowercase.
7. Removed duplicate transactions
8. Removed transactions with invalid dates.
9. Removed transactions with amounts that were not numbers.
10. Removed transactions  invalid types.
11. I kept negative amounts.

## Assumptions
1. A transaction with a missing category can still be used, so I used Other.
2. A transaction with a missing description can still be used, so I used Unknown.
3. When duplicate transactions have different information, I keep the one with more information.
4. Currency symbols and commas do not change the actual amount.
5. I have kept transactions with negative amounts in the output as these are valid numbers.


## Project Structure
1. data: it contains the CSV  files.
2. output: it contains  JSON results.
3. tests: it contains the test files.
4. main.py: This script processes the clean transaction data.
5. messy_data.py: cleans and processes the messy transaction data.

## Testing
I wrote three simple tests to check the total income, total expenses and balance.
I ran the tests using:
python -m pytest
The result was: 3 passed.

