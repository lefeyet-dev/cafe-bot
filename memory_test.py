from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()


def ask(messages):
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=16000,
        messages=messages,
    )
    for block in response.content:
        if block.type == "text":
            return block.text


# Request 1
reply1 = ask([{"role": "user", "content": "Hi! My name is Alex."}])
print(reply1)
print("-----")

# Request 2
print(ask([
    {"role": "user", "content": "Hi! My name is Alex."},
    {"role": "assistant", "content": reply1},
    {"role": "user", "content": "What is my name?"},
]))
