from hashlib import sha256
from uuid import uuid4


def hash_password(password: str) -> tuple[str, str]:
    """
    Hash a password using sha256 and a salt

    :param password: The password to hash
    :return: A tuple of hash and salt
    """

    password = password.encode("utf-8")
    salt = uuid4().hex
    hashed_password = sha256(password + salt.encode("utf-8")).hexdigest()
    return hashed_password, salt


def check_password(password: str, salt: str, hashed_password: str) -> bool:
    """
    Check whether a password with its salt matches the hash

    :param password: The plain text password
    :param salt: The salt used to hash the password
    :param hashed_password: The hashed password
    :return: A boolean indicating whether the hash matches the plain-text password
    """

    password = password.encode("utf-8")
    hash_check = sha256(password + salt.encode("utf-8")).hexdigest()
    return hashed_password == hash_check

