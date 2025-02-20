from flask import Flask, request, jsonify
import requests
import os
from supabase import create_client, Client

app = Flask(__name__)
# Load environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_KEY_2 = os.getenv("SUPABASE_KEY_2")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = os.getenv("GROQ_URL")

HF_API_KEY = os.getenv("HF_API_KEY")
WHATSAPP_PHONE_ID = os.getenv("WHATSAPP_PHONE_ID")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")

# Supabase Config
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Groq Config
GROQ_URL = "https://api.groq.com/v1/chat/completions"


def get_jokes():
    payload = {
        "model": "groq-llm",
        "messages": [{"role": "user", "content": "Tell me 5 jokes"}]
    }
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    response = requests.post(GROQ_URL, json=payload, headers=headers)
    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")

@app.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    data = request.json
    if "messages" in data["entry"][0]["changes"][0]["value"]:
        message = data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
        sender = data["entry"][0]["changes"][0]["value"]["messages"][0]["from"]

        # Process message
        if "send an email to" in message:
            email = message.split("send an email to")[-1].strip()
            jokes = get_jokes()
            return jsonify({"email": email, "jokes": jokes})
        
        # Respond to WhatsApp message
        send_whatsapp_message(sender, "I only understand 'send an email to XYZ'")

    return jsonify({"status": "ok"})

def send_whatsapp_message(to, message):
    print("hello")
    url = f"https://graph.facebook.com/v17.0/{WHATSAPP_PHONE_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "text": {"body": message}
    }
    requests.post(url, json=payload, headers=headers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
