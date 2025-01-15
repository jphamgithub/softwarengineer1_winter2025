
# W.E.T. System (Water Extraction and Transformation System)

The **W.E.T. System** is a Python-based project designed to optimize water extraction efficiency in space environments. It employs microservices to calculate, monitor, adjust, and summarize water extraction processes for optimal performance in resource-constrained settings. 

---

## Directory Structure

```
.
├── README.md                  # Main project README
└── wet_system/                # Core project directory
    ├── main_program.py        # Main program to orchestrate microservices
    ├── requirements.txt       # Python dependencies
    ├── microservices/         # Directory containing microservices
    │   ├── microservice_a_efficiency.py  # Calculates extraction efficiency
    │   ├── microservice_b_monitoring.py  # Monitors system metrics
    │   ├── microservice_c_adjustment.py  # Provides system adjustment suggestions
    │   ├── microservice_d_summary.py     # Summarizes operations and insights
    └── tests/                 # Unit tests for all components
        ├── test_efficiency.py   # Tests for microservice A
        ├── test_monitoring.py   # Tests for microservice B
        ├── test_adjustment.py   # Tests for microservice C
        ├── test_summary.py      # Tests for microservice D
```

---

## How It Works

The W.E.T. System utilizes a **modular microservices architecture**, where each microservice performs a specific role:

1. **Efficiency Calculation** (`microservice_a_efficiency.py`): Computes the water extraction efficiency based on input parameters.
2. **Monitoring** (`microservice_b_monitoring.py`): Tracks system metrics such as waste volume and resource consumption.
3. **Adjustment** (`microservice_c_adjustment.py`): Suggests operational changes to improve efficiency.
4. **Summary** (`microservice_d_summary.py`): Provides a comprehensive overview of system performance.

The `main_program.py` integrates these microservices and provides a user-friendly interface for astronauts or ground control to interact with the system.

---

## Installation and Setup

Follow these steps to set up and run the project:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/softwarengineer1_winter2025.git
   cd softwarengineer1_winter2025/wet_system
   ```

2. **Install Dependencies:**
   Ensure you have Python 3.8 or later installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Main Program:**
   Execute the main program to start the W.E.T. System:
   ```bash
   python3 main_program.py
   ```

4. **Run Tests:**
   Ensure all components are working as expected:
   ```bash
   pytest tests/
   ```

---

## Usage

### Running the Program
- **Input**: Provide parameters such as waste volume, environmental conditions, and system status.
- **Output**: The system calculates efficiency, monitors metrics, suggests adjustments, and summarizes data.

### Example Workflow:
1. Start the program using `python main_program.py`.
2. Enter the required parameters as prompted.
3. View real-time metrics and adjustment suggestions.
4. Receive a detailed performance summary.

---

## Features

- **Efficiency Optimization**: Advanced algorithms for water recovery.
- **Modular Design**: Easy to maintain and extend with additional microservices.
- **Real-Time Monitoring**: Tracks system performance for immediate feedback.
- **Actionable Insights**: Provides clear adjustment recommendations.

---

## Contributing

We welcome contributions! Please fork the repository, create a feature branch, and submit a pull request.


