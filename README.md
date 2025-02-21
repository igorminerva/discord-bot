# Discord Bot - Fun and Interactive Bot
Welcome to the repository for my Discord bot! This bot is designed to bring fun and interactivity to your Discord server with a variety of commands. It can send playful messages, fetch random dog images, and even share monkey pictures (because why not?).
---
## Features
- **Playful Insults**: The bot responds with lighthearted and humorous messages when triggered.
- **Random Dog Images**: Fetches and sends adorable dog pictures using the [Dog CEO's Dog API](https://dog.ceo/dog-api/).
- **Random Monkey Images**: Fetches and sends random monkey pictures using the [Animals API](https://animals.maxz.dev/).
---
## Commands
Here are the commands you can use with the bot:

- **`!ping`**: The bot responds with a playful and humorous message.
- **`!dog`**: The bot fetches and sends a random dog image.
- **`!alessio` or `!simo`**: The bot fetches and sends a random monkey image.
---
## Setup Instructions
Follow these steps to set up and run the bot on your local machine or server.

### 1. **Prerequisites**
- Python 3.8 or higher installed.
- A Discord bot token. You can create a bot and get the token from the [Discord Developer Portal](https://discord.com/developers/applications).
- Install the required Python libraries.

### 2. **Install Dependencies**
Run the following command to install the required Python libraries:
```bash
pip install discord.py requests python-dotenv
```

### 3. Set Up Environment Variables
Create a .env file in the root directory of your project and add your Discord bot token:
```bash
DISCORD_TOKEN=your_discord_bot_token_here
```
Replace your_discord_bot_token_here with your actual bot token.


### 4. Run the Bot
Execute the bot script using Python:
```bash
python your_bot_script_name.py
```
Replace your_bot_script_name.py with the actual name of your Python file.










