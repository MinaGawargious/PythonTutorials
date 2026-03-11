import os

# db_user = "my_db_user"
# db_user = "my_db_password_123"

# Use environment variables vs. hard-coded username and password:
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASS")

print(db_user, db_password)