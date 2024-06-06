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

    default_var_env_keys = ["BASE_DIR", "SECRET_KEY", "DEBUG", "ALLOWED_HOSTS", "INSTALLED_APPS", "MIDDLEWARE",
                            "ROOT_URLCONF", "TEMPLATES", "DATABASES", "AUTH_PASSWORD_VALIDATORS", "LANGUAGE_CODE", "TIME_ZONE", "USE_I18N"]

    for var_env_key in default_var_env_keys:
        if not os.environ.get(var_env_key, None):
            raise KeyError(
                f"Please import at least the environment variable. <{var_env_key}>")
