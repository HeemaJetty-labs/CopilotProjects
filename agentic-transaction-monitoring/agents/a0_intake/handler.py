# A0 - Intake & Validation Agent

# This agent ensures incoming transaction data is valid
# before passing it deeper into the workflow

# =====================================================

# Required fields for every transaction
REQUIRED_TRANSACTION_FIELDS = [
    "transactionId",
    "accountId",
    "amount",
    "currency",
    "timestamp",
    "merchant"
]


def validate_transaction(transaction):
    """
    Validates incoming transaction data.

    Returns:
        (is_valid: bool, error: str or None)
    """

    # ✅ 1. Input must be a dictionary
    if not isinstance(transaction, dict):
        return False, "Transaction must be a dictionary"

    # ✅ 2. Check all required fields exist
    for field in REQUIRED_TRANSACTION_FIELDS:
        if field not in transaction:
            return False, f"Missing required field: {field}"

    # ✅ 3. Validate data types
    if not isinstance(transaction["amount"], (int, float)):
        return False, "Amount must be a number"

    if not isinstance(transaction["currency"], str):
        return False, "Currency must be a string"

    if not isinstance(transaction["accountId"], str):
        return False, "AccountId must be a string"

    # ✅ 4. Business rule checks
    if transaction["amount"] <= 0:
        return False, "Amount must be greater than 0"

    if len(transaction["currency"]) != 3:
        return False, "Currency must be 3-letter ISO code"

    # ✅ 5. All checks passed
    return True, None


def handler(transaction):
    """
    Entry point for A0 Agent
    """

    is_valid, error = validate_transaction(transaction)

    if not is_valid:
        return {
            "status": "REJECTED",
            "stage": "A0_INTAKE",
            "reason": error
        }

    return {
        "status": "VALID",
        "stage": "A0_INTAKE",
        "data": transaction
    }