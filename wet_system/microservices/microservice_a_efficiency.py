# Microservice A: Calculates water extraction efficiency and saves output to JSON
import json

def calculate_efficiency():
    """Calculate water extraction efficiency based on input data."""
    # Read input data from JSON file
    try:
        with open("data/input_a.json", "r") as file:
            input_data = json.load(file)
            waste_volume = input_data["waste_volume"]
            environment_conditions = input_data["environment_conditions"]
    except (FileNotFoundError, KeyError) as e:
        print(f"Error reading input data for efficiency calculation: {e}")
        return

    # Base efficiency for the system
    base_efficiency = 0.85

    # Adjust efficiency based on temperature and gravity
    temperature = environment_conditions["temperature"]
    gravity = environment_conditions["gravity"]
    temperature_factor = max(0, 1 - abs(25 - temperature) * 0.02)
    gravity_factor = max(0, 1 - abs(1.0 - gravity) * 0.05)
    efficiency = max(0, min(base_efficiency * temperature_factor * gravity_factor, 1))

    # Save calculated efficiency to JSON file
    output = {"efficiency": efficiency}
    with open("data/efficiency.json", "w") as file:
        json.dump(output, file)

    print(f"Efficiency calculated: {efficiency * 100:.2f}%")

if __name__ == "__main__":
    calculate_efficiency()
