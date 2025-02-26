import google.generativeai as genai

def meheng_brain(query):
    try:
        genai.configure(api_key="secret-API-key-removed-for-security")

        generation_config = {
            "temperature": 0,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 200,
            "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction="You are meheng, an ai voice assistant, designed to aid me with all my questions. You have been developed by Yasir Eqbal. Give me short and to-the-point answers to all my questions. Don't respond with any emojis.",
        )

        chat_session = model.start_chat(
            history=[
            ]
        )

        response = chat_session.send_message(query)

        return response.text

    except Exception as e:
        return "Sorry, Unable to answer this question currently."
