# Microservice B: Monitors system status and saves output to JSON
import json

def monitor_system():
    """Monitor system status and write to a JSON file."""
    try:
        # Read input data from JSON
        with open("data/input_b.json", "r") as file:
            input_data = json.load(file)
            waste_volume = input_data["waste_volume"]
            system_status = input_data["system_status"]

        # Read efficiency data from Microservice A's output
        with open("data/efficiency.json", "r") as file:
            efficiency_data = json.load(file)
    except (FileNotFoundError, KeyError) as e:
        print(f"Error reading data for system monitoring: {e}")
        return

    # Determine energy status
    energy_status = "low" if system_status["energy_level"] < 50 else "sufficient"

    # Create monitoring report
    report = {
        "waste_volume": waste_volume,
        "energy_status": energy_status,
        "filter_status": system_status["filter_status"],
        "efficiency": efficiency_data["efficiency"]
    }

    # Save monitoring report to JSON
    with open("data/monitoring.json", "w") as file:
        json.dump(report, file, indent=4)  # Use indent for better formatting

    # Print monitoring details to the terminal
    print("\n--- Monitoring Report ---")
    print(json.dumps(report, indent=4))  # Display the report in a readable format
    print("\nSystem monitoring complete. Report saved to 'data/monitoring.json'.")

if __name__ == "__main__":
    monitor_system()
