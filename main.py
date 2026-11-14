from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

SYSTEM = "You are a friendly waiter in a small cafe. We sell coffee, tea and croissants. Answer in 1-2 short sentences."

def make_reply(notebook):
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=16000,
        system=SYSTEM,
        messages=notebook,
    )
    for block in response.content:
        if block.type == "text":
            return block.text
        
notebook = []
try:
    with open("chat_log.txt", "r") as file:
        old = file.read()
    print("=== Previous chats ===")
    print(old)
    print("======================")
except FileNotFoundError:
    print("No previous chats. This is our first meeting!")

while True:
    text = input("You: ")
    if text == "quit":
        break
    notebook.append({"role": "user", "content": text})          # 1️⃣ сначала записать
    reply = make_reply(notebook)                                 # 2️⃣ потом спросить Claude
    print("Waiter: " + reply)
    notebook.append({"role": "assistant", "content": reply})
print("--- Notebook ---")
with open("chat_log.txt", "a") as file:
    for entry in notebook:
        file.write(f"{entry['role']}: {entry['content']}\n")
        print(f"{entry['role']}: {entry['content']}")


    
        
