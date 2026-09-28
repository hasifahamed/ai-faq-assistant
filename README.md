# AI FAQ Assistant

A simple project where you ask a question and it gives the best answer
from an FAQ database. If it does not know, it says so.

## What it does

- You type a question in the chat page.
- The backend searches the FAQ database by meaning.
- It replies with the matching answer.
- If nothing matches, it says "Sorry, I don't know the answer to that question."

## Built with

Python, Flask, SQLite, HTML/CSS/JavaScript, sentence-transformers

## How to run

1. Download the project:
   git clone https://github.com/hasifahamed/ai-faq-assistant
2. Go into the folder:
   cd ai-faq-assistant
3. Create a virtual environment:
   python -m venv venv
4. Activate it (Windows):
   venv\Scripts\activate
5. Install packages:
   pip install -r requirements.txt
6. Start the server:
   python app.py
7. Open http://127.0.0.1:5000  in your browser.

Note: the first question may take a few seconds while the AI model loads.