import os

if os.path.exists('.env'):
    with open('.env', 'r') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                value = value.strip('"').strip("'")
                os.environ.setdefault(key, value)
    print("Environment variables have been loaded correctly")
else:
    print(
        "The .env file was not found. Please create the .env file in the project root."
        "Or"
        "Make sure you import environment variables directly into the system"
    )

    default_var_env_keys = ["DJANGO_APP_SECRET_KEY", "DJANGO_APP_DEBUG", "DJANGO_APP_DB_NAME", "DJANGO_APP_DB_USER", "DJANGO_APP_DB_PASSWORD", "DJANGO_APP_DB_HOST",
                            "DJANGO_APP_DB_PORT"]

    for var_env_key in default_var_env_keys:
        if not os.environ.get(var_env_key, None):
            raise KeyError(
                f"Please import at least the environment variable. <{var_env_key}>")
