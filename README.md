WhatsApp Trigger - News Fetching and Email System
Overview
This system integrates a WhatsApp trigger to fetch the latest news from India. Upon receiving a command like "send an email to abc@gmail.com," it:

Fetches the latest news.
Uses the Groq chat model to rank the top 5 news stories.
Generates an email message with the news content.
Sends the email to a Gmail address.
Additionally, the system uses the DeepSeek model for ranking and news message generation.

Features
WhatsApp Integration: Trigger actions through WhatsApp messages.
Groq Model: Self-ranks top 5 news articles based on relevance using the Groq chat model.
DeepSeek Model: Generates the message content for email.
Email Sending: Sends the generated news summary to a specified Gmail account.
News Source: Latest news from India.
Technologies Used
WhatsApp: For receiving messages and triggering actions.
Groq: For ranking the top 5 news stories.
DeepSeek: For generating the email message content.
Gmail API: For sending emails.
Supabase: For database storage.
Setup Instructions
Clone this repository:

bash
Copy
Edit
git clone <repository-url>
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up your environment variables:

WhatsApp API credentials
Gmail API credentials (for sending emails)
Groq API credentials
Supabase URL and API key
Configure the trigger command in WhatsApp (e.g., "send an email to abc@gmail.com").

To Run the application in local:

bash
Copy
Edit
python app.py
Usage
Send a WhatsApp message with the command "send an email to abc@gmail.com."
The system will fetch the latest news from India, rank the top 5 stories using Groq, and generate an email message.
The email will be sent to the specified address (e.g., abc@gmail.com).
Video Recording
For a demonstration of how this system works, check out the video recording:

[Video Recording Link]

License
This project is licensed under the MIT License - see the LICENSE file for details.
