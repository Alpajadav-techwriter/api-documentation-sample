# Error Codes Reference

The Employee Management API uses standard HTTP status codes to indicate
the success or failure of an API request.

---

## Error Response Format

All error responses follow this structure:

```json
{
  "status": "error",
  "code": 404,
  "message": "Human-readable error description",
  "details": "Additional context about the error (optional)",
  "documentation": "https://api.employeemanager.com/docs/errors#404"
}
```

---

## 2xx - Success Codes

| Code | Status | Description |
|---|---|---|
| 200 | OK | Request completed successfully |
| 201 | Created | Resource created successfully |
| 204 | No Content | Request successful, no content returned (DELETE) |

---

## 4xx - Client Error Codes

| Code | Status | Cause | Resolution |
|---|---|---|---|
| 400 | Bad Request | Invalid or missing request parameters | Check request body and parameters |
| 401 | Unauthorized | Missing or invalid API key | Verify your API key is correct and included |
| 403 | Forbidden | Valid key but insufficient permissions | Request higher permission scope |
| 404 | Not Found | Resource does not exist | Verify the resource ID is correct |
| 409 | Conflict | Duplicate resource already exists | Check for existing record before creating |
| 422 | Unprocessable Entity | Request understood but validation failed | Check field formats and constraints |
| 429 | Too Many Requests | Rate limit exceeded | Wait and retry after the reset window |

---

## 5xx - Server Error Codes

| Code | Status | Cause | Resolution |
|---|---|---|---|
| 500 | Internal Server Error | Unexpected server error | Retry request; contact support if persists |
| 502 | Bad Gateway | Upstream service failure | Retry after a short delay |
| 503 | Service Unavailable | Server temporarily down | Check API status page and retry |
| 504 | Gateway Timeout | Request timed out | Retry with exponential backoff |

---

## Detailed Error Examples

### 400 - Bad Request
```json
{
  "status": "error",
  "code": 400,
  "message": "Bad Request — Missing required field: email",
  "details": "The 'email' field is required when creating an employee record",
  "documentation": "https://api.employeemanager.com/docs/errors#400"
}
```

### 401 - Unauthorized
```json
{
  "status": "error",
  "code": 401,
  "message": "Unauthorized — Invalid API key",
  "details": "The provided API key does not match any active keys",
  "documentation": "https://api.employeemanager.com/docs/errors#401"
}
```

### 404 - Not Found
```json
{
  "status": "error",
  "code": 404,
  "message": "Employee with ID 999 not found",
  "details": "No employee record exists with the specified ID",
  "documentation": "https://api.employeemanager.com/docs/errors#404"
}
```

### 429 - Too Many Requests
```json
{
  "status": "error",
  "code": 429,
  "message": "Too Many Requests — Rate limit exceeded",
  "details": "You have exceeded 1000 requests per hour",
  "retryAfter": 3600,
  "documentation": "https://api.employeemanager.com/docs/errors#429"
}
```

---

## Best Practices for Error Handling

- Always check the HTTP status code before processing the response body
- Log error responses with the full `details` field for easier debugging
- Implement **exponential backoff** for 429 and 5xx errors
- Do not retry on 4xx errors without fixing the underlying issue first
- Monitor the `retryAfter` field in 429 responses before retrying
