from sqlalchemy import create_engine

url = "postgresql://postgres:Postgres%232026@localhost:5433/revmail_db"

print("Using URL:", url)

engine = create_engine(url)

try:
    with engine.connect() as conn:
        print("✅ Connected successfully!")
except Exception as e:
    print("❌ Error:")
    print(e)