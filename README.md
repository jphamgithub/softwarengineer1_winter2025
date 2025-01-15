
# W.E.T. System (Water Extraction and Transformation System)

The **W.E.T. System** is a Python-based project designed to optimize water extraction efficiency in space environments. It employs microservices to calculate, monitor, adjust, and summarize water extraction processes for optimal performance in resource-constrained settings. Outputs are provided in JSON format for integration with other systems or detailed analysis.

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
    │   ├── microservice_d_summary.py     # Summarizes operations and outputs JSON
    └── tests/                 # Unit tests for all components
        ├── test_efficiency.py   # Tests for microservice A
        ├── test_monitoring.py   # Tests for microservice B
        ├── test_adjustment.py   # Tests for microservice C
        ├── test_summary.py      # Tests for microservice D
```

---

## How It Works

The W.E.T. System uses a **modular microservices architecture**, where each microservice performs a specific role:

1. **Efficiency Calculation** (`microservice_a_efficiency.py`): Computes water extraction efficiency.
2. **Monitoring** (`microservice_b_monitoring.py`): Tracks metrics like waste volume and resource consumption.
3. **Adjustment** (`microservice_c_adjustment.py`): Suggests operational changes to improve efficiency.
4. **Summary** (`microservice_d_summary.py`): Provides a JSON-formatted report summarizing system performance.

The `main_program.py` integrates these microservices and provides a user-friendly interface for astronauts or ground control.

---

## Installation and Setup

### Prerequisites

- Python 3.8 or later installed on your system.

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/softwarengineer1_winter2025.git
   cd softwarengineer1_winter2025/wet_system
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Main Program:**
   ```bash
   python3 main_program.py
   ```

4. **Run Tests:**
   ```bash
   pytest tests/
   ```

---

## Usage

### Running the Program
- **Input**: Provide parameters such as waste volume, environmental conditions, and system status.
- **Output**: The program generates a JSON report of the system's performance.

### JSON Output Example:
The summary will be saved in `summary_report.json`. Below is an example output:

```json
{
    "WaterExtractionEfficiency": "85.00%",
    "SystemMonitoringReport": {
        "filter_status": "optimal",
        "energy_status": "sufficient",
        "waste_volume": 100
    },
    "RecommendedAdjustments": [
        "Increase filtration power.",
        "Optimize energy usage."
    ]
}
```

### How to Use JSON Outputs
1. Run the program to generate a report.
2. The JSON file `summary_report.json` is automatically saved in the project directory.
3. This file can be shared with other team members or integrated into downstream applications for further processing.

---

## Features

- **Efficiency Optimization**: Advanced algorithms to maximize water recovery.
- **JSON Integration**: Outputs are stored in JSON format for compatibility and ease of sharing.
- **Real-Time Monitoring**: Tracks and reports system metrics in real-time.
- **Actionable Insights**: Suggests adjustments to enhance system performance.

---

## Contributing

We welcome contributions! Please fork the repository, create a feature branch, and submit a pull request.


