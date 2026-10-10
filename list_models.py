from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

for m in sorted(client.models.list(), key=lambda m: m.id):
    print(m.id)
