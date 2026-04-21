# Getting Started with the Employee Management API

This guide helps you make your first API call in under 5 minutes.

---

## Prerequisites

Before you begin, ensure you have:
- A valid API key (see [Authentication](authentication.md))
- A REST client such as Postman or cURL installed
- Basic understanding of REST APIs and JSON

---

## Base URL

All API requests are made to the following base URL:

```
https://api.employeemanager.com/v1
```

---

## Step 1 — Get Your API Key

1. Log in to the **Developer Portal** at `https://developer.employeemanager.com`
2. Navigate to **Settings → API Keys**
3. Click **Generate New Key**
4. Copy and store your key securely — it will not be shown again

---

## Step 2 — Make Your First API Call

Retrieve a list of all employees:

**Using cURL:**
```bash
curl -X GET "https://api.employeemanager.com/v1/employees" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

**Using Python:**
```python
import requests

headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

response = requests.get(
    "https://api.employeemanager.com/v1/employees",
    headers=headers
)

print(response.json())
```

---

## Step 3 — Understand the Response

A successful response returns HTTP status `200 OK` with the following JSON:

```json
{
  "status": "success",
  "count": 3,
  "employees": [
    {
      "id": 101,
      "name": "Rahul Sharma",
      "department": "Engineering",
      "isActive": true
    },
    {
      "id": 102,
      "name": "Priya Mehta",
      "department": "HR",
      "isActive": true
    },
    {
      "id": 103,
      "name": "Arjun Reddy",
      "department": "Finance",
      "isActive": false
    }
  ]
}
```

---

## Step 4 — Handle Errors

If your request fails, the API returns an error response:

```json
{
  "status": "error",
  "code": 401,
  "message": "Unauthorized — Invalid or missing API key",
  "documentation": "https://api.employeemanager.com/docs/errors#401"
}
```

See [Error Codes](error-codes.md) for a complete list of errors and resolutions.

---

## Next Steps

- 📖 Read the [Authentication Guide](authentication.md)
- 📡 Explore all [API Endpoints](endpoints/)
- 💻 View [Code Samples](code-samples/) in Python, JavaScript, and cURL
- 📋 Check [Rate Limits](rate-limits.md)
