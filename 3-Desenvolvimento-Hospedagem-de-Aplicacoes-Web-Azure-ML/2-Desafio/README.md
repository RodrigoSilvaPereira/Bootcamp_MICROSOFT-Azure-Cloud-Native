# 🚀 Desafio: Deploy de Aplicação Web com Azure Container Registry e Container Apps

Este desafio tem como objetivo realizar o **deploy de uma aplicação web simples (HTML + CSS)** utilizando serviços da plataforma Microsoft Azure.

A aplicação será:

- containerizada com Docker
- armazenada no Azure Container Registry (ACR)
- executada no Azure Container Apps

---

# 🎯 Objetivo

Construir uma aplicação cloud-native simples utilizando:

- Docker
- Azure Container Registry (ACR)
- Azure Container Apps

---

# 🧱 Arquitetura da Solução

```
Aplicação HTML/CSS
        │
Docker Build
        │
Azure Container Registry (ACR)
        │
Azure Container Apps
        │
Internet (URL pública)
```

---

# 📁 Estrutura do Projeto

```
/Codigos/
 ├── index.html
 └── Dockerfile
```

---

# 🖥 1️⃣ Criar a Aplicação Web

Crie um arquivo:

```html
index.html
```

Exemplo:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Minha Aplicação Azure</title>
</head>
<body>
    <h1>🚀 Deploy com Azure Container Apps</h1>
    <p>Aplicação rodando na nuvem!</p>
</body>
</html>
```

---

# 🐳 2️⃣ Criar o Dockerfile

Crie um arquivo chamado:

```
Dockerfile
```

Conteúdo:

```
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html
```

---

# ⚙️ 3️⃣ Build da Imagem Docker

```bash
docker build -t minhaapp:latest .
```

---

# ▶️ 4️⃣ Testar Localmente

```bash
docker run -d -p 8080:80 minhaapp:latest
```

Acesse:

```
http://localhost:8080
```

---

# ☁️ 5️⃣ Login no Azure

```bash
az login
```

---

# 📦 6️⃣ Criar Resource Group

```bash
az group create --name rg-containerapp-lab --location eastus
```

---

# 🐳 7️⃣ Criar Azure Container Registry (ACR)

```bash
az acr create \
--name meuacrcontainerapp \
--resource-group rg-containerapp-lab \
--sku Basic
```

---

# 🔐 8️⃣ Login no ACR

```bash
az acr login --name meuacrcontainerapp
```

---

# 🏷 9️⃣ Tag da Imagem para o ACR

```bash
docker tag minhaapp:latest meuacrcontainerapp.azurecr.io/minhaapp:latest
```

---

# 🚀 🔟 Enviar Imagem para o ACR

```bash
docker push meuacrcontainerapp.azurecr.io/minhaapp:latest
```

---

# 🧩 1️⃣1️⃣ Criar Ambiente do Container Apps

```bash
az containerapp env create \
--name env-containerapp \
--resource-group rg-containerapp-lab \
--location eastus
```

---

# 🚀 1️⃣2️⃣ Criar Container App

```bash
az containerapp create \
--name minha-container-app \
--resource-group rg-containerapp-lab \
--environment env-containerapp \
--image meuacrcontainerapp.azurecr.io/minhaapp:latest \
--target-port 80 \
--ingress external \
--registry-server meuacrcontainerapp.azurecr.io \
--query properties.configuration.ingress.fqdn
```

---

# 🔎 Explicação dos Parâmetros

- `--image` → imagem hospedada no ACR  
- `--environment` → ambiente do Container Apps  
- `--target-port` → porta exposta pelo container  
- `--ingress external` → acesso público  
- `--registry-server` → registry utilizado  

---

# 🌍 1️⃣3️⃣ Acessar a Aplicação

Após o deploy, o Azure retornará uma URL:

```
https://xxxx.azurecontainerapps.io
```

Abra no navegador e veja sua aplicação rodando na nuvem 🚀

---

# 🔐 1️⃣4️⃣ (Opcional) Configurar Credenciais do ACR

Caso necessário:

```bash
az acr update -n meuacrcontainerapp --admin-enabled true
```

---

# 📊 Fluxo Completo

```
HTML/CSS
   ↓
Dockerfile
   ↓
Docker Build
   ↓
ACR (push)
   ↓
Container Apps (deploy)
   ↓
Aplicação Online
```

---

# ⚠️ Boas Práticas

- Use nomes únicos para o ACR (globalmente únicos)
- Nunca exponha credenciais no código
- Utilize `.env` para configurações sensíveis
- Sempre delete recursos após o uso para evitar custos

---

# 🧹 Limpeza de Recursos

Após finalizar o laboratório:

```bash
az group delete --name rg-containerapp-lab
```

---

# 📚 Conclusão

Neste desafio foi possível:

- containerizar uma aplicação web
- utilizar o Azure Container Registry
- realizar deploy no Azure Container Apps
- expor a aplicação publicamente

Esse fluxo representa um cenário real de **deploy de aplicações cloud-native utilizando contêineres na Azure**.