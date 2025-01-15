"""
Microservice A: Calculates the water extraction efficiency based on waste volume and environmental conditions.
"""

def calculate_efficiency(waste_volume, environment_conditions):
    """
    Calculate water extraction efficiency.

    Args:
        waste_volume (float): The amount of waste to process, in liters.
        environment_conditions (dict): Includes temperature and gravity.

    Returns:
        float: The efficiency percentage (0.0 to 1.0).
    """
    # Base efficiency starts at 85%
    base_efficiency = 0.85

    # Adjust efficiency for temperature differences
    temperature_factor = 1 - abs(25 - environment_conditions["temperature"]) * 0.01

    # Adjust efficiency for gravity variations
    gravity_factor = 1 - abs(1.0 - environment_conditions["gravity"]) * 0.05

    # Calculate the final efficiency by combining factors
    efficiency = base_efficiency * temperature_factor * gravity_factor

    # Ensure efficiency is clamped between 0 (0%) and 1 (100%)
    return max(0, min(efficiency, 1))
