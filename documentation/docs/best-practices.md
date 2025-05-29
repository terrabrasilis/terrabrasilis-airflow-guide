
# Best Practices for Airflow Tasks

This section outlines the recommended best practices for designing and developing Airflow DAGs and tasks within the **TerraBrasilis** project. Following these guidelines ensures a consistent, maintainable, and scalable workflow structure.

---

## 🧮 Airflow Variables

Airflow Variables are useful for storing configuration values and secrets that might change between environments or deployments. To ensure consistency and clarity across all DAGs, the following conventions must be followed.

---

### 📚 Managing Variables via the UI

To add or edit variables via the Airflow web UI:

1. Navigate to **Admin** > **Variables**.
2. Click **Create** to add a new variable.
3. Enter the **Key** (name), and the **Value** (string or JSON).
4. Fill in the **Description** field with a brief explanation of the variable’s purpose.
5. Click **Save**.

---

### 🔧 Accessing Variables

You can access Airflow variables using the `Variable` class:

```python
from airflow.models import Variable

# Access a variable
value = Variable.get("MY_VARIABLE_NAME")

# Access a variable with a default value
value = Variable.get("MY_VARIABLE_NAME", default_var="default_value")

# Access and parse a JSON-formatted variable
config = Variable.get("MY_JSON_VARIABLE", deserialize_json=True)
```

---

### 📌 Naming Conventions

All Airflow variables must follow these naming rules:

- ✅ Use **English** for all variable names.
- ✅ Use **UPPERCASE** letters only.
- ✅ Use **underscores (`_`)** to separate words.
- ✅ Always include a **reference to the DAG name or acronym** as a prefix, to indicate where the variable is used.
- ✅ Always fill in the **Description** field with a brief explanation of the variable's purpose and where it is used.

#### ✅ Good Examples

| Variable Name                | Description                                           |
|-----------------------------|-------------------------------------------------------|
| `RISKDB_CMASK_SATELLITES`   | Used in the `riskdb` DAG to configure satellite list |
| `PRODES_EXPORT_FOLDER_PATH` | Used in the `prodes` DAG to define export folder     |
| `DEFORESTATION_API_TOKEN`   | Token used by deforestation DAG                      |

#### ❌ Bad Examples (to avoid)

| Variable Name     | Issue                                     |
|-------------------|--------------------------------------------|
| `satelliteList`   | Not uppercase, not in English              |
| `list_sat`        | No reference to DAG                        |
| `prodespath`      | Unclear meaning, not readable              |

---

### 🧼 Tips for Using Variables

- Prefer **Airflow Connections** or **secrets backends** for sensitive information like passwords or tokens.
- Keep variables **centralized and consistent** across environments. You can use the **Import/Export JSON** feature in the UI.

---

## 🔗 Airflow Connections

Airflow Connections are used to securely store credentials and connection details (such as host, port, username, password, API tokens) for external systems. They help avoid hardcoding sensitive data directly in DAGs or code.

---

### 🔧 Accessing Connections

To view and manage Connections in the Airflow Web UI:

1. Go to **Admin** > **Connections**.
2. Here you will see a list of existing connections.
3. Click **Create** to add a new connection or click on an existing one to edit it.
4. Fill in the required fields: **Conn Id**, **Conn Type**, **Host**, **Login**, **Password**, **Port**, **Schema**, and **Extra**.
5. Fill in the **Description** field with a brief explanation of the connection’s purpose.
6. Click **Save**.

---

### 📌 Naming Conventions

All Airflow connections must follow these naming rules:

- ✅ Use **English** for all connection IDs (`Conn Id`).
- ✅ Use **UPPERCASE** letters only.
- ✅ Use **underscores (`_`)** to separate words.
- ✅ Always include a **reference to the DAG name or acronym** as a prefix to indicate where the connection is used.
- ✅ Always fill in the **Description** field explaining the connection’s purpose and where it is used.

#### ✅ Good Examples

| Conn Id                      | Description                                         |
|------------------------------|-----------------------------------------------------|
| `RISKDB_POSTGRES`             | Postgres database connection for `riskdb` DAG       |
| `PRODES_S3_BUCKET`            | AWS S3 bucket connection used by `prodes` DAG       |
| `DEFORESTATION_API_SERVICE`   | API service connection for `deforestation` DAG      |

#### ❌ Bad Examples (to avoid)

| Conn Id            | Issue                                        |
|--------------------|-----------------------------------------------|
| `postgres`         | No DAG reference, too generic                  |
| `s3bucket`         | Not uppercase, no underscores                  |
| `deforestationapi` | No separators, unclear meaning                  |
| *(no description)* | Missing description reduces clarity            |

---

### 🧼 Tips for Managing Connections

- Avoid hardcoding credentials in DAGs or variables; use Connections instead.
- Use the **Extra** field to store JSON-formatted parameters when needed.
- Keep connections centralized and documented with clear descriptions.
- Use different connections for different environments (dev, staging, prod) with consistent naming prefixes.
- Regularly audit connections to remove unused or expired credentials.