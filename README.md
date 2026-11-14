# ☕ Cafe Bot: AI Waiter powered by Claude

A command-line chatbot that plays a friendly cafe waiter. It uses the Claude API to understand natural language in any language, remembers the conversation, and saves chat history to a file.

## Features

- 🤖 Natural conversation powered by Claude (`claude-opus-5-5`)
- 🧠 Remembers the conversation: sends the full history with every request
- 🎭 Custom waiter persona via a system prompt
- 💾 Saves chats to `chat_log.txt` and shows previous chats on start
- 🌍 Understands any language

## Tech stack

Python 3, Anthropic Python SDK, python-dotenv

## How to run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo "ANTHROPIC_API_KEY=your-key-here" > .env
python main.py
```

## Example

```
You: coffee please
Waiter: Coming right up! Would you like a fresh croissant to go with it?
You: do you have pizza?
Waiter: Sorry, no pizza here, just coffee, tea and croissants.
```

## What I learned

- How to use API keys and connect Claude to my Python script
- How to keep my API key secret with a `.env` file (and never commit it)
- Why Claude and other LLMs don't remember previous messages: the app has to send the full chat history every time
- Why developers use Git, and how GitHub works

