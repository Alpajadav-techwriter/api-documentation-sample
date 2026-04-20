# 📡 REST API Documentation Sample

> A professional API documentation sample demonstrating skills in REST API documentation,
> JSON structure, endpoint documentation, authentication, and error handling.

---

## 📋 Project Overview

This repository contains a complete **REST API documentation sample** for a fictional
**Employee Management API**. It demonstrates industry-standard API documentation
practices used in real software organizations.

## 🎯 Purpose

To showcase:
- REST API documentation skills
- JSON request/response documentation
- Authentication documentation
- Error code documentation
- Code sample writing across multiple languages

## 🛠️ Tools Used

- Markdown for documentation
- Postman for API testing and validation
- Swagger/OpenAPI specification concepts
- JSON for request/response examples

## 📂 Repository Structure

```
api-documentation-sample/
├── README.md                    ← You are here
├── overview.md                  ← API overview and concepts
├── authentication.md            ← Authentication guide
├── getting-started.md           ← Quick start guide
├── rate-limits.md               ← Rate limiting documentation
├── endpoints/
│   ├── employees-get.md         ← GET endpoints
│   ├── employees-post.md        ← POST endpoints
│   ├── employees-put-patch.md   ← PUT and PATCH endpoints
│   └── employees-delete.md      ← DELETE endpoints
├── code-samples/
│   ├── python-example.py        ← Python code sample
│   ├── javascript-example.js    ← JavaScript code sample
│   └── curl-example.sh          ← cURL code sample
├── error-codes.md               ← Complete error reference
└── changelog.md                 ← API version history
```

## 🔑 Key Skills Demonstrated

| Skill | Where to Find It |
|---|---|
| Endpoint documentation | /endpoints/ folder |
| JSON request/response | All endpoint files |
| Authentication | authentication.md |
| Error codes | error-codes.md |
| Code samples | /code-samples/ folder |
| Getting started | getting-started.md |
| Versioning/Changelog | changelog.md |

---

## 📄 Sample — Endpoint Documentation Preview

```
GET /v1/employees/{id}
Returns details of a specific employee by ID.
```

**Path Parameter:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| id | integer | Yes | Unique employee identifier |

**Sample Response:**
```json
{
  "id": 101,
  "name": "Rahul Sharma",
  "department": "Engineering",
  "email": "rahul@company.com",
  "isActive": true
}
```
