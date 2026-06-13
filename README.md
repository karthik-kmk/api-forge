# APIForge

APIForge is a modular API Platform built with **FastAPI**, **PostgreSQL**, and **Kong API Gateway**.

It enables developers to:

* Sign up and authenticate with JWT
* Generate and manage API Keys
* Discover available capabilities
* Consume APIs securely using API Keys
* Track API usage
* View analytics
* Access APIs through Kong API Gateway with rate limiting

---

## Architecture

<p align="center">
  <img src="./assets/architecture.png" alt="APIForge Architecture" width="900"/>
</p>

---

## Tech Stack

| Layer              | Technology                  |
| ------------------ | --------------------------- |
| Backend            | FastAPI                     |
| Database           | PostgreSQL                  |
| ORM                | Async SQLAlchemy 2.0        |
| Authentication     | JWT                         |
| API Keys           | SHA256 Hashed Keys          |
| API Gateway        | Kong 3.8                    |
| Containerization   | Docker Compose              |
| OCR                | Tesseract OCR               |
| PDF Generation     | ReportLab                   |
| Email Validation   | email-validator + dnspython |
| Website Screenshot | Playwright                  |

---

## Features

### Authentication

* User Signup
* User Login
* JWT Authentication
* Current User API

Endpoints:

```http
POST /auth/signup

POST /auth/login

GET /auth/me
```

---

### API Key Management

* Generate API Keys
* List API Keys
* Revoke API Keys
* SHA256 Key Hashing

Endpoints:

```http
POST   /api-keys

GET    /api-keys

DELETE /api-keys/{id}
```

Example API Key:

```text
apiforge_live_xxxxxxxxxxxxxxxxx
```

Stored as:

```text
SHA256(api_key)
```

---

### Capability Registry

APIForge supports dynamic capability discovery.

Endpoints:

```http
POST /capabilities

GET /capabilities

GET /capabilities/{id}

PATCH /capabilities/{id}/activate

PATCH /capabilities/{id}/deactivate
```

---

## Available Capabilities

| Capability         | Endpoint           | Authentication |
| ------------------ | ------------------ | -------------- |
| OCR                | `/v1/ocr/extract`  | API Key        |
| PDF Generation     | `/v1/pdf/generate` | API Key        |
| Email Validation   | `/v1/email/verify` | API Key        |
| Website Screenshot | `/v1/screenshot`   | API Key        |

---

## OCR API

Extract text from images.

```http
POST /v1/ocr/extract
```

Uses:

* pytesseract
* Pillow
* OpenCV

Response:

```json
{
  "text": "Hello World"
}
```

---

## PDF Generation API

Generate PDFs dynamically.

```http
POST /v1/pdf/generate
```

Uses:

* ReportLab

Response:

```text
application/pdf
```

---

## Email Validation API

Validate email addresses.

```http
POST /v1/email/verify
```

Checks:

* Syntax Validation
* MX Record Validation
* Disposable Email Detection

Example Response:

```json
{
  "email":"john@gmail.com",

  "valid_syntax": true,

  "mx_found": true,

  "disposable": false,

  "is_valid": true
}
```

---

## Website Screenshot API

Capture website screenshots using Playwright.

```http
POST /v1/screenshot
```

Example Request:

```json
{
  "url":"https://example.com",

  "full_page": true,

  "width": 1280,

  "height": 720
}
```

Response:

```text
image/png
```

Security:

* Blocks localhost
* Blocks private IPs
* Blocks file:// URLs
* Prevents SSRF attacks

---

## API Key Authentication

Capability APIs are protected using API Keys.

Flow:

```text
Read x-api-key

↓

Hash API Key

↓

Lookup api_keys table

↓

Validate Active

↓

Return APIKey
```

The authenticated API key is stored in:

```python
request.state.api_key
```

---

## Usage Tracking

APIForge automatically tracks API usage using middleware.

Tracked Fields:

* API Key
* Endpoint
* Method
* Status Code
* Latency
* Timestamp

Tracked capabilities:

* OCR
* PDF Generation
* Email Validation
* Website Screenshot
* Future Capabilities

---

## Analytics

Analytics APIs are protected using JWT.

Endpoints:

```http
GET /analytics/usage

GET /analytics/top-capabilities

GET /analytics/request-volume
```

Example:

```json
{
  "total_requests": 120,

  "ocr_requests": 50,

  "pdf_requests": 30,

  "email_requests": 20,

  "screenshot_requests": 20
}
```

---

## Kong API Gateway

APIForge uses Kong Gateway in **DB-less mode**.

Responsibilities:

* Routing
* Rate Limiting
* Gateway Policies

Configured Routes:

```text
/auth

/api-keys

/capabilities

/analytics

/v1/ocr

/v1/pdf

/v1/email

/v1/screenshot
```

---

## Rate Limiting

Implemented using Kong Rate Limiting Plugin.

Example:

```yaml
plugins:

  - name: rate-limiting

    config:

      minute: 5

      policy: local
```

After exceeding the limit:

```text
429 Too Many Requests
```

---

## Project Structure

```text
APIForge/

.devcontainer/

services/

├── apiforge/

│   ├── app/

│   ├── auth/

│   ├── api_keys/

│   ├── capabilities/

│   ├── ocr/

│   ├── pdf/

│   ├── email_validation/

│   ├── screenshot/

│   ├── usage/

│   ├── analytics/

│   ├── core/

│   ├── db/

│   ├── models/

│   └── main.py

│

└── kong/

    └── kong.yml


docker-compose.yml
```

---

## Running Locally

Clone:

```bash
git clone <repo-url>

cd APIForge
```

Start Services:

```bash
docker compose up --build -d
```

Available Services:

| Service    | URL                        |
| ---------- | -------------------------- |
| FastAPI    | http://localhost:8000      |
| Swagger UI | http://localhost:8000/docs |
| Kong Proxy | http://localhost:8080      |
| Kong Admin | http://localhost:8001      |

---



APIForge is a complete API Platform MVP featuring JWT authentication, API keys, capability discovery, OCR, PDF generation, email validation, website screenshots, analytics, and Kong API Gateway integration.
