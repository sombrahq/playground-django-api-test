# For more information, https://hurl.dev/


POST {{DJANGO_BASE_URL}}/api/tokens/
{
  "username": "{{DJANGO_SUPERUSER_USERNAME}}",
  "password": "{{DJANGO_SUPERUSER_PASSWORD}}"
}

HTTP 200
[Captures]
token: jsonpath "$['token']"


GET {{DJANGO_BASE_URL}}/api/emails/
Content-Type: application/json
Authorization: Token {{token}}

HTTP 200


POST {{DJANGO_BASE_URL}}/api/emails/
Content-Type: application/json
Authorization: Token {{token}}

{
  "name": "My Emails"
}

HTTP 201
[Captures]
emails: jsonpath "$['url']"
