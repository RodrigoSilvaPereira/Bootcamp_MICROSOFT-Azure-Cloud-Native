# ☁️ Desafio: Armazenando Dados de um E-Commerce na Cloud

Este desafio tem como objetivo construir uma **estrutura de armazenamento em nuvem utilizando o Microsoft Azure** para simular o backend de um **sistema de e-commerce**.

A solução utiliza:

- **Azure SQL Database** para armazenar os dados dos produtos
- **Azure Blob Storage** para armazenar imagens dos produtos
- **Python + Streamlit** para interface da aplicação
- **Variáveis de ambiente (.env)** para gerenciamento seguro das credenciais

Todos os códigos utilizados neste desafio estão disponíveis na pasta:

```
/Codigos
```

---

# 🧠 Arquitetura da Solução

A arquitetura da aplicação segue o seguinte fluxo:

```
Usuário
   ↓
Aplicação Python (Streamlit)
   ↓
Upload de imagem → Azure Blob Storage
   ↓
Registro do produto → Azure SQL Database
   ↓
Listagem de produtos com imagem armazenada no Blob
```

Essa arquitetura separa **armazenamento estruturado e não estruturado**, seguindo boas práticas de aplicações cloud.

---

# 🚀 Etapas de Configuração no Azure

## 1️⃣ Criar um Resource Group

Criar um **Resource Group** para agrupar todos os recursos do laboratório.

```
LAB001
```

Esse grupo será responsável por organizar:

- Banco de dados
- Storage account
- Configurações de rede

---

# 🗄 Criando o Banco de Dados no Azure

## 2️⃣ Criar um Azure SQL Database

Criar um banco SQL dentro do Resource Group.

Tipo de banco:

```
Single Database Development
```

Nome do banco:

```
sqllab001dbdeveastus
```

---

## 3️⃣ Criar o SQL Database Server

Criar um servidor para hospedar o banco de dados.

Nome do servidor:

```
rodbsrvdeveastuslab001
```

Durante a criação será necessário definir:

- usuário administrador
- senha segura

⚠️ Importante: nunca utilizar senhas simples ou previsíveis.

---

# 💾 Criando o Storage Account

Criar um **Storage Account** para armazenar arquivos de imagens dos produtos.

Nome do Storage Account:

```
rostadevlab001eastus001
```

Tipo de armazenamento:

```
Azure Blob Storage - Standard
```

Redundância utilizada:

```
LRS (Local Redundant Storage)
```

---

# 📦 Configurando o Blob Storage

Após criar o Storage Account:

1. Acessar **Data Storage**
2. Selecionar **Containers**
3. Criar um container chamado:

```
Fotos
```

Configuração de acesso:

```
Blob (acesso público para blobs)
```

Também é necessário **habilitar acesso anônimo ao Blob**.

---

# 🔑 Obtendo a Connection String

Para acessar o Blob Storage pela aplicação:

1. Ir em:

```
Security + Networking → Access Keys
```

2. Copiar a **Connection String**

Ela será utilizada no arquivo `.env`.

---

# 🔐 Configurando Variáveis de Ambiente

Criar um arquivo `.env` com as seguintes variáveis:

```
BLOB_CONNECTION_STRING=
BLOB_CONTAINER_NAME=
BLOB_ACCOUNT_NAME=

SQL_SERVER=
SQL_DATABASE=
SQL_USER=
SQL_PASSWORD=
```

Essas variáveis serão utilizadas pela aplicação Python para conexão com os serviços do Azure.

---

# 🌐 Configurando Firewall do SQL Server

Para permitir conexão externa:

1. Acessar o **SQL Server**
2. Ir em:

```
Networking → Firewall rules
```

3. Habilitar acesso
4. Criar regra de acesso com o **IP do cliente**

---

# 🧪 Testando Conexão com SQL Server

Testar conexão utilizando:

```
SQL Server Management Studio (SSMS)
```

Caso a conexão funcione corretamente, o banco estará pronto para uso.

---

# 🗃 Criando a Tabela no Banco

Executar o script SQL disponível no arquivo:

```
/Codigos/infox.txt
```

Esse script cria a tabela utilizada para armazenar os produtos do e-commerce.

---

# 🧩 Estrutura da Aplicação Python

A aplicação foi desenvolvida utilizando **Streamlit** para criar uma interface simples de cadastro de produtos.

Funcionalidades principais:

- cadastro de produto
- upload de imagem
- armazenamento da imagem no Blob Storage
- registro do produto no banco SQL
- listagem de produtos cadastrados

Arquivo principal da aplicação:

```
/Codigos/main.py
```

---

# 📤 Upload de Imagens no Blob Storage

A aplicação envia a imagem do produto para o **Azure Blob Storage**.

Fluxo:

1. gerar um identificador único com `uuid`
2. salvar o arquivo no container
3. gerar a URL pública da imagem
4. armazenar a URL no banco de dados

Isso permite que as imagens sejam carregadas diretamente da nuvem.

---

# 🗄 Inserção de Produtos no Banco

Após o upload da imagem, a aplicação insere os dados no **Azure SQL Database**.

Campos armazenados:

- nome
- preço
- descrição
- URL da imagem no Blob Storage

---

# 📋 Listagem de Produtos

A aplicação também possui uma funcionalidade para listar os produtos cadastrados.

Para cada produto são exibidos:

- nome
- preço
- descrição
- imagem armazenada no Blob Storage

---

# ▶️ Executando a Aplicação

Para executar a aplicação localmente:

1️⃣ Instalar dependências

```
pip install streamlit azure-storage-blob pymssql python-dotenv
```

2️⃣ Executar o projeto

```
streamlit run main.py
```

3️⃣ Acessar no navegador

```
http://localhost:8501
```

---

# 📦 Estrutura do Projeto

```
Codigos/
│
├── main.py
├── infox.txt
└── .env
```

---

# ✅ Resultado Final

Ao final do desafio foi construída uma solução completa de armazenamento para um sistema de e-commerce utilizando serviços do Azure.

A aplicação permite:

- cadastrar produtos
- enviar imagens para o Blob Storage
- armazenar dados estruturados no Azure SQL
- listar produtos cadastrados

Esse tipo de arquitetura é comum em aplicações modernas que utilizam **cloud para armazenamento escalável e alta disponibilidade**.

---

# 📚 Conclusão

Este desafio demonstrou como integrar diferentes serviços da plataforma Azure para construir uma solução prática de armazenamento em nuvem.

Foram utilizados conceitos importantes como:

- **Azure SQL Database**
- **Azure Blob Storage**
- **Gerenciamento de variáveis de ambiente**
- **Integração entre aplicação Python e serviços cloud**

Esses conceitos são fundamentais para desenvolvimento de aplicações **cloud-native na plataforma Azure**.