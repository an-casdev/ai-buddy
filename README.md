# 👁️ AI Buddy Windows — Screen-Aware AI Assistant

An AI assistant that sees your screen in real time and answers 
questions about what you're doing — no copy-paste needed.

## 🎯 What it does

- 👁️ Captures your screen automatically on every question
- 🤖 Sends it to Gemini Vision AI for real-time analysis  
- 💬 Answers based on exactly what it sees
- 📄 Summarizes PDFs open in your browser
- 🗂️ Identifies open tabs, windows and apps
- 💻 Debugs your code by seeing terminal + editor at once

## 🧠 Real examples from testing

> "What tabs do I have open in Chrome?"
> → "Samsung Estudiantes, SUNAT SOL, Mi cuenta"

> "Summarize the PDF I have open"  
> → Summarized La Vida es Sueño (187 pages) in seconds

> "What am I doing right now?"
> → Described VS Code + terminal + conversation context

> "Help me fix this error"
> → Saw the traceback in terminal and suggested the fix

## 🛠️ Built With

- Python 3.14
- Google Gemini Vision API (gemini-3.6-flash)
- pyautogui — screen capture
- Pillow — image compression (70% size reduction)
- google-genai

## ⚙️ Setup

1. Clone this repo
2. Install dependencies:
\```
pip install pyautogui pillow google-genai
\```
3. Get a free API key at aistudio.google.com
4. Replace in code:
\```python
client = genai.Client(api_key="YOUR_KEY_HERE")
\```
5. Run:
\```
python ai_buddy.py
\```

## 🔮 Roadmap

- [ ] Voice input (speechrecognition)
- [ ] Voice output (pyttsx3)
- [ ] Hotkey activation (press key to ask)
- [ ] Floating window UI (tkinter)

## 💡 Inspired by

Clicky by @farzaa — reimagined for Windows with free APIs

## 👩‍💻 Author

angie casablanca — Industrial Engineer & AI Developer
Lima, Peru 🇵🇪
github.com/an-casdev
