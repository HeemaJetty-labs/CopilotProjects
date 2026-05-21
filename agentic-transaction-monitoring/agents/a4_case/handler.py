# A4 – Case Pack Builder


def build_summary(context, risk_score, reasons):
    """
    Create human-readable summary
    """

    transaction = context["transaction"]
    customer = context["customer"]

    summary_parts = []

    summary_parts.append(
        f"Transaction of {transaction['amount']} {transaction['currency']} "
        f"for account {transaction['accountId']}."
    )

    summary_parts.append(
        f"Customer account age: {customer['accountAgeDays']} days."
    )

    summary_parts.append(
        f"Merchant: {transaction['merchant']}."
    )

    if reasons:
        summary_parts.append("Key risk indicators:")
        for r in reasons:
            summary_parts.append(f"- {r}")

    return " ".join(summary_parts)


def build_next_steps(context):
    """
    Suggest what analyst should check next
    """

    return [
        "Verify transaction against customer's typical behavior",
        "Check recent transaction history for similar patterns",
        "Validate source of funds if required",
        "Review any linked accounts or related transactions"
    ]


def handler(a3_output):
    """
    Entry point for A4
    """

    if a3_output["status"] != "DECIDED":
        return a3_output

    decision = a3_output["decision"]

    # Only create case for human-involved flows
    if decision not in ["MANUAL_REVIEW", "CREATE_CASE", "ESCALATE"]:
        return a3_output

    context = a3_output["context"]
    risk_score = a3_output["riskScore"]
    confidence = a3_output["confidence"]
    reasons = a3_output["reasons"]

    case = {
        "caseId": f"CASE-{context['transaction']['transactionId']}",
        "priority": "HIGH" if risk_score > 0.8 else "MEDIUM",
        "decision": decision,
        "summary": build_summary(context, risk_score, reasons),
        "riskScore": risk_score,
        "confidence": confidence,
        "reasons": reasons,
        "nextSteps": build_next_steps(context),
        "context": context
    }

    return {
        "status": "CASE_BUILT",
        "stage": "A4_CASE",
        "case": case
    }