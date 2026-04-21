# Authentication

The Employee Management API uses **Bearer Token authentication** to secure all requests.
Every API request must include a valid API key in the request header.

---

## Authentication Methods

### Bearer Token (Recommended)

Include your API key in the `Authorization` header of every request:

```
Authorization: Bearer YOUR_API_KEY
```

**Example:**
```bash
curl -X GET "https://api.employeemanager.com/v1/employees" \
  -H "Authorization: Bearer abc123xyz789"
```

---

### API Key as Query Parameter

Alternatively, pass the API key as a query parameter:

```
GET /v1/employees?api_key=abc123xyz789
```

> ⚠️ **Note:** Using the Authorization header is recommended over query parameters
> for better security, as query parameters may be logged in server logs.

---

## Obtaining an API Key

1. Register at the **Developer Portal**: `https://developer.employeemanager.com`
2. Go to **Account Settings → API Keys**
3. Click **Create New API Key**
4. Assign a name and permission scope to the key
5. Copy the key immediately — it is shown only once

---

## Permission Scopes

| Scope | Access Level | Description |
|---|---|---|
| `read:employees` | Read only | GET requests only |
| `write:employees` | Read and write | GET, POST, PUT, PATCH |
| `admin:employees` | Full access | All methods including DELETE |

---

## Token Expiry and Renewal

- API keys do **not expire** unless manually revoked
- If a key is compromised, revoke it immediately from the Developer Portal
- Generate a new key and update all integrations

---

## Authentication Errors

| Error Code | Message | Resolution |
|---|---|---|
| 401 | Unauthorized | Missing or invalid API key |
| 403 | Forbidden | Valid key but insufficient permissions |

**401 Response Example:**
```json
{
  "status": "error",
  "code": 401,
  "message": "Unauthorized — Invalid or missing API key",
  "documentation": "https://api.employeemanager.com/docs/errors#401"
}
```

---

## Security Best Practices

- 🔒 Never expose your API key in client-side code or public repositories
- 🔒 Store API keys in environment variables, not hardcoded in source code
- 🔒 Use separate API keys for development, staging, and production environments
- 🔒 Rotate API keys periodically as part of security hygiene
- 🔒 Restrict API key permissions to only the scopes your application needs
