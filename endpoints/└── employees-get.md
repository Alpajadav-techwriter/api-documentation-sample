# GET Endpoints - Employee Resource

---

## GET /v1/employees

Retrieves a list of all employees.

**Endpoint:**
```
GET https://api.employeemanager.com/v1/employees
```

### Query Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| department | string | No | Filter by department name |
| isActive | boolean | No | Filter by active status (true/false) |
| page | integer | No | Page number for pagination (default: 1) |
| limit | integer | No | Results per page, max 100 (default: 20) |

### Sample Request

```bash
curl -X GET "https://api.employeemanager.com/v1/employees?department=Engineering&isActive=true" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Sample Response — 200 OK

```json
{
  "status": "success",
  "count": 2,
  "page": 1,
  "totalPages": 1,
  "employees": [
    {
      "id": 101,
      "name": "Rahul Sharma",
      "department": "Engineering",
      "email": "rahul@company.com",
      "isActive": true,
      "createdAt": "2024-01-15T09:00:00Z"
    },
    {
      "id": 104,
      "name": "Meera Iyer",
      "department": "Engineering",
      "email": "meera@company.com",
      "isActive": true,
      "createdAt": "2024-03-20T10:30:00Z"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|---|---|---|
| status | string | Request status — success or error |
| count | integer | Number of results returned |
| page | integer | Current page number |
| totalPages | integer | Total number of pages |
| employees | array | List of employee objects |
| id | integer | Unique employee identifier |
| name | string | Full name of the employee |
| department | string | Department name |
| email | string | Work email address |
| isActive | boolean | Whether the employee is currently active |
| createdAt | string | ISO 8601 timestamp of record creation |

---

## GET /v1/employees/{id}

Retrieves details of a single employee by ID.

**Endpoint:**
```
GET https://api.employeemanager.com/v1/employees/{id}
```

### Path Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| id | integer | Yes | Unique employee identifier |

### Sample Request

```bash
curl -X GET "https://api.employeemanager.com/v1/employees/101" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Sample Response — 200 OK

```json
{
  "id": 101,
  "name": "Rahul Sharma",
  "age": 30,
  "department": "Engineering",
  "designation": "Senior Software Engineer",
  "email": "rahul@company.com",
  "phone": "+91-9876543210",
  "address": {
    "city": "Hyderabad",
    "state": "Telangana",
    "country": "India",
    "pincode": "500001"
  },
  "skills": ["Python", "Java", "REST APIs"],
  "isActive": true,
  "joiningDate": "2022-06-01",
  "createdAt": "2022-06-01T09:00:00Z",
  "updatedAt": "2024-01-10T14:30:00Z"
}
```

### Error Responses

| Status Code | Message | Description |
|---|---|---|
| 401 | Unauthorized | Invalid or missing API key |
| 404 | Not Found | Employee with specified ID does not exist |
| 500 | Internal Server Error | Unexpected server-side error |

### 404 Error Example

```json
{
  "status": "error",
  "code": 404,
  "message": "Employee with ID 999 not found",
  "documentation": "https://api.employeemanager.com/docs/errors#404"
}
```
