class PromptController:
    def __init__(self, role="Tutor"):
        self.role = role

    def build_prompt(self, user_input, memory):

        system_prompt = f"""
You are Jarvis, a highly intelligent personal AI assistant.

Role : {self.role}

Rules:
- Be polite, clear, and helpful
- Explain step-by-step when teaching
- Answer concisely but accuately
- If coding, give clean Python Examples
"""
        

        conversation = memory.get_history()

        final_prompt = system_prompt + "\n\nConversation History:\n"

        for msg in conversation: 
            final_prompt += f"{msg['role'].upper()}: {msg['message']}\n"

        final_prompt += f"\nUser: {user_input}\nJARVIS: "

        return final_prompt