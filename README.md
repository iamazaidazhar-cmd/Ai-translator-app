# 🌍 AI Language Translator

A simple, elegant web app built with **Streamlit** that translates text instantly into multiple languages, with optional text-to-speech output and translation history tracking.

## ✨ Features

- 🌐 Translate text between 12 languages (English, Urdu, French, German, Spanish, Arabic, Hindi, Chinese, Japanese, Korean, Italian, Russian)
- 🔍 Auto-detect source language
- 🔊 Text-to-speech voice output for translated text
- 📖 Translation history (last 5 shown in sidebar)
- 📥 Download translated text as a `.txt` file
- 📋 One-click copy of translated text
- 🌙 Light / Dark mode toggle
- 📊 Sidebar statistics (languages supported, history count)

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) — Web app framework
- [Deep Translator](https://pypi.org/project/deep-translator/) — Google Translate wrapper
- [gTTS](https://pypi.org/project/gTTS/) — Google Text-to-Speech

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   cd YOUR-REPO-NAME
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

4. Open your browser at `http://localhost:8501`

## 🚀 Usage

1. Type or paste the text you want to translate in the input box.
2. Select the **Source Language** (or enable Auto Detect).
3. Select the **Target Language**.
4. Click **🌍 Translate**.
5. View the translated text, copy it, download it, or listen to it (if voice output is enabled).

## 📋 Requirements

- Python 3.8+
- Internet connection (required for Google Translate and Text-to-Speech services)

## 👨‍💻 Developer

Developed by **Muhammad Zaid Azhar**

## 📄 License

This project is open source and available for personal and educational use.
