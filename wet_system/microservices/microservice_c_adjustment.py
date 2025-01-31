# Microservice C: Provides operational adjustment recommendations and saves output to JSON
import json

def adjust_operations():
    """Generate operational adjustments based on monitoring data and save to JSON."""
    try:
        # Read monitoring report
        with open("data/monitoring.json", "r") as file:
            monitoring_data = json.load(file)
    except (FileNotFoundError, KeyError) as e:
        print(f"Error reading monitoring data: {e}")
        return

    # Extract key metrics
    efficiency = monitoring_data["efficiency"]
    energy_status = monitoring_data["energy_status"]
    filter_status = monitoring_data["filter_status"]
    waste_volume = monitoring_data["waste_volume"]

    # Generate adjustments based on conditions
    adjustments = []

    # Efficiency-related adjustments
    if efficiency < 0.7:
        adjustments.append(f"Efficiency is low ({efficiency * 100:.2f}%). Consider increasing filtration power or optimizing processes.")
    elif efficiency > 0.9:
        adjustments.append("Efficiency is high. No major changes needed.")

    # Energy-related adjustments
    if energy_status == "low":
        adjustments.append("Energy level is low. Reduce operational intensity or switch to energy-saving mode.")
    else:
        adjustments.append("Energy level is sufficient. Maintain current power settings.")

    # Filter-related adjustments
    if filter_status != "optimal":
        adjustments.append("Filters are not optimal. Inspect and replace or clean filters as needed.")
    else:
        adjustments.append("Filters are in optimal condition. No immediate action required.")

    # Waste volume-related insights
    if waste_volume > 1000:
        adjustments.append(f"High waste volume detected ({waste_volume} liters). Consider scheduling additional extraction cycles.")
    elif waste_volume < 100:
        adjustments.append(f"Waste volume is low ({waste_volume} liters). System is running efficiently.")

    # Save adjustments to JSON
    output = {"adjustments": adjustments or ["System is running optimally. No adjustments needed."]}
    with open("data/adjustments.json", "w") as file:
        json.dump(output, file, indent=4)  # Pretty-print JSON output

    # Print adjustments to terminal
    print("\n--- Generated Adjustments ---")
    for i, adjustment in enumerate(adjustments, start=1):
        print(f"{i}. {adjustment}")
    print("\nAdjustments saved to 'data/adjustments.json'.")

if __name__ == "__main__":
    adjust_operations()
