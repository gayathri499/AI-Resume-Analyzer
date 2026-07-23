from werkzeug.security import generate_password_hash, check_password_hash
from database import add_user, get_user_by_email


def register(username, email, password):
    """
    Register a new user.
    Returns:
        (True, "Success") on success
        (False, "Error message") on failure
    """

    # Check if email already exists
    existing_user = get_user_by_email(email)

    if existing_user:
        return False, "Email already registered."

    # Hash password
    hashed_password = generate_password_hash(password)

    # Save user
    success = add_user(username, email, hashed_password)

    if success:
        return True, "Registration successful."

    return False, "Registration failed."


def login(email, password):
    """
    Login user.

    Returns:
        user object on success
        None on failure
    """

    user = get_user_by_email(email)

    if user is None:
        return None

    if check_password_hash(user["password"], password):
        return user

    return None