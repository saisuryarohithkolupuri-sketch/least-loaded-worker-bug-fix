# Least Loaded Selection Logic Bug Fix

## Overview

This project fixes a bug in a load balancer where the worker selection logic incorrectly relied on dictionary insertion order instead of selecting the worker with the fewest active tasks.

The updated implementation sorts all available workers based on their active task count and always assigns the next task to the least-loaded worker. This ensures fair task distribution, better resource utilization, and improved load balancing.

---

## Task Information

- **Task Type:** Bug Fix
- **Assigned Task:** Least Loaded Selection Logic Bug Fix
- **Module:** Load Balancing
- **Difficulty:** Easy
- **Intern Name:** K. Sai Surya Rohith

---

## Problem Statement

The existing implementation selected workers using dictionary order, which could assign tasks to a busy worker instead of the least-loaded one.

### Before Bug Fix

Example worker status:

| Worker | Active Tasks |
|---------|-------------:|
| Worker_A | 5 |
| Worker_B | 2 |
| Worker_C | 1 |
| Worker_D | 4 |

Old implementation:

```python
selected_worker = next(iter(workers))
```

Output:

```
Worker_A
```

This is incorrect because Worker_A has the highest number of active tasks.

---

## Solution

The bug was fixed by sorting all workers according to their active task count.

Updated implementation:

```python
sorted_workers = sorted(
    workers.items(),
    key=lambda worker: worker[1]
)

selected_worker = sorted_workers[0][0]
```

Output:

```
Worker_C
```

Now the scheduler correctly selects the worker with the least number of active tasks.

---

## Features

- Fixes least-loaded worker selection bug
- Sorts workers based on active task count
- Fair task allocation
- REST API using Flask
- Simple and modular architecture
- Easy to extend

---

## Project Structure

```text
least_loaded_worker_bug_fix/
│
├── app.py
├── load_balancer.py
├── workers.py
├── test.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- Flask
- Requests
- JSON
- VS Code
- Git & GitHub

---

## Installation

### Clone Repository

```bash
git clone https://github.com/saisuryarohithkolupuri-sketch/least-loaded-worker-bug-fix 
```

### Navigate to Project

```bash
cd least_loaded_worker_bug_fix
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

The server starts at:

```
http://127.0.0.1:5000
```

---

## API Endpoint

### Assign Task

**GET**

```
/assign
```

---

## Sample Response

```json
{
  "assigned_worker": "Worker_C",
  "active_tasks": {
    "Worker_A": 5,
    "Worker_B": 2,
    "Worker_C": 2,
    "Worker_D": 4
  }
}
```

---

## Running Test Cases

Open another terminal.

```bash
python test.py
```

Example Output:

```
Assigned Worker : Worker_C
Assigned Worker : Worker_B
Assigned Worker : Worker_C
Assigned Worker : Worker_D
```

---

## Algorithm

1. Read all available workers.
2. Sort workers by active task count.
3. Select the worker with the minimum active tasks.
4. Assign the new task.
5. Increment that worker's active task count.
6. Return the updated worker information.

---

## System Workflow

```text
Incoming Task
      │
      ▼
Load Balancer
      │
      ▼
Sort Workers by Active Tasks
      │
      ▼
Select Least Loaded Worker
      │
      ▼
Assign Task
      │
      ▼
Update Active Task Count
      │
      ▼
Return Response
```

---

## Testing

The project was tested using multiple worker configurations.

### Test Cases

- Workers with different active task counts
- Equal active task counts
- Multiple consecutive task assignments
- Empty worker validation
- API response verification

The scheduler correctly selected the least-loaded worker in every test.

---

## Future Improvements

- Dynamic worker registration
- Worker health monitoring
- Weighted load balancing
- Round Robin fallback
- Priority-based scheduling
- Real-time dashboard
- Database integration

---

## Author

**Intern Name:** K. Sai Surya Rohith

**Task:** Least Loaded Selection Logic Bug Fix

**Module:** Load Balancing

**Captain:** Nithin Goli 

"# least-loaded-worker-bug-fix" 
