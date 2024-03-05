from utils.security import hash_password, check_password


def test_can_hash_password() -> None:
    """
    Make sure that hashing a password with the hash password utility function, and checking it again later
    with the check password function returns true
    """
    password = "password"
    hashed_password, salt = hash_password(password)
    assert check_password(password, salt, hashed_password)

