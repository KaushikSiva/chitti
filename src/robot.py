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
GROQ_MODEL = os.getenv("GROQ_MODEL")
HF_API_KEY = os.getenv("HF_API_KEY")
WHATSAPP_PHONE_ID = os.getenv("WHATSAPP_PHONE_ID")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
# Supabase Config
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


N8N_WEBHOOK_URL = os.getenv("N8N_URL")

def send_to_n8n(jokes, email):
    # Prepare the payload to send to n8n
    payload = {
        "jokes": jokes,
        "email": email
    }

    # Send a POST request to the n8n webhook
    response = requests.post(N8N_WEBHOOK_URL, json=payload)
    
    if response.status_code == 200:
        print("Successfully sent to n8n")
    else:
        print(f"Error sending to n8n: {N8N_WEBHOOK_URL},{response.status_code}")


def get_jokes():
    payload = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": "Tell me 5 jokes"}]
    }
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    response = requests.post(GROQ_URL, json=payload, headers=headers)
    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")


from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/webhook", methods=["GET", "POST"])
def whatsapp_webhook():
    if request.method == "GET":
        # WhatsApp webhook verification
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200  # Return the challenge token as required
        return "Forbidden", 403

    elif request.method == "POST":
        # WhatsApp message processing
        data = request.json

        try:
            message_data = data["entry"][0]["changes"][0]["value"]
            if "messages" in message_data:
                message = message_data["messages"][0]["text"]["body"]
                sender = message_data["messages"][0]["from"]
                if "send an email to" in message:
                    email = message.split("send an email to")[-1].strip()
                    jokes = get_jokes()
                    send_to_n8n(jokes, email)
                    # Respond to WhatsApp message
                    send_whatsapp_message(sender, "Sending your jokes via email!")

                # Send a response back to WhatsApp
                send_whatsapp_message(sender, "I only understand 'send an email to XYZ'")

        except KeyError:
            return jsonify({"error": "Invalid message format"}), 400

    return jsonify({"status": "ok"}), 200


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
