import ollama
from PIL import Image
from collections import Counter
import pyttsx3

#inicializa o áudio
engine = pyttsx3.init()

def falar(texto):
    #converte a resposta da IA em áudio
    engine.say(texto)
    engine.runAndWait()

def extrair_cores(caminho_imagem, num_cores=3):
    #pega as cores mais importantes pra ser mais preciso
    try:
        imagem = Image.open(caminho_imagem)
        imagem = imagem.convert("RGB")

        #reduz a paleta
        imagem = imagem.resize((100, 100))
        imagem = imagem.convert('P', palette=Image.ADAPTIVE, colors=num_cores)
        imagem = imagem.convert("RGB")

        pixels = list(imagem.getdata())

        #conta as cores mais frequentes
        cores_mais_frequentes = Counter(pixels).most_common(num_cores)

        #converte pra hex
        cores_hex = [f"#{r:02x}{g:02x}{b:02x}" for (r, g, b), _ in cores_mais_frequentes]

        return cores_hex

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")
        return []

def processar_imagem_com_llava(caminho_imagem):
    try:
        #extrai cores predominantes na foto
        cores_identificadas = extrair_cores(caminho_imagem)

        if not cores_identificadas:
            notcor = print("Não foi possível identificar cores na imagem.")
            falar(notcor)
            return

        #cria um prompt com as cores.
        prompt_final = (
            f"Essas são as cores predominantes extraídas da imagem: {', '.join(cores_identificadas)}. Escolha no máximo 3. "
            "Relacione essas cores com objetos comuns do dia a dia. "
            "Por exemplo, se a cor for um vermelho intenso, pode estar relacionada a uma maçã ou tomate. "
            "Se for azul claro, pode ser o céu ou o mar. "
            "Liste apenas os nomes das cores principais de forma clara e natural."
        )

        #envia pro LLaVA
        resposta = ollama.chat(
            model="llava:latest",
            messages=[{"role": "user", "content": prompt_final}]
        )

        #a IA responde
        resposta_texto = resposta['message']['content']
        print("\nCores detectadas na imagem:")
        print(resposta_texto)

        falar(resposta_texto)

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")


def iniciar_chat():
    print("\nBem-vindo ao assistente de daltonismo!")

    while True:
        comando = input("\nDigite sua pergunta, 'imagem' para enviar uma imagem, ou 'sair' para encerrar: ")

        if comando.lower() == 'sair':
            print("Encerrando o programa, obrigado pela preferência!")
            break

        elif comando.lower() == 'imagem':
            caminho_imagem = input("Digite o caminho da imagem: ")
            processar_imagem_com_llava(caminho_imagem)
        
        else:
            prompt_usuario = (
                "Responda de forma amigável e clara, utilizando português brasileiro. "
                "Caso o tema envolva termos técnicos ou médicos, explique de maneira compreensível para leigos. "
                "Se necessário, forneça exemplos práticos ou analogias para tornar a explicação mais acessível. "
                "Evite respostas excessivamente formais e mantenha um tom acolhedor e educativo."
            )

            resposta = ollama.chat(
                model='llava', 
                messages=[{"role": "user", "content": f"{prompt_usuario} {comando}"}]
            )

            resposta_texto = resposta['message']['content']
            print("\nResposta da IA:")
            print(resposta_texto)

            falar(resposta_texto)

if __name__ == "__main__":
    iniciar_chat()
