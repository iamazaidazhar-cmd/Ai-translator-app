import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import io

# -------------------- Page Configuration --------------------

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

# -------------------- Session State --------------------

if "history" not in st.session_state:
    st.session_state.history = []

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

if "target_lang_code" not in st.session_state:
    st.session_state.target_lang_code = "en"

# -------------------- Sidebar (settings defined FIRST, before use) --------------------

st.sidebar.title("🌍 AI Translator")
st.sidebar.success("👋 Welcome!")
st.sidebar.markdown("---")

# Settings
st.sidebar.subheader("⚙️ Settings")

save_history = st.sidebar.checkbox("📜 Save Translation History", value=True)
auto_detect = st.sidebar.checkbox("🌐 Auto Detect Source Language", value=False)
voice_enabled = st.sidebar.checkbox("🔊 Enable Voice Output", value=False)
dark_mode = st.sidebar.checkbox("🌙 Dark Mode", value=False)

st.sidebar.markdown("---")

# Translation History
st.sidebar.subheader("📖 Recent History")

if st.session_state.history:
    for item in reversed(st.session_state.history[-5:]):
        st.sidebar.markdown(
            f"**{item['From']} ➜ {item['To']}**\n\n"
            f"📝 {item['Input'][:25]}...\n\n---"
        )
else:
    st.sidebar.info("No translations yet.")

st.sidebar.markdown("---")

# Quick Actions
st.sidebar.subheader("⚡ Quick Actions")

if st.sidebar.button("🗑 Clear History"):
    st.session_state.history.clear()
    st.rerun()

if st.sidebar.button("🔄 Refresh App"):
    st.rerun()

st.sidebar.markdown("---")

# About
st.sidebar.subheader("ℹ️ About")
st.sidebar.write("Version : 1.0")
st.sidebar.write("Status : 🟢 Online")

# -------------------- Theme CSS (inline, no missing files) --------------------

dark_css = """
<style>
.stApp{ background:#3A3D42; }
h1,h2,h3,h4,h5,h6,p,label,span,div{ color:#F3F4F6; }
[data-testid="stSidebar"]{ background:#1E2229; }
[data-testid="stSidebar"] *{ color:#F3F4F6; }
.stButton>button{
    width:100%; height:50px; border-radius:10px;
    background:#4F46E5; color:#F3F4F6; font-size:18px; font-weight:bold;
    border:1px solid #4F46E5;
}
.stButton>button:hover{ background:#3730A3; color:#F3F4F6; border:1px solid #3730A3; }
textarea{ border-radius:10px !important; background:#2A2D33 !important; color:#F3F4F6 !important; }
input, .stSelectbox div[data-baseweb="select"]{ background:#2A2D33 !important; color:#F3F4F6 !important; }
</style>
"""

light_css = """
<style>
.stApp{ background:#FFFFFF; }
h1,h2,h3,h4,h5,h6,p,label,span,div{ color:#1F2937; }
[data-testid="stSidebar"]{ background:#1E2229; }
[data-testid="stSidebar"] *{ color:#F3F4F6; }
.stButton>button{
    width:100%; height:50px; border-radius:10px;
    background:#4F46E5; color:#F3F4F6; font-size:18px; font-weight:bold;
    border:1px solid #4F46E5;
}
.stButton>button:hover{ background:#3730A3; color:#F3F4F6; border:1px solid #3730A3; }
textarea{ border-radius:10px !important; background:#F3F4F6 !important; color:#1F2937 !important; }
input, .stSelectbox div[data-baseweb="select"]{ background:#F3F4F6 !important; color:#1F2937 !important; }
</style>
"""

st.markdown(dark_css if dark_mode else light_css, unsafe_allow_html=True)

# -------------------- Title --------------------

st.title("🌍 AI Language Translator")
st.write("Translate text instantly into multiple languages.")

# -------------------- Languages --------------------

languages = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Arabic": "ar",
    "Hindi": "hi",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Italian": "it",
    "Russian": "ru"
}

# Statistics
st.sidebar.subheader("📊 Statistics")
st.sidebar.metric("🌐 Languages", len(languages))
st.sidebar.metric("📜 History", len(st.session_state.history))
st.sidebar.markdown("---")

# -------------------- Input --------------------

text = st.text_area(
    "✍ Enter Text",
    height=180,
    placeholder="Type your text here..."
)

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "Source Language",
        list(languages.keys()),
        disabled=auto_detect
    )

with col2:
    target = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

# -------------------- Translate --------------------

if st.button("🌍 Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            source_lang = "auto" if auto_detect else languages[source]
            target_lang = languages[target]

            translated = GoogleTranslator(
                source=source_lang,
                target=target_lang
            ).translate(text)

            # Store in session_state so it survives reruns from other buttons
            st.session_state.translated_text = translated
            st.session_state.target_lang_code = target_lang

            if save_history:
                st.session_state.history.append({
                    "Input": text,
                    "Output": translated,
                    "From": "Auto" if auto_detect else source,
                    "To": target
                })

        except Exception as e:
            st.error(f"Translation Failed: {e}")

# -------------------- Show Result (persists across reruns) --------------------

if st.session_state.translated_text:

    st.success("✅ Translation Completed")

    st.text_area(
        "Translated Text",
        st.session_state.translated_text,
        height=180
    )

    # Built-in copy icon — no clipboard access needed, works on servers too
    st.code(st.session_state.translated_text, language=None)

    st.download_button(
        label="📥 Download Translation",
        data=st.session_state.translated_text,
        file_name="translation.txt",
        mime="text/plain"
    )

    if voice_enabled:
        try:
            tts = gTTS(
                text=st.session_state.translated_text,
                lang=st.session_state.target_lang_code.split("-")[0]
            )
            audio_buffer = io.BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)
            st.audio(audio_buffer.read(), format="audio/mp3")
        except Exception as e:
            st.error(f"Voice generation failed: {e}")

# -------------------- Clear --------------------

if st.button("🗑 Clear"):
    st.session_state.translated_text = ""
    st.rerun()

# -------------------- Footer --------------------

st.markdown("---")

col1, col2, col3 = st.columns(3)
col1.metric("Languages", len(languages))
col2.metric("Translator", "Google")
col3.metric("Status", "Online")

st.markdown("---")
st.caption("Developed by Muhammad Zaid Azhar")
