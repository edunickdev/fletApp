import openai

from Project.ChatGPT.lector_credenciales import cargar_credenciales
# from lector_credenciales import cargar_credenciales

credentials = cargar_credenciales()

openai.api_key = credentials['api_key']

def sugerencias_chatGPT(prompt):
    try:
        response = openai.chat.completions.create (
            max_tokens=150,
            temperature=0.7,
            model="gpt-3.5-turbo",
            messages=[
                {
                    'content': prompt,
                    'role': 'user'
                }
            ]
        )
        answer = response.choices[0].message.content
        return answer
    
    except Exception as e:
        return f"Error: {str(e)}"

# def main():
#     prompt = "Enumera en maximo 5 opciones la tarea a resolver, ajusta siemore la respuesta a máximo 100 tokens"
#     response = sugerencias_chatGPT(prompt)
#     print("Respuesta de ChatGPT:", response)

# main()
