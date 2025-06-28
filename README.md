[English Version](README.EN.md)

# AS05: Implementação de Assistente Conversacional Baseado em LLM

Trabalho da matéria Tópicos em Computação III do curso de Ciência da Computação da PUC Minas no qual deveria ser desenvolvido um Assistente Conversacional Baseado em LLM que seja capaz de indexar vetores (embeddings textuais) de uma coleção de documentos em PDF para responder posteriormente a perguntas feitas por meio de uma interface de conversação.

## Como executar

Para executar este programa, siga os seguintes passos:

### Use um ambiente virtual (opcional e recomendado)

#### Crie o ambiente virtual

No shell (Terminal, Prompt de Comando ou PowerShell) dentro da pasta do projeto, digite:

```
python3 -m venv venv
```

ou

```
python -m venv venv
```

#### Ative o ambiente virtual

Se o seu shell for o Bash do Linux ou Mac OS, dentro da pasta do projeto, digite:

```
source venv/bin/activate
```

Se o seu shell for o Prompt de Comando do Windows, dentro da pasta do projeto, digite:

```
venv\Scripts\activate.bat
```

Se o seu shell for o PowerShell do Windows, dentro da pasta do projeto, digite:

```
.\venv\Scripts\Activate.ps1
```

### Instale as dependências

No shell (Terminal, Prompt de Comando ou PowerShell) dentro da pasta do projeto, digite:

```
pip install -r requirements.txt
```

### Adicione as variáveis de ambiente

Renomeie o arquivo ```.env.sample``` para ```.env```.

Abra o arquivo ```.env``` em um editor de texto.

#### Obtenha a chave de API do Hugging Face:

1. Acesse: https://huggingface.co/settings/tokens

   Caso não esteja logado no Hugging Face, faça login. Caso não tenha conta, crie uma conta.

2. Clique no botão ```Create new token```.

3. Em ```Token name```, digite o nome de sua preferência para a chave de API.

4. Clique em ````Create token```.

5. No prompt que foi aberto, clique no botão ```Copy```.

6. No arquivo ```.env```, cole o token á direita de (na mesma linha) ```HUGGINGFACEHUB_API_KEY=```.

#### Obtenha a chave de API do Pinecone:

1. Acesse: https://app.pinecone.io

   Caso não esteja logado no Pinecone, faça login. Caso não tenha conta, crie uma conta.

2. No canto esquerdo, clique em ```Database``` e depois em ```Indexes```.

3. No canto esquerdo, clique em ```API Keys```.

4. Clique no botão ```Create API Key```.

5. No prompt que foi aberto, digite o nome de sua preferência para a chave de API.

6. Clique em ```Create key```.

7. Na barra de texto, clique no botão copiar.

8. No arquivo ```.env```, cole o token á direita de (na mesma linha) ```PINECONE_API_KEY=```.

#### Obtenha o nome do índice do Pinecone

1. Acesse: https://app.pinecone.io

2. No canto esquerdo, clique em ```Indexes```.

3. Caso não tenha nenhum índice, clique no botão ```Create index```. Digite o nome desejado para índice, e clique em ```Create index``` (no canto inferior direito).

4. No arquivo ```.env```, cloe o índice á direita de (na mesma linha) ```PINECONE_INDEX_NAME=```.

### Execute o programa

No shell (Terminal, Prompt de Comando ou PowerShell) dentro da pasta do projeto, digite:

```
python3 app
```

ou

```
python app
```

E uma janela do programa se abrirá.

## Aplicação em Funcionamento

### Vídeo

[Neste vídeo](https://youtu.be/sO1tvquSQWM) é possível ver a aplicação em funcionamento:

[![Demonstração do Assistente Conversacional - Tópicos em Computação III - Ciência da Computação](https://img.youtube.com/vi/sO1tvquSQWM/0.jpg)](https://youtu.be/sO1tvquSQWM)

### Captura de Tela

![Captura de tela do Assistente Conversacional, mostrando um exemplo de conversa](screenshots/Captura%20de%20tela%20de%202025-06-24%2018-28-51.png)