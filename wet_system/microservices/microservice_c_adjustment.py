"""
Microservice C: Recommends adjustments to improve system performance.
"""

def adjust_operations(efficiency, monitoring_report):
    """
    Provide recommendations for optimizing system performance.

    Args:
        efficiency (float): The current water extraction efficiency.
        monitoring_report (dict): The system's operational report.

    Returns:
        list: A list of recommended actions.
    """
    # Initialize the list of adjustments
    adjustments = []

    # Recommend action if efficiency is below a threshold
    if efficiency < 0.7:
        adjustments.append("Increase filtration power.")

    # Recommend action if energy level is low
    if monitoring_report["energy_status"] == "low":
        adjustments.append("Reduce operational intensity to save energy.")

    # Recommend action if filters are not optimal
    if monitoring_report["filter_status"] != "optimal":
        adjustments.append("Replace or clean filters.")

    # Return adjustments or indicate no action is needed
    return adjustments if adjustments else ["No adjustments needed."]
