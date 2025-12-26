import streamlit as st
from config.setting import Settings
from jarvis.gemini_engine import GeminiEngine
from jarvis.prompt_controller import PromptController
from jarvis.memory import Memory
from jarvis.assistant import JarvisAssistant
from jarvis.speech_engine import SpeechEngine
import time
from jarvis.exporter import ChatExporter



st.set_page_config(page_title="Jarvis AI", layout="wide", page_icon="🤖")

st.title("🤖 Jarvis - Personal AI Assistant")

# Initialize Memory
memory = Memory()


#Sidebar
st.sidebar.header("⚙️ Controls")
role = st.sidebar.selectbox("Assistant Role", ["Tutor", "Coder", "Career Mentor"])

if st.sidebar.button("Clear Memory"):
    memory.clear()
    st.sidebar.success("Memory Cleared!")


st.sidebar.subheader("🎤 Voice Input")
use_voice = st.sidebar.checkbox("Enable Voice Input")

speech_engine = SpeechEngine(language="en-US")

st.sidebar.subheader("🌐 Language Preference")
language = st.sidebar.selectbox("Response Language", ["English", "Bangla", "Banglish"])


st.sidebar.subheader("📁 Export Chat")

if st.sidebar.button("Export Chat as PDF"):
    exporter = ChatExporter(memory)
    file_path = exporter.export_pdf()
    st.sidebar.success(f"Chat exported successfully!")

    with open(file_path, "rb") as f:
        st.sidebar.download_button(
            label="⬇️ Download PDF",
            data=f,
            file_name="jarvis_chat.pdf",
            mime="application/pdf"
        )
    
        

#Initialize System
settings = Settings()
engine = GeminiEngine(settings.load_api_key())  
prompt_controller = PromptController(role=role, language=language)
jarvis = JarvisAssistant(engine, prompt_controller, memory)

# Greet
if "greeted" not in st.session_state: 
    st.chat_message("assistant").write(jarvis.greet())
    st.session_state.greeted = True


# Display chat history
for msg in memory.get_history():
    st.chat_message(msg["role"]).write(msg["message"])

# User input
user_input = st.chat_input("Ask Jarvis anything...", key="jarvis_chat")

if user_input:
    st.chat_message("user").write(user_input)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_text = ""

        for chunk in jarvis.respond_stream(user_input):
                full_text += chunk
    response_placeholder.markdown(full_text)


if use_voice:
    if st.button("🎤 Speak"):
        with st.spinner("Listening..."):
            user_input = speech_engine.listen()
            st.chat_message("user").write(user_input)
            response = jarvis.respond(user_input)
            st.chat_message("assistant").write(response)
    else:
        user_input = st.chat_input("Ask Jarvis anything...")
        if user_input:
            st.chat_message("user").write(user_input)
            response = jarvis.respond(user_input)
            st.chat_message("assistant").write(response)


    
