class JarvisAssistant:
    def __init__(self, engine, prompt_controller, memory):
        self.engine = engine
        self.prompt_controller = prompt_controller
        self.memory = memory

    def greet(self):
        return "Hello! I am Jarvis, your personal AI assistant. How can I assist you today?"

    def respond_stream(self, user_input):
        self.memory.add("user", user_input)
        prompt = self.prompt_controller.build_prompt(user_input=user_input, memory=self.memory)

        full_response = ""
        for chunk in self.engine.generate_stream(prompt):
            full_response += chunk
            yield chunk

        self.memory.add("assistant", full_response)
   