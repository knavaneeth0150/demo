class LoginService:
    def __init__(self):
        # Dummy user database (for demo/testing)
        self.users = {
            "user@example.com": "Password123",
            "admin@example.com": "AdminPass"
        }

    def validate_login(self, email: str, password: str) -> dict:
        """
        Validates user credentials.

        Returns:
            dict: Login result with status and message
        """

        if not email or not password:
            return {
                "status": "failure",
                "message": "Email and password are required"
            }

        if email not in self.users:
            return {
                "status": "failure",
                "message": "User does not exist"
            }

        if self.users[email] != password:
            return {
                "status": "failure",
                "message": "Invalid credentials"
            }

        return {
            "status": "success",
            "message": "Login successful"
        }


# Simple manual test execution
if __name__ == "__main__":
    service = LoginService()

    test_cases = [
        ("user@example.com", "Password123"),
        ("user@example.com", "WrongPass"),
        ("unknown@example.com", "Password123"),
        ("", "")
    ]

    for email, password in test_cases:
        result = service.validate_login(email, password)
        print(f"Test login ({email}): {result}")
