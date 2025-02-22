# WhatsApp Trigger - News Fetching and Email System

## Overview
This system integrates a WhatsApp trigger to fetch the latest news from India. Upon receiving a command like "send an email to abc@gmail.com," it:
1. Fetches the latest news.
2. Uses the Groq chat model to rank the top 5 news stories.
3. Generates an email message with the news content.
4. Sends the email to a Gmail address.

Additionally, the system uses the DeepSeek model for ranking and news message generation.

## Features
- **WhatsApp Integration**: Trigger actions through WhatsApp messages.
- **Groq Model**: Self-ranks top 5 news articles based on relevance using the Groq chat model.
- **DeepSeek Model**: Generates the message content for email.
- **Email Sending**: Sends the generated news summary to a specified Gmail account.
- **News Source**: Latest news from India.

## Technologies Used
- **WhatsApp**: For receiving messages and triggering actions.
- **Groq**: For ranking the top 5 news stories.
- **DeepSeek**: For generating the email message content.
- **Gmail API**: For sending emails.
- **Supabase**: For database storage.

## Setup Instructions
1. Clone this repository:
   ```
   git clone <repository-url>
   ```
2. Install dependencies:
  ```
  pip install -r requirements.txt
  ```
