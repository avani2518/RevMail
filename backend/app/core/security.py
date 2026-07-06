from passlib.context import CryptContext

# Configure bcrypt as the hashing algorithm
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    """
    Convert a plain password into a secure hash.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify whether a plain password matches its stored hash.
    """
    return pwd_context.verify(plain_password, hashed_password)