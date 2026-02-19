Restaurant FAQ Bot
Overview

Restaurant FAQ Bot is an AI-powered conversational assistant built using Streamlit and the Groq API. The application compresses restaurant menu data once per session and uses a large language model to answer customer queries efficiently.

The system is designed to reduce repetitive customer inquiries related to pricing, dietary preferences, allergens, and food recommendations while maintaining fast response times.

Key Features

One-time menu compression using an LLM

Session-based caching to reduce API calls

Natural language FAQ handling

Mood-based recommendation engine

Response time measurement

Secure API key handling using environment variables

Free-tier Groq model integration

System Architecture

Raw Menu (Text File)
→ LLM Compression (Executed Once Per Session)
→ Stored in Streamlit Session State
→ User Query
→ Groq Chat Completion API
→ Intelligent Response

Tech Stack

Python

Streamlit

Groq API

Llama 3.1 Model

Session State Caching

Project Structure
restaurant_faq_bot/
│
├── app.py
├── config.py
├── requirements.txt
│
└── data/
    └── raw_menu.txt

Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/restaurant-faq-bot.git
cd restaurant-faq-bot


Install dependencies:

pip install -r requirements.txt

API Configuration

Create a Groq account at:

https://console.groq.com

Generate an API key.

Set the API key as an environment variable.

For Windows (PowerShell):

setx GROQ_API_KEY "your_api_key_here"


Restart the terminal after setting the variable.

For macOS/Linux:

export GROQ_API_KEY="your_api_key_here"


The application reads the key securely using environment variables. No API keys are stored in the repository.

Running the Application

Start the Streamlit server:

streamlit run app.py


The application will open in your browser.

Performance Characteristics

Approximately 70–80% menu token reduction through compression

Compression executed only once per session

Reduced repeated API calls

Sub-second average response time

Accurate handling of dietary and allergen-related queries

Use Cases

Restaurant customer self-service assistant

Digital menu exploration system

Hospitality automation tool

AI-driven recommendation interface

Future Enhancements

Reservation booking integration

Order placement workflow

Persistent compression cache (file-based)

Vector-based retrieval system (RAG)

Administrative analytics dashboard

Cloud deployment and containerization
