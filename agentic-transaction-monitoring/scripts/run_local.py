import json
from agents.a0_intake.handler import handler as a0_handler
from agents.a1_context.handler import handler as a1_handler
from agents.a2_risk.handler import handler as a2_handler

# Load transaction
with open("data/sample_transactions.json") as f:
    transactions = json.load(f)

transaction = transactions[0]

# A0
a0_result = a0_handler(transaction)

# A1
a1_result = a1_handler(a0_result)

# A2
a2_result = a2_handler(a1_result)

print("FINAL OUTPUT:")
print(json.dumps(a2_result, indent=2))