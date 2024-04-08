import google.generativeai as palm
import signal
def handle_interrupt(sig, frame):
    """Gracefully exits the program on Ctrl+C press."""
    print("exiting...")
    exit(0)
signal.signal(signal.SIGINT, handle_interrupt) #Register the signal handler
API_KEY = "YOUR_API_KEY"
palm.configure(api_key = API_KEY)
prompt = str(input("Enter your prompt:"))
response=palm.chat(messages=prompt,temperature=0.2,context="Speak like a AI assistance")
for message in response.messages:
    print(message['author'],message['content'])
    
# for message in response.messages:
#     for i in message['content'].split('\n'):
#         if i == "*" or i == "**":
#             continue
#         else:
#             print(i)
