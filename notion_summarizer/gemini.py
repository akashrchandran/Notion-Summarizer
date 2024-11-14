import google.generativeai as genai
from google.generativeai import GenerationConfig
import json


generation_config = GenerationConfig(
    temperature=1,
    top_p=0.95,
    top_k=40,
    max_output_tokens=8192
)

class GeminiClient:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
        )

    def generate_content(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text
