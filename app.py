import streamlit as st
from config.setting import Settings
from jarvis.gemini_engine import GeminiEngine
from jarvis.prompt_controller import PromptController
from jarvis.memory import Memory
from jarvis.assistant import JarvisAssistant

st.set_page_config(page_title="Jarvis AI", layout="wide", page_icon="🤖")

st.title("🤖 Jarvis - Personal AI Assistant")


#Sidebar
st.sidebar.header("⚙️ Controls")
role = st.sidebar.selectbox("Assistant Role", ["Tutor", "Coder", "Career Mentor"])

if st.sidebar.button("Clear Memory"):
    Memory().clear()
    st.sidebar.success("Memory Cleared!")


#Initialize System
settings = Settings()
engine = GeminiEngine(settings.load_api_key())  
memory = Memory()
prompt_controller = PromptController(role=role)
jarvis = JarvisAssistant(engine, prompt_controller, memory)

# Greet
if "greeted" not in st.session_state: 
    st.chat_message("assistant").write(jarvis.greet())
    st.session_state.greeted = True


# Display chat history
for msg in memory.get_history():
    st.chat_message(msg["role"]).write(msg["message"])

# User input
user_input = st.chat_input("Ask Jarvis anything...")

if user_input:
    st.chat_message("user").write(user_input)
    response = jarvis.respond(user_input)
    st.chat_message("assistant").write(response)


    
