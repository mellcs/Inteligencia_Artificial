</head>
<body>

<header>
  <h1>Trabalho de IA1</h1>
  <p>Meu projeto se chama DaltoHelp, e ele é um assistente para pessoas com daltonismo.</p>
</header>

<main>

  <h2>🪼 Funcionalidades</h2>
  <ul>
    <li>🫧 <strong>Texto</strong>: Permite a entrada de texto com o modelo de linguagem (LLaVA).</li>
    <li>🫧 <strong>Imagem</strong>: Extrai e analisa as cores dominantes e uma foto via IA.</li>
    <li>🫧 <strong>Áudio</strong>: Converte a resposta da IA em áudio para que o usuário possa ouvir.</li>
    <li>🫧 <strong>Prompt engineering</strong>: Injeção de instruções aos prompts para obter respostas mais úteis, relevantes e precisas.</li>
  </ul>

  <h2>🪼 Tecnologias utilizadas</h2>
  <ul>
    <li><span class="tag">Python 3.10+</span></li>
    <li><a href="https://ollama.com/" target="_blank">Ollama</a> com modelo <strong>LLaVA</strong></li>
    <li>Bibliotecas Python:
      <ul>
        <li><code>ollama</code> – integração com modelos de linguagem locais</li>
        <li><code>pyttsx3</code> – conversão de texto em áudio</li>
        <li><code>pillow</code> – processamento de imagens</li>
        <li><code>collections</code> – para contagem das cores</li>
      </ul>
    </li>
  </ul>

  <h2>🪼 Como executar o projeto</h2>

  <h3>1. Clone o repositório</h3>
  <pre><code>git clone https://github.com/mellcs/Inteligencia_Artificial.git
cd Inteligencia_Artificial/Trabalho\ de\ IA</code></pre>

  <h3>2. Instale as dependências</h3>
  <pre><code>pip install ollama pyttsx3 pillow</code></pre>
  <p><strong>Obs:</strong> O módulo <code>collections</code> já faz parte da biblioteca padrão do Python.</p>

  <h3>3. Instale e configure o Ollama</h3>
  <ul>
    <li>Baixe o Ollama: <a href="https://ollama.com/download" target="_blank">https://ollama.com/download</a></li>
    <li>Instale o modelo <code>llava</code>:</li>
  </ul>
  <pre><code>ollama run llava</code></pre>

  <h3>4. Execute a aplicação</h3>
  <pre><code>python multimodal_ia.py</code></pre>

  <h2>🪼 Exemplos de uso</h2>

  <h3>🫧 Entrada de texto</h3>
  <p><strong>Digite uma pergunta:</strong> <em>"Explique o que é daltonismo."</em></p>
  <p>🫧 Áudio de resposta: <em>“Claro! O daltonismo é uma doença...”</em></p>

  <h3>🫧 Entrada de imagem</h3>
  <p><strong>Digite o caminho da imagem:</strong> <code>imagens/exemplo.png</code></p>
  <p>🫧 Cores detectadas: <code>#e63946</code>, <code>#f1faee</code>, <code>#a8dadc</code>, <code>#457b9d</code>, <code>#1d3557</code></p>
  <p>🫧 Resposta do modelo: “As cores predominantes são o azul do céu, um preto que lembra a noite...”</p>
  <p>🫧 A resposta também é lida em voz alta.</p>

  <h2>🪼 Modelos e fontes</h2>
  <ul>
    <li><strong>Modelo utilizado:</strong> <a href="https://ollama.com/library/llava" target="_blank">llava</a> (LLaMA Visual Language Assistant)</li>
    <li><strong>Baseado em modelo local via:</strong> <a href="https://ollama.com/" target="_blank">Ollama</a></li>
    <li><strong>Análise de imagem:</strong> Pillow</li>
    <li><strong>Áudio:</strong> pyttsx3 (offline)</li>
  </ul>

  <h2>🪼 Desenvolvido por</h2>
  <p>Mell Santos de Campos </p>

</main>

<footer>
  <p>&copy; 2025 | DaltoHelp</p>
</footer>

</body>
</html>
