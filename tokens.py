from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()


response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    messages=[{"role": "user", "content": "Say hi in 3 words!"}],
)
print(response.usage.input_tokens)
print(response.usage.output_tokens)
input_cost = response.usage.input_tokens * 4 / 1000000
output_cost = response.usage.output_tokens * 20 / 1000000
print(f"Cost: ${input_cost + output_cost}")
