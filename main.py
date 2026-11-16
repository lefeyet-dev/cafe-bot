from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

SYSTEM = "You are a friendly waiter in a small cafe. We sell coffee, tea and croissants. Answer in 1-2 short sentences."

def make_reply(notebook):
    reply = ""
    with client.messages.stream(
        model="claude-opus-5-5",
        max_tokens=16000,
        system=SYSTEM,
        messages=notebook,
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            reply += text
        response = stream.get_final_message()    
    print()
    print(f"[tokens: in {response.usage.input_tokens}, out {response.usage.output_tokens}]")
    return reply
        
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
    notebook.append({"role": "user", "content": text})  
    print("Waiter: ", end="", flush=True)        # 1️⃣ сначала записать
    reply = make_reply(notebook)                                 # 2️⃣ потом спросить Claude
    
    notebook.append({"role": "assistant", "content": reply})
print("--- Notebook ---")
with open("chat_log.txt", "a") as file:
    for entry in notebook:
        file.write(f"{entry['role']}: {entry['content']}\n")
        print(f"{entry['role']}: {entry['content']}")


    
        
