# 🤖 AI ChatBot - Streamlit + Gemini + LangChain

A modern, interactive AI chatbot built with Streamlit and Google Gemini AI using LangChain for advanced conversation management.

## ✨ Features
- Modern chat interface (Streamlit)
- Google Gemini AI integration
- Conversation memory (LangChain)
- Fast response (Streamlit caching)
- Error handling & clear chat
- Secure: API key in `.env`

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/sudeepkrishnan87/ai-chatbot.git
cd ai-chatbot
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_actual_api_key_here
```

### 5. Run the Application
```bash
cd prompt-mimic
streamlit run prompt_app.py
```

### 6. Access the App
Open your browser and go to:
```
http://localhost:8501
```

## 📝 Project Structure
```
ai-chatbot/
├── prompt-mimic/
│   └── prompt_app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## 🐛 Troubleshooting
- **Module not found?** Activate your virtual environment and reinstall requirements.
- **API key error?** Check your `.env` file and key value.
- **Port in use?** Run with `streamlit run prompt_app.py --server.port 8502`

## 📦 Dependencies
- streamlit
- google-generativeai
- langchain
- langchain-google-genai
- langchain-core
- langchain-community
- python-dotenv
- pydantic

## 🙏 Credits
- [Streamlit](https://streamlit.io/)
- [Google AI](https://ai.google.dev/)
- [LangChain](https://langchain.com/)

---

**Happy Chatting! 🚀**
