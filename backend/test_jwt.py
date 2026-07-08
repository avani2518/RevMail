from app.core.jwt import create_access_token, decode_access_token

token = create_access_token(
    {
        "sub": "12345",
        "email": "avani@gmail.com"
    }
)

print("TOKEN")
print(token)

print()

payload = decode_access_token(token)

print("PAYLOAD")
print(payload)