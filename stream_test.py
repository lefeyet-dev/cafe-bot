from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

reply = ""
with client.messages.stream(
    model="claude-opus-5-5",
    max_tokens=16000,
    messages=[{"role": "user", "content": "Write a 5-sentence story about a cafe cat"}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
        reply += text
print()
print("---")
print(len(reply))