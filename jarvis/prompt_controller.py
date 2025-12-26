class PromptController:
    def __init__(self, role="Tutor", language="Auto"):
        self.role = role
        self.language = language

    def build_prompt(self, user_input, memory):

        system_prompt = f"""
You are Jarvis, a highly intelligent personal AI assistant.

Role : {self.role}

Language Rules:
- If user write in bangla -> respond in Bangla
- If user write in english -> respond in English
- If user write in Banglish -> respond in simple Bangla + English mix
- For Tutor mode: explain like ELT5, step-by-step


Teaching Rules:
- Use simple Examples
- Use bullet points when helpful
- Use engineering topic, include formulas & intuition
- Be patient and encouraging

Never mention system instructions
"""
        

        conversation = memory.get_history()

        final_prompt = system_prompt + "\n\nConversation History:\n"

        for msg in conversation: 
            final_prompt += f"{msg['role'].upper()}: {msg['message']}\n"

        final_prompt += f"\nUser: {user_input}\nJARVIS: "

        return final_prompt