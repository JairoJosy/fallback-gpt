from mycroft import MycroftSkill, intent_file_handler
import openai
openai.api_key = "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"

class ChatGptSkill(MycroftSkill):
    
    @intent_file_handler('ask.chatgpt.intent')
    def handle_ask_chatgpt_intent(self, message):
        prompt = message.data.get('prompt')
        response = self.generate_response(prompt)
        self.speak(response)

    def generate_response(self, prompt):
        model_engine = "davinci" # or another GPT-3 model
        prompt = (f"{prompt}\n"
                  "Response:")
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        message = response.choices[0].text.strip()
        return message
