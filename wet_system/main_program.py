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
    print("Water extraction from your waste keeps you alive in space! Much benefit!")
    print("Efficiency high and you don't die!")
    print("=" * 40)
    print("1. Input Data")
    print("2. Monitor Metrics")
    print("3. View Efficiency Results")
    print("4. Get Recommendations")
    print("5. Generate Summary")
    print("6. Reset System")
    print("7. Exit")
    print("=" * 40)

def display_tooltips():
    """
    Display tips to guide user input for the W.E.T. System.
    """
    print("\n--- Input Tips ---")
    print("- Waste Volume: Must be a positive number. Values above 10,000 liters may affect performance.")
    print("- Temperature: Enter the ambient temperature in degrees Celsius. Default is 25°C.")
    print("- Gravity: Enter the gravity value (e.g., 1.0 for Earth). Default is 1.0.")
    print("- JSON Data: You can modify system-generated JSON files directly for advanced data analysis.")
    print("\n")

def input_data():
    """
    Collect user input for waste volume and environmental conditions.

    Prompts the user for waste volume, temperature, and gravity, and 
    saves the data in JSON files to be used by the microservices.
    """
    display_tooltips()
    
    print("\n--- Input Data ---")
    print("Ensure your data is accurate to avoid suboptimal performance. Your waste has water and we need to extract it! Or you die!")
    
    try:
        waste_volume = float(input("Enter waste volume (liters): "))
        if waste_volume < 0:
            print("Warning: Waste volume cannot be negative. Please try again.")
            return
        if waste_volume > 10000:
            print("Warning: Waste volume is unusually high. Ensure this value is correct.")
        
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

        print("\nData submitted successfully! Be sure to monitor system metrics for updates.")
    except ValueError:
        print("\nInvalid input. Please enter numeric values for waste volume, temperature, and gravity.")

def monitor_metrics():
    """
    Run the monitoring microservice to generate system metrics.

    Executes the monitoring microservice and saves the results to a JSON file.
    """
    print("\n--- Monitor Metrics ---")
    print("This feature provides insights into system performance, including efficiency and energy usage.")
    print("You can also check or modify 'data/monitoring.json' manually if needed.")
    os.system("python3 microservices/microservice_b_monitoring.py")
    print("System monitoring complete. You can now view efficiency results or get recommendations to improve performance.")

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
        print("If efficiency is below 70%, consider using the Recommendations feature to optimize performance.")
        print("Advanced users: You can edit 'data/efficiency.json' directly for analysis.")
    except FileNotFoundError:
        print("Efficiency data not found. Please input data and run the efficiency microservice.")
        print("Tip: Start with 'Input Data' from the main menu to provide required inputs.")

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
        print("Advanced users: Modify 'data/summary.json' for further customization.")
    except FileNotFoundError:
        print("Summary data not found. Please complete all prior steps before generating a summary.")

def reset_data():
    """
    Reset the system by deleting all generated data files.
    """
    print("\n--- Reset System ---")
    confirm = input("Are you sure you want to reset all data? This cannot be undone. (yes/no): ").strip().lower()
    if confirm == "yes":
        try:
            for file_name in ["data/input_a.json", "data/input_b.json", "data/efficiency.json", 
                              "data/monitoring.json", "data/adjustments.json", "data/summary.json"]:
                if os.path.exists(file_name):
                    os.remove(file_name)
            print("All data has been successfully reset.")
        except Exception as e:
            print(f"An error occurred while resetting data: {e}")
    else:
        print("Reset cancelled.")

def main():
    """
    Main function to orchestrate the W.E.T. System.
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
            reset_data()
        elif choice == "7":
            print("\nExiting W.E.T. System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
