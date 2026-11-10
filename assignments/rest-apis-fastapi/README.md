# 📘 Tarefa: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com o framework FastAPI, do primeiro endpoint até um CRUD completo com validação de dados e tratamento de erros.

> 💡 **Preparação:** instale as dependências com `pip install fastapi uvicorn` e execute a API com `uvicorn main:app --reload`. Depois acesse `http://127.0.0.1:8000/docs` para testar seus endpoints pela documentação interativa gerada automaticamente.

## 📝 Tarefas

### 🛠️ Criar o Primeiro Endpoint

#### Descrição
Crie uma aplicação FastAPI com uma rota `GET` que retorna uma mensagem de boas-vindas e uma rota com parâmetro de caminho que retorna uma saudação personalizada.

#### Requisitos
O programa completo deve:

- Criar uma instância de `FastAPI` chamada `app`
- Definir a rota `GET /` retornando um dicionário com a chave `"message"`
- Definir a rota `GET /greet/{name}` retornando um dicionário com a chave `"greeting"` contendo a saudação com o nome informado
- Testar as duas rotas pelo navegador ou pela documentação em `/docs`


### 🛠️ Receber Dados com Modelos Pydantic

#### Descrição
Crie um endpoint `POST` que recebe os dados de um livro no corpo da requisição. Use um modelo Pydantic para validar os dados automaticamente e retornar a resposta com o status correto.

#### Requisitos
O programa completo deve:

- Criar uma classe `Book` herdando de `BaseModel` com os campos `title` (texto), `author` (texto), `year` (inteiro) e `pages` (inteiro, opcional, padrão `None`)
- Definir a rota `POST /books` que recebe um `Book` no corpo da requisição
- Retornar status `201 Created` ao cadastrar um livro com sucesso
- Verificar que o FastAPI rejeita, com status `422`, uma requisição com `year` em formato inválido (por exemplo, `"abc"`)


### 🛠️ Implementar um CRUD Completo

#### Descrição
Expanda a API para gerenciar uma coleção de livros em memória (um dicionário). Implemente as operações de listar, buscar, atualizar e remover, tratando corretamente os casos em que o livro não existe.

#### Requisitos
O programa completo deve:

- Armazenar os livros em um dicionário `books_db`, usando um `id` inteiro como chave e gerando novos ids automaticamente
- Definir `GET /books` para listar todos os livros
- Definir `GET /books/{book_id}` para retornar um livro específico
- Definir `PUT /books/{book_id}` para substituir os dados de um livro existente
- Definir `DELETE /books/{book_id}` para remover um livro, retornando status `204 No Content`
- Retornar erro `404 Not Found` com uma mensagem clara quando o `book_id` não existir, usando `HTTPException`
