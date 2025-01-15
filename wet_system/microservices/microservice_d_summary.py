"""
Microservice D: Generates a detailed summary of system performance and adjustments.
"""

def generate_summary(efficiency, monitoring_report, adjustments):
    """
    Generate a summary report of the system's performance.

    Args:
        efficiency (float): Water extraction efficiency.
        monitoring_report (dict): System status details.
        adjustments (list): Recommended operational adjustments.

    Returns:
        str: A formatted summary string.
    """
    # Format the summary details for user output
    return (
        f"Water Extraction Efficiency: {efficiency * 100:.2f}%\n"
        f"System Monitoring Report: {monitoring_report}\n"
        f"Recommended Adjustments: {', '.join(adjustments)}"
    )
