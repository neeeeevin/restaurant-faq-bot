# Restaurant FAQ Bot

An AI-powered restaurant assistant built with Streamlit and Groq’s LLM API.  
The system compresses menu data once per session and answers customer queries using a fast, large language model.

---

## Overview

Restaurant FAQ Bot is designed to automate common customer inquiries related to:

- Dietary preferences  
- Allergen information  
- Pricing  
- Menu exploration  
- Personalized food recommendations  

The application optimizes API usage by compressing the menu once and caching it in session memory for subsequent queries.

---

## Features

- One-time menu compression using Groq LLM
- Session-based caching to reduce API cost
- Natural language FAQ handling
- Mood-based recommendation engine
- Sub-second response times
- Secure API key management via environment variables

---

## System Architecture

Raw Menu (Text File)  
→ LLM Compression (Executed Once Per Session)  
→ Stored in Session State  
→ User Query  
→ Groq Chat Completion API  
→ Context-Aware Response  

---

## Tech Stack

- Python
- Streamlit
- Groq API
- Llama 3.1 Model
- Session State Caching

---

## Project Structure

restaurant_faq_bot/
│
├── app.py
├── config.py
├── requirements.txt
│
└── data/
    └── raw_menu.txt

---

## Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/restaurant-faq-bot.git
cd restaurant-faq-bot

Install dependencies:

pip install -r requirements.txt

---

## API Configuration

1. Create a Groq account at:
   https://console.groq.com

2. Generate an API key.

3. Set the API key as an environment variable.

For Windows (PowerShell):

setx GROQ_API_KEY "your_api_key_here"

Restart your terminal after setting it.

For macOS/Linux:

export GROQ_API_KEY="your_api_key_here"

The application securely reads the key from the environment.  
No credentials are stored in the repository.

---

## Running the Application

Start the Streamlit server:

streamlit run app.py

The application will open in your browser automatically.

---

## Performance Characteristics

- ~70–80% reduction in menu token size after compression
- Compression executed only once per session
- Reduced repeated API calls
- Fast response latency using Groq inference
- Accurate handling of dietary and allergen queries

---

## Use Cases

- Digital restaurant assistants
- Hospitality automation systems
- AI-based menu exploration
- Customer self-service interfaces

---

## Future Improvements

- Reservation system integration
- Order placement workflow
- Persistent compression cache
- Vector-based retrieval (RAG)
- Admin analytics dashboard
- Cloud deployment support
