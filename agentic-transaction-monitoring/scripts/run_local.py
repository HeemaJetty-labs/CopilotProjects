import json
from agents.a0_intake.handler import handler

# Load sample transactions
with open("data/sample_transactions.json") as f:
    transactions = json.load(f)

# Take first transaction
transaction = transactions[0]

# Run A0
result = handler(transaction)

print("A0 OUTPUT:")
print(json.dumps(result, indent=2))
