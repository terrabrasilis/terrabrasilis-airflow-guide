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


### 1. Define the Path in Your DAG

In your DAG file, define the path to your virtualenv, you don't need to create it in your environment beforehand, as Airflow will automatically handle its creation during execution.:

```python
venv_path = "/opt/airflow/venv/inpe/pantanal_deter_cmask_data_flow/venv"
```

### 2. Difine the requirements

It is necessary to store all the parameters required for the DAG execution in a local variable, so that Airflow can properly install the dependencies during execution.

```python
requirements = [
    "requests",
    "psycopg2-binary",
    "geopandas==0.13.2",
    "fiona==1.9.6",
    "geoalchemy2",
    "rasterstats",
    "libpysal",
    "beautifulsoup4",
    "rasterio",
    "apache-airflow==2.10.5"
]
```

### 3. Use the `PythonVirtualenvOperator` in Tasks

You can now create tasks using the operator. 
In the first call to the PythonVirtualenvOperator, you need 
to provide the requirements parameter so that Airflow can 
install the previously defined packages:

```python
task_1 = PythonVirtualenvOperator(
    task_id="1_trigger_task",
    requirements=requirements,
    python_callable=task_callable_01,
    system_site_packages=True,
    op_kwargs={"biome": biome},
    venv_cache_path=venv_path
)
```

In subsequent calls to the PythonVirtualenvOperator, 
it will no longer be necessary to pass the requirements 
parameter, as all dependencies will have already been 
installed in the virtual environment, which will be 
reused in the following calls.

```python
task_2 = PythonVirtualenvOperator(
    task_id='2_create_tables_task',
    python_callable=task_callable_02,
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

