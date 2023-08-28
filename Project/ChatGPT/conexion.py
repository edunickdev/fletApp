import openai

openai.api_key = "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"

def sugerencias_chatGPT(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt= f"{prompt}, dame las sugerencias en máximo 100 tokens.",
            max_tokens=120,
            temperature=0.7,
        )
        return response.choices[0].text.strip()

    except Exception as e:
        return f"Error: {str(e)}"

# def main():
#     prompt = "Enumera en maximo 5 opciones la tarea a resolver, ajusta siemore la respuesta a máximo 100 tokens"
#     response = sugerencias_chatGPT(prompt)
#     print("Respuesta de ChatGPT:", response)

# main()
