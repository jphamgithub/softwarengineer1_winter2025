# Main Program: Coordinates microservices using JSON-based communication
import os
import json

def main():
    """Main function to orchestrate the W.E.T. System."""
    print("Welcome to the W.E.T. System!")

    # Prompt for waste volume
    waste_volume = float(input("Enter waste volume (liters): "))

    # Optional: Prompt for environmental temperature
    temp_input = input("Enter temperature (°C) [default: 25]: ")
    temperature = float(temp_input) if temp_input.strip() else 25

    # Optional: Prompt for gravity
    gravity_input = input("Enter gravity [default: 1.0]: ")
    gravity = float(gravity_input) if gravity_input.strip() else 1.0

    # Write input data to JSON file for Microservice A
    input_a = {
        "waste_volume": waste_volume,
        "environment_conditions": {"temperature": temperature, "gravity": gravity}
    }
    with open("data/input_a.json", "w") as file:
        json.dump(input_a, file)

    # Write input data to JSON file for Microservice B
    input_b = {
        "waste_volume": waste_volume,
        "system_status": {"filter_status": "optimal", "energy_level": 40}
    }
    with open("data/input_b.json", "w") as file:
        json.dump(input_b, file)

    # Call microservices using os.system() and JSON files
    os.system("python3 microservices/microservice_a_efficiency.py")
    os.system("python3 microservices/microservice_b_monitoring.py")
    os.system("python3 microservices/microservice_c_adjustment.py")
    os.system("python3 microservices/microservice_d_summary.py")

    # Read and display the final summary
    with open("data/summary.json", "r") as file:
        summary = json.load(file)
    print("\n--- W.E.T. System Summary ---")
    print(json.dumps(summary, indent=4))

if __name__ == "__main__":
    main()
