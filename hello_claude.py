from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    system="You are a friendly waiter in a small cafe. We only sell coffee, tea and croissants. Answer in 1-2 short sentences.",

    messages=[
        {"role": "user", "content": "coffee please"}
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
