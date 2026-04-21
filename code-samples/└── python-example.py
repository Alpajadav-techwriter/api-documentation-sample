# Employee Management API — Python Code Samples

import requests
import json

# ─────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────
BASE_URL = "https://api.employeemanager.com/v1"
API_KEY = "YOUR_API_KEY"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# ─────────────────────────────────────────
# GET — Retrieve All Employees
# ─────────────────────────────────────────
def get_all_employees(department=None, is_active=None):
    params = {}
    if department:
        params["department"] = department
    if is_active is not None:
        params["isActive"] = is_active

    response = requests.get(
        f"{BASE_URL}/employees",
        headers=HEADERS,
        params=params
    )

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.json()['message']}")
        return None

# ─────────────────────────────────────────
# GET — Retrieve Single Employee
# ─────────────────────────────────────────
def get_employee(employee_id):
    response = requests.get(
        f"{BASE_URL}/employees/{employee_id}",
        headers=HEADERS
    )

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print(f"Employee {employee_id} not found")
        return None
    else:
        print(f"Error {response.status_code}: {response.json()['message']}")
        return None

# ─────────────────────────────────────────
# POST — Create New Employee
# ─────────────────────────────────────────
def create_employee(name, department, email, age):
    payload = {
        "name": name,
        "department": department,
        "email": email,
        "age": age
    }

    response = requests.post(
        f"{BASE_URL}/employees",
        headers=HEADERS,
        data=json.dumps(payload)
    )

    if response.status_code == 201:
        print(f"Employee created successfully. ID: {response.json()['id']}")
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.json()['message']}")
        return None

# ─────────────────────────────────────────
# PATCH — Update Employee Department
# ─────────────────────────────────────────
def update_employee_department(employee_id, new_department):
    payload = {
        "department": new_department
    }

    response = requests.patch(
        f"{BASE_URL}/employees/{employee_id}",
        headers=HEADERS,
        data=json.dumps(payload)
    )

    if response.status_code == 200:
        print(f"Employee {employee_id} department updated successfully")
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.json()['message']}")
        return None

# ─────────────────────────────────────────
# DELETE — Remove Employee
# ─────────────────────────────────────────
def delete_employee(employee_id):
    response = requests.delete(
        f"{BASE_URL}/employees/{employee_id}",
        headers=HEADERS
    )

    if response.status_code == 204:
        print(f"Employee {employee_id} deleted successfully")
        return True
    else:
        print(f"Error {response.status_code}: {response.json()['message']}")
        return False

# ─────────────────────────────────────────
# Example Usage
# ─────────────────────────────────────────
if __name__ == "__main__":

    # Get all Engineering employees
    employees = get_all_employees(department="Engineering", is_active=True)
    print(employees)

    # Get specific employee
    employee = get_employee(101)
    print(employee)

    # Create new employee
    new_employee = create_employee(
        name="Sneha Reddy",
        department="Marketing",
        email="sneha@company.com",
        age=25
    )

    # Update department
    update_employee_department(101, "Finance")

    # Delete employee
    delete_employee(103)
