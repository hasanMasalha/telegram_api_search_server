# telegram_api_search_server
# Fastapi Server

This server provides endpoints for searching Telegram groups by `keyword`.

# Installation and Setup

1. **Environment Variables:**
  - Create an `.env` file in the root directory of your project.
  - Add the following environment variables:
      - `API_ID`: The API ID for accessing the Telegram API.
      - `API_HASH`: The API hash for accessing the Telegram API.

    **WARNING:** Ensure the `.env` file is listed in your `.gitignore` to prevent it from being included in your version control system, such as GitHub.

    You can obtain these values from the [Telegram Credentials Generator](https://my.telegram.org/auth). For more details, refer to [Obtaining API ID](https://core.telegram.org/api/obtaining_api_id). A phone number is required to acquire these credentials.

2. **Install Dependencies:**

    Run the following command to install the required Python packages:
    ```shell
    pip install -r requirements.txt
    ```


# Packages Used

- `Telethon`: A library for interacting with Telegram's API, used here to fetch users from a specific group for search functionality.

# Running The Server

To start the FastAPI server, use the following command:
```shell
uvicorn server:app
```
