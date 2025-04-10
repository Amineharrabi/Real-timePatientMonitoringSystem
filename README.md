# Real-Time Patient Monitoring System

This project implements a **Real-Time Patient Monitoring System** that evaluates patients' vital signs using machine learning models and sorts them into priority queues based on their risk levels. The system is designed to assist healthcare providers in making timely decisions and allocating resources efficiently.

## Project Structure

```
Real-timePatientMonitoringSystem/
├── PEM.py                # Predictive Early Warning Model (Logistic Regression)
├── SEM.py                # Severity Evaluation Model (SVM)
├── Priority queue/
│   ├── main.c            # Priority queue implementation and integration
│   ├── Queue.c           # Queue operations (add, remove, print)
│   ├── Queue.h           # Queue structure and function declarations
├── mainData.xlsx         # Input dataset for PEM.py
├── mainData.csv          # Input dataset for SEM.py
├── results.csv           # Output file containing patient risk levels
└── README.md             # Project documentation
```

## Workflow

1. **Evaluate Patients**:

   - `PEM.py` predicts patient churn risk using logistic regression.
   - `SEM.py` evaluates patient severity using an SVM classifier.

2. **Export Results**:

   - Both models export predictions to `results.csv` in the format:
     ```
     PatientID,RiskLevel
     1,0
     2,2
     3,1
     ```

3. **Sort Patients**:

   - `main.c` reads `results.csv` and sorts patients into priority queues based on their risk levels using a linked list implementation.

4. **Display Results**:
   - The priority queues are printed to the terminal, showing patients grouped by their risk levels.

## How to Run

### Step 1: Run the Machine Learning Models

- **Run PEM.py**:
  ```bash
  python PEM.py
  ```
- **Run SEM.py**:
  ```bash
  python SEM.py
  ```

### Step 2: Compile and Run the Priority Queue Program

- Compile the C program:
  ```bash
  gcc -o main Priority\ queue/main.c Priority\ queue/Queue.c
  ```
- Run the program:
  ```bash
  ./main
  ```

### Step 3: View Results

The program will display the sorted priority queues in the terminal. For example:

```
Patients sorted into priority queues:
Queue 1:
1, 4,

Queue 2:
3,

Queue 3:
2,

Queue 4:
5,

Queue 5:
(empty)
```

## File Descriptions

### `PEM.py`

- Implements a logistic regression model to predict patient churn risk.
- Outputs predictions to `results.csv`.

### `SEM.py`

- Implements an SVM classifier to evaluate patient severity.
- Outputs predictions to `results.csv`.

### `main.c`

- Reads `results.csv` and sorts patients into priority queues based on their risk levels.
- Uses the queue operations defined in `Queue.c`.

### `Queue.c` and `Queue.h`

- Implements a linked list-based queue structure.
- Provides functions to create, add, remove, and print elements in the queue.

### `results.csv`

- Contains the patient IDs and their corresponding risk levels as predicted by the machine learning models.

## Example `results.csv`

```
PatientID,RiskLevel
1,0
2,2
3,1
4,0
5,3
```

## Requirements

### Python

- Python 3.x
- Libraries: `pandas`, `numpy`, `matplotlib`, `scikit-learn`

### C

- GCC compiler

## Notes

- Ensure `mainData.xlsx` and `mainData.csv` contain the required columns for the models.
- Modify the file paths in the code if necessary to match your directory structure.

## License

This project is licensed under the MIT License.
