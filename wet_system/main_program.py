"""
Main Program: Orchestrates the W.E.T. system by interacting with all microservices and the user.
"""

# Importing necessary microservices
from microservices.microservice_a_efficiency import calculate_efficiency
from microservices.microservice_b_monitoring import monitor_system
from microservices.microservice_c_adjustment import adjust_operations
from microservices.microservice_d_summary import generate_summary

def main():
    """
    Main function that coordinates all operations of the W.E.T. system.
    """

    # Display a welcome message to the user
    print("Welcome to the W.E.T. System!")
    print("This system optimizes water extraction in space environments.\n")

    try:
        # Get user input for waste volume in liters
        waste_volume = float(input("Enter waste volume (liters): "))

        # Define environmental conditions (e.g., temperature and gravity)
        environment_conditions = {
            "temperature": 25,  # Default temperature in Celsius
            "gravity": 1.0      # Default gravity (Earth standard)
        }

        # Define the system's operational status
        system_status = {
            "filter_status": "optimal",  # Filter condition
            "energy_level": 80          # Energy level in percentage
        }

        # Call Microservice A to calculate water extraction efficiency
        efficiency = calculate_efficiency(waste_volume, environment_conditions)

        # Call Microservice B to monitor the system and generate a status report
        monitoring_report = monitor_system(waste_volume, system_status)

        # Call Microservice C to provide adjustment recommendations based on efficiency and status
        adjustment_recommendation = adjust_operations(efficiency, monitoring_report)

        # Call Microservice D to generate a final summary of results
        summary = generate_summary(efficiency, monitoring_report, adjustment_recommendation)

        # Display the final summary to the user
        print("\n--- W.E.T. System Results ---")
        print(summary)

    except ValueError:
        # Handle invalid input gracefully
        print("Invalid input. Please enter a numeric value for waste volume.")

if __name__ == "__main__":
    # Entry point of the program
    main()
