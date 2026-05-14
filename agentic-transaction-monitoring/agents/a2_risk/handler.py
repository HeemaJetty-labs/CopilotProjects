# A2 – Risk Analysis Agent

def calculate_risk(context):
    """
    Simple rule-based risk scoring
    """

    transaction = context["transaction"]
    customer = context["customer"]
    derived = context["derived"]

    risk_score = 0
    reasons = []

    # Rule 1: High amount vs average
    if derived["amountVsAverage"] > 5:
        risk_score += 0.4
        reasons.append("Transaction amount significantly higher than average")

    # Rule 2: New account
    if customer["accountAgeDays"] < 30:
        risk_score += 0.3
        reasons.append("Account is newly created")

    # Rule 3: Risky merchant (basic check)
    if "crypto" in transaction["merchant"].lower():
        risk_score += 0.3
        reasons.append("Transaction involves crypto-related merchant")

    # Clamp score (0 to 1)
    risk_score = min(risk_score, 1.0)

    return risk_score, reasons


def calculate_confidence(context):
    """
    Basic confidence logic
    """

    customer = context["customer"]

    # Simple heuristic
    if customer["kycStatus"] == "VERIFIED":
        return 0.9
    else:
        return 0.6


def handler(a1_output):
    """
    Entry point for A2
    """

    if a1_output["status"] != "READY":
        return a1_output  # pass through errors

    context = a1_output["context"]

    risk_score, reasons = calculate_risk(context)
    confidence = calculate_confidence(context)

    return {
        "status": "ASSESSED",
        "stage": "A2_RISK",
        "riskScore": round(risk_score, 2),
        "confidence": confidence,
        "reasons": reasons,
        "context": context
    }