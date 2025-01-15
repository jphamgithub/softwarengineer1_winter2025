"""
Microservice B: Monitors the operational status of the system.
"""

def monitor_system(waste_volume, system_status):
    """
    Monitor the system's current operational state.

    Args:
        waste_volume (float): The current waste volume being processed.
        system_status (dict): Includes energy level and filter status.

    Returns:
        dict: A report on the system's status.
    """
    # Determine energy status based on energy level
    energy_status = "low" if system_status["energy_level"] < 50 else "sufficient"

    # Retrieve filter status
    filter_status = system_status["filter_status"]

    # Return a structured monitoring report
    return {
        "waste_volume": waste_volume,
        "energy_status": energy_status,
        "filter_status": filter_status
    }
