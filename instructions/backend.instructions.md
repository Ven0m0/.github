---
applyTo: "**/{api,server,routes}/**"
---

# Backend/API Standards

## 🎯 Before Any API Work

**READ**: `.github/skills/api-patterns/SKILL.md`

## 📋 REST Conventions

- Use nouns, not verbs: `/users` not `/getUsers`
- Use plural nouns: `/users` not `/user`
- HTTP methods for actions:
  - `GET` - Read
  - `POST` - Create
  - `PUT/PATCH` - Update
  - `DELETE` - Delete

## 📊 Status Codes

| Code | Meaning       | Use When                  |
| ---- | ------------- | ------------------------- |
| 200  | OK            | Successful GET/PUT/PATCH  |
| 201  | Created       | Successful POST           |
| 204  | No Content    | Successful DELETE         |
| 400  | Bad Request   | Invalid input             |
| 401  | Unauthorized  | Missing/invalid auth      |
| 403  | Forbidden     | Valid auth, no permission |
| 404  | Not Found     | Resource doesn't exist    |
| 422  | Unprocessable | Validation failed         |
| 500  | Server Error  | Our fault                 |

## 🔐 Security Rules

1. **Validate ALL inputs** at API boundary
2. **Use parameterized queries** - never string concat
3. **Hash passwords** with bcrypt or argon2
4. **Rate limit** all endpoints
5. **HTTPS only** in production
6. **Never expose** internal errors to clients

## 🚨 Error Response Format

```toon
error:
  code: VALIDATION_ERROR
  message: User-friendly message
  details[0]:
```

## 📝 Logging

- Log all errors with stack traces
- Include request context (userId, requestId)
- Never log sensitive data (passwords, tokens)
