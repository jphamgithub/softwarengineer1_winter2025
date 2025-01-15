# Microservice C: Provides operational adjustment recommendations and saves output to JSON
import json

def adjust_operations():
    """Generate operational adjustments and save to JSON."""
    try:
        # Read monitoring report
        with open("data/monitoring.json", "r") as file:
            monitoring_data = json.load(file)
    except (FileNotFoundError, KeyError) as e:
        print(f"Error reading monitoring data: {e}")
        return

    # Generate adjustments
    adjustments = []
    if monitoring_data["efficiency"] < 0.7:
        adjustments.append("Increase filtration power.")
    if monitoring_data["energy_status"] == "low":
        adjustments.append("Reduce operational intensity.")
    if monitoring_data["filter_status"] != "optimal":
        adjustments.append("Replace or clean filters.")

    # Save adjustments to JSON
    output = {"adjustments": adjustments or ["No adjustments needed."]}
    with open("data/adjustments.json", "w") as file:
        json.dump(output, file)

    print("Adjustments generated.")

if __name__ == "__main__":
    adjust_operations()
