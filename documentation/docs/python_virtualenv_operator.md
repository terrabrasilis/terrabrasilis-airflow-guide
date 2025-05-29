# Using `PythonVirtualenvOperator` in TerraBrasilis Airflow DAGs

The `PythonVirtualenvOperator` is useful when your Airflow task requires specific Python dependencies that may not be available in the main Airflow environment. It allows you to run a Python function in a **virtual environment**, isolated from the system packages.

---

## 📥 Importing the Operator

First, make sure to import the operator using:

```python
from airflow.operators.python import PythonVirtualenvOperator
```

---

## ⚙️ Step-by-Step Guide

### 1. Create a Virtual Environment (venv)

Create your virtual environment locally in the desired folder:

```bash
python3 -m venv /opt/airflow/projects/YOUR_PROJECT/venv
```

### 2. Activate the Virtual Environment

Activate the environment to install required dependencies:

```bash
source /opt/airflow/projects/YOUR_PROJECT/venv/bin/activate
```

### 3. Install Required Dependencies

Inside the virtual environment, install the necessary packages:

```bash
pip install pandas requests numpy  # example packages
```

You can also use a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Define the Path in Your DAG

In your DAG file, define the path to your virtualenv:

```python
venv_path = "/opt/airflow/projects/deter_cmask_data_flow/venv"
```

### 5. Use the `PythonVirtualenvOperator` in Tasks

You can now create tasks using the operator:

```python
task_1 = PythonVirtualenvOperator(
    task_id="1_trigger_task",
    python_callable=task_callable_01,
    system_site_packages=True,
    op_kwargs={"biome": biome},
    venv_cache_path=venv_path
)
```

- `python_callable`: your Python function.
- `op_kwargs`: keyword arguments to pass to the function.
- `system_site_packages=True`: allows access to system-wide packages if needed.
- `venv_cache_path`: the path to your virtual environment.

---

## 🔁 Sharing Data with XComs

To pass values between tasks using XComs:

### Return values in your function:

```python
def task_callable_01(biome):
    result = {"satellite": "CBERS", "year": 2024}
    return result
```

### Use `op_kwargs` in dependent tasks:

```python
task_2 = PythonVirtualenvOperator(
    task_id="2_process_result",
    python_callable=task_callable_02,
    op_kwargs={"result": task_1.output},
    venv_cache_path=venv_path
)
```

---

## ✅ Best Practices

- Use a consistent folder structure for virtualenvs inside the `/opt/airflow/projects` directory.
- Keep dependencies lean and versioned.
- Always return structured data (like dictionaries) when using XComs.

