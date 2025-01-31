"""
W.E.T. System: Main Program
---------------------------
This script coordinates the Water Extraction and Transformation (W.E.T.) System. 
It provides a menu-driven interface for users to input data, monitor metrics, 
view efficiency results, generate recommendations, and summarize performance.

Modules:
- Input Data: Allows users to input waste volume and environmental conditions.
- Monitor Metrics: Runs a microservice to analyze system metrics.
- View Efficiency: Displays calculated water extraction efficiency.
- Recommendations: Generates system optimization suggestions.
- Summary: Provides a complete summary of system performance.

Usage:
Run the script and follow the on-screen menu to interact with the system.

Author: Jacob Pham
"""

import os
import json

def display_menu():
    """
    Display the main menu options for the W.E.T. System.
    """
    print("\n" + "=" * 40)
    print("          W.E.T. System Main Menu          ")
    print("=" * 40)
    print("1. Input Data")
    print("2. Monitor Metrics")
    print("3. View Efficiency Results")
    print("4. Get Recommendations")
    print("5. Generate Summary")
    print("6. Exit")
    print("=" * 40)

def input_data():
    """
    Collect user input for waste volume and environmental conditions.

    Prompts the user for waste volume, temperature, and gravity, and 
    saves the data in JSON files to be used by the microservices.
    """
    try:
        print("\n--- Input Data ---")
        waste_volume = float(input("Enter waste volume (liters): "))
        temp_input = input("Enter temperature (°C) [default: 25]: ")
        temperature = float(temp_input) if temp_input.strip() else 25
        gravity_input = input("Enter gravity [default: 1.0]: ")
        gravity = float(gravity_input) if gravity_input.strip() else 1.0

        # Save input data for Microservice A
        input_a = {
            "waste_volume": waste_volume,
            "environment_conditions": {"temperature": temperature, "gravity": gravity}
        }
        with open("data/input_a.json", "w") as file:
            json.dump(input_a, file)

        # Save input data for Microservice B
        input_b = {
            "waste_volume": waste_volume,
            "system_status": {"filter_status": "optimal", "energy_level": 40}
        }
        with open("data/input_b.json", "w") as file:
            json.dump(input_b, file)

        print("\nData submitted successfully!")
    except ValueError:
        print("\nInvalid input. Please enter numeric values for waste volume, temperature, and gravity.")

def monitor_metrics():
    """
    Run the monitoring microservice to generate system metrics.

    Executes the monitoring microservice and saves the results to a JSON file.
    """
    print("\n--- Monitor Metrics ---")
    os.system("python3 microservices/microservice_b_monitoring.py")
    print("System monitoring complete.")

def view_efficiency_results():
    """
    Display the water extraction efficiency.

    Reads and prints the efficiency data from the efficiency.json file.
    """
    print("\n--- View Efficiency Results ---")
    try:
        with open("data/efficiency.json", "r") as file:
            efficiency_data = json.load(file)
        print(f"Efficiency: {efficiency_data['efficiency'] * 100:.2f}%")
    except FileNotFoundError:
        print("Efficiency data not found. Please input data and run the efficiency microservice.")

def get_recommendations():
    """
    Run the adjustments microservice and display recommendations.

    Executes the adjustments microservice and reads the generated recommendations.
    """
    print("\n--- Get Recommendations ---")
    os.system("python3 microservices/microservice_c_adjustment.py")
    try:
        with open("data/adjustments.json", "r") as file:
            adjustments = json.load(file)["adjustments"]
        print("\nRecommendations:")
        for adjustment in adjustments:
            print(f"- {adjustment}")
    except FileNotFoundError:
        print("Recommendations data not found. Please monitor metrics first.")

def generate_summary():
    """
    Generate and display the system performance summary.

    Runs the summary microservice and prints the results from the summary.json file.
    """
    print("\n--- Generate Summary ---")
    os.system("python3 microservices/microservice_d_summary.py")
    try:
        with open("data/summary.json", "r") as file:
            summary = json.load(file)
        print("\n--- System Summary ---")
        print(json.dumps(summary, indent=4))
    except FileNotFoundError:
        print("Summary data not found. Please complete all prior steps before generating a summary.")

def main():
    """
    Main function to orchestrate the W.E.T. System.

    Provides a menu-driven interface for users to interact with the system, 
    allowing them to input data, view metrics, and generate summaries.
    """
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            input_data()
        elif choice == "2":
            monitor_metrics()
        elif choice == "3":
            view_efficiency_results()
        elif choice == "4":
            get_recommendations()
        elif choice == "5":
            generate_summary()
        elif choice == "6":
            print("\nExiting W.E.T. System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
