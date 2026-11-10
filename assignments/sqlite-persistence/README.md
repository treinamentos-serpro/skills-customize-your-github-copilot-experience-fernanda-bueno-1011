# 📘 Assignment: SQLite and Data Persistence

## 🎯 Objective

Aprenda a armazenar dados em um banco SQLite e conectá-lo a uma aplicação FastAPI. Substitua o armazenamento temporário em memória por operações CRUD que continuam disponíveis depois que o servidor é reiniciado.

## 📝 Tasks

### 🛠️ Criar o Banco de Dados SQLite

#### Descrição
Implemente a inicialização do banco de dados da API de livros. Crie uma tabela `books` com um ID gerado automaticamente e as colunas necessárias para cada livro.

#### Requisitos
O programa concluído deve:

- Usar o módulo `sqlite3` incluído no Python e um arquivo de banco de dados chamado `books.db`
- Criar a tabela `books` com as colunas `id`, `title`, `author` e `year`
- Usar `CREATE TABLE IF NOT EXISTS` para permitir que a inicialização seja executada mais de uma vez
- Inicializar o banco de dados quando a aplicação iniciar


### 🛠️ Implementar as Operações do Banco de Dados

#### Descrição
Adicione funções de banco de dados para cadastrar um livro e listar os livros salvos. Use parâmetros SQL para passar às consultas os valores fornecidos pelo usuário.

#### Requisitos
O programa concluído deve:

- Implementar funções para inserir um livro e recuperar todos os livros
- Usar espaços reservados e parâmetros SQL em vez de inserir valores diretamente no texto das consultas
- Fechar as conexões com o banco de dados depois de cada operação
- Conectar os endpoints `POST /books` e `GET /books` ao banco de dados


### 🛠️ Persistir os Dados de Toda a API de Livros

#### Descrição
Conclua as operações restantes de livros e conecte-as à API. Verifique se os livros salvos continuam disponíveis depois de parar e reiniciar o servidor.

#### Requisitos
O programa concluído deve:

- Implementar funções para buscar, atualizar e excluir um livro pelo ID
- Conectar os endpoints `GET /books/{book_id}`, `PUT /books/{book_id}` e `DELETE /books/{book_id}` ao SQLite
- Retornar `404 Not Found` quando o livro solicitado não existir
- Verificar que, após cadastrar um livro e reiniciar o servidor, a listagem ainda retorna o livro salvo
- Executar a API com `uvicorn main:app --reload` e testar os endpoints em `/docs`