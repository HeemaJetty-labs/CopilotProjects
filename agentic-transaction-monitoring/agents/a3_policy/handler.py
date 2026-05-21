# A3 – Policy Gate Agent (Deterministic)


# Configurable thresholds (can move to config later)
CONFIDENCE_FLOOR = 0.6
ESCALATE_THRESHOLD = 0.85
AUTO_CLOSE_THRESHOLD = 0.3


def decide_action(risk_score, confidence):
    """
    Deterministic routing logic
    """

    # ✅ Safety first: low confidence → human
    if confidence < CONFIDENCE_FLOOR:
        return "MANUAL_REVIEW", "Low confidence - requires human review"

    # ✅ High risk → escalate
    if risk_score >= ESCALATE_THRESHOLD:
        return "ESCALATE", "High risk transaction"

    # ✅ Low risk → auto close (we will enable later)
    if risk_score <= AUTO_CLOSE_THRESHOLD:
        return "AUTO_CLOSE", "Low risk transaction"

    # ✅ Default → create case
    return "CREATE_CASE", "Medium risk - requires investigation"


def handler(a2_output):
    """
    Entry point for A3
    """

    # Pass through failures
    if a2_output["status"] != "ASSESSED":
        return a2_output

    risk_score = a2_output["riskScore"]
    confidence = a2_output["confidence"]

    action, reason = decide_action(risk_score, confidence)

    return {
        "status": "DECIDED",
        "stage": "A3_POLICY",
        "decision": action,
        "decisionReason": reason,
        "riskScore": risk_score,
        "confidence": confidence,
        "reasons": a2_output["reasons"],
        "context": a2_output["context"]
    }