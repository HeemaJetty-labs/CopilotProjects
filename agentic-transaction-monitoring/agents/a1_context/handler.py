import json


def load_customers():
    """
    Load mock customer data
    """
    with open("data/sample_customers.json") as f:
        return json.load(f)


def find_customer(account_id, customers):
    """
    Find matching customer by accountId
    """
    for customer in customers:
        if customer["accountId"] == account_id:
            return customer
    return None


def build_context(transaction):
    """
    Build combined context (transaction + customer)
    """

    customers = load_customers()

    customer = find_customer(transaction["accountId"], customers)

    if not customer:
        return {
            "status": "REJECTED",
            "stage": "A1_CONTEXT",
            "reason": "Customer not found"
        }

    # ✅ Build MCP-style context
    context = {
        "transaction": transaction,
        "customer": customer,
        "derived": {
            "amountVsAverage": transaction["amount"] / customer["avgTransactionAmount"]
        }
    }

    return {
        "status": "READY",
        "stage": "A1_CONTEXT",
        "context": context
    }


def handler(a0_output):
    """
    Entry point for A1
    """

    if a0_output["status"] != "VALID":
        return a0_output  # pass through rejection

    transaction = a0_output["data"]

    return build_context(transaction)