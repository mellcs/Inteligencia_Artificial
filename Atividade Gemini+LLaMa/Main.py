import requests
import google.generativeai as genai

question = "Why is the sky blue?"

human_response = "I'm not exactly sure, but I assume it has something to do with the atmosphere and the sun rays, but I could be mistaken."

OLLAMA_MODEL = "llama3"

genai.configure(api_key=('AIzaSyCnYMaEDMMHlxxEMFwemA7KhpGAXHY_tVM'))
gemini_model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(prompt):
    try:
        response = gemini_model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[Erro ao gerar resposta com Gemini: {e}]"

def get_llama_response(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}
        )
        data = response.json()
        return data.get("response", "").strip()
    except Exception as e:
        return f"[Erro ao gerar resposta com LLaMA: {e}]"


response_llama = get_llama_response(question)
response_gemini = get_gemini_response(question)

answers = [
    {"id": "A", "source": "LLaMA", "text": response_llama},
    {"id": "B", "source": "Gemini", "text": response_gemini},
    {"id": "C", "source": "Human", "text": human_response}
]

detection_prompt = (
    "Below are three answers to the question: 'Why is the sky blue?'\n\n"
)
for answer in answers:
    detection_prompt += f"Answer {answer['id']}: {answer['text']}\n\n"

detection_prompt += (
    "Taking in account the style, vocabulary, coherence and subtleties, day wich one of the answers was probably written by a human."
    "Explain why you arrived at each conclusion. At the end, just say: 'The human answer is [letra]'."
    "Humans tend to have simpler answers, without much technicall knowledge."
)

llama_analysis = get_llama_response(detection_prompt)


print("\n<<<QUESTIONS>>")
print(question)

print("\n<<<ANSWERS>>>")
for answer in answers:
    print(f"Answer {answer['id']} ({answer['source']}):\n{answer['text']}\n")

print("<<<LLaMa's ANALYSIS>>>")
print(llama_analysis)
