# Microservice D: Generates a summary of system performance and saves output to JSON
import json

def generate_summary():
    """Generate a summary of system performance."""
    try:
        # Read monitoring and adjustments data
        with open("data/monitoring.json", "r") as mon_file:
            monitoring_data = json.load(mon_file)
        with open("data/adjustments.json", "r") as adj_file:
            adjustment_data = json.load(adj_file)
    except (FileNotFoundError, KeyError) as e:
        print(f"Error reading data for summary generation: {e}")
        return

    # Create summary
    summary = {
        "efficiency": f"{monitoring_data['efficiency'] * 100:.2f}%",
        "monitoring": monitoring_data,
        "adjustments": adjustment_data["adjustments"]
    }

    # Save summary to JSON
    with open("data/summary.json", "w") as file:
        json.dump(summary, file)

    print("Summary generated.")

if __name__ == "__main__":
    generate_summary()
