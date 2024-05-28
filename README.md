# Voice Assistant Project

## Introduction

This project is a Python-based voice assistant designed to help you with various tasks through voice commands. The assistant can greet you, open applications, search the web, tell jokes, provide advice, get the latest news, weather updates, and more.

## Features

- **Greetings:** The assistant greets the user based on the time of day.
- **Open Applications:** Commands to open Notepad, Command Prompt, Camera, Calculator, and Discord.
- **Search Capabilities:**
  - Search on Google
  - Search on Wikipedia
  - Play videos on YouTube
- **Communication:**
  - Send WhatsApp messages
  - Send emails
- **Entertainment:**
  - Tell jokes
  - Provide random advice
  - List trending movies
- **Updates:**
  - Get the latest news
  - Get weather updates

## Requirements

- Python 3.x
- Required Python Libraries:
  - `requests`
  - `pyttsx3`
  - `speech_recognition`
  - `decouple`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/voice-assistant.git
   ```

2. Change into the project directory:
   ```bash
   cd voice-assistant
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your configuration:
   ```
   USER=YourName
   BOTNAME=YourBotName
   ```

## Usage

Run the main script to start the voice assistant:
```bash
python main.py
```

The assistant will greet you and wait for your commands. Use any of the supported commands to interact with the assistant.

## Supported Commands

- **Open Applications:**
  - "open notepad"
  - "open discord"
  - "open command prompt" / "open cmd"
  - "open camera"
  - "open calculator"
- **Search:**
  - "search on google"
  - "wikipedia"
  - "youtube"
- **Communication:**
  - "send whatsapp message"
  - "send an email"
- **Entertainment:**
  - "joke"
  - "advice"
  - "trending movies"
- **Updates:**
  - "news"
  - "weather"

## Contribution

Feel free to fork this project, create a feature branch, and submit pull requests. Contributions are always welcome.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Thank you for using the Voice Assistant Project! If you have any questions or issues, please feel free to open an issue on GitHub.
