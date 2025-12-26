import google.genai as genai
#import google.generativeai as genai

class GeminiEngine:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)
        self.model_name = "gemini-2.5-flash"

    def generate_stream(self, prompt: str):
        try:
            response = self.client.models.generate_content_stream(model=self.model_name,
                                                                  contents=prompt)
            for chunk in response:
                if chunk.text:
                    yield chunk.text
        except Exception as e :
            yield f"‼️Gemini Error: {str(e)}"
                                      