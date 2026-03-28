# 🔐 Desafio: Criando uma API de Pagamentos Segura com Azure API Management

Este desafio tem como objetivo construir e proteger uma **API de pagamentos** utilizando serviços da plataforma Microsoft Azure.

A solução envolve:

- criação de uma API
- hospedagem no Azure App Service
- autenticação com JWT
- gerenciamento e proteção via Azure API Management

---

# 🎯 Objetivo

Construir uma arquitetura segura para exposição de APIs, incluindo:

- autenticação baseada em token (JWT)
- controle de acesso via API Management
- boas práticas de endpoints REST

---

# 🧱 Arquitetura da Solução

```
Cliente
   │
JWT (Bearer Token)
   │
Azure API Management
   │
Azure App Service (API)
   │
Lógica de Pagamentos
```

---

# 🖥 1️⃣ Criar a API de Pagamentos

Você pode utilizar qualquer stack. Exemplo com **Python + FastAPI**:

## 📄 main.py

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

payments = []

@app.post("/payments")
def create_payment(amount: float):
    payment = {"id": len(payments) + 1, "amount": amount}
    payments.append(payment)
    return payment

@app.get("/payments")
def list_payments():
    return payments
```

---

# 🧪 Boas Práticas de Endpoints

Utilize padrões REST:

| Método | Endpoint        | Descrição              |
|--------|----------------|-----------------------|
| GET    | /payments      | Listar pagamentos     |
| POST   | /payments      | Criar pagamento       |
| GET    | /payments/{id} | Buscar pagamento      |

Boas práticas:

- usar substantivos (payments)
- evitar verbos na URL
- utilizar status HTTP corretos
- versionar APIs (ex: /v1/payments)

---

# ☁️ 2️⃣ Criar Resource Group

```bash
az group create --name RG-APIPagamento --location eastus
```

---

# 🌐 3️⃣ Criar Azure App Service

```bash
az appservice plan create \
--name plan-api-pagamento \
--resource-group RG-APIPagamento \
--sku B1 \
--is-linux
```

---

# 🚀 4️⃣ Criar Web App

```bash
az webapp create \
--resource-group RG-APIPagamento \
--plan plan-api-pagamento \
--name api-pagamento-rodrigo \
--runtime "PYTHON:3.10"
```

---

# 📦 5️⃣ Publicar API

Você pode publicar via:

- VS Code
- GitHub Actions
- ZIP Deploy

Exemplo:

```bash
az webapp up --name api-pagamento-rodrigo
```

---

# 🔐 6️⃣ Criar Autenticação com JWT

## 🧠 O que é JWT

JWT (JSON Web Token) é um token usado para autenticação contendo:

- Header
- Payload
- Signature

---

## 🔑 Exemplo de Token

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

# 🔐 7️⃣ Integrar com Azure AD

Criar autenticação com Azure Active Directory:

### Criar App Registration

1. Acesse Azure Portal  
2. Vá em **Azure Active Directory**  
3. Clique em **App registrations**  
4. Crie um novo app  

---

### Configurar:

- Nome: API Pagamentos
- Redirect URI (opcional)
- Salvar Application (client) ID

---

# 🔑 8️⃣ Proteger API com JWT no API Management

Após criar o API Management, adicione a API e configure política de validação:

## 📄 Política JWT

```xml
<validate-jwt header-name="Authorization" failed-validation-httpcode="401">
    <openid-config url="https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration" />
    <required-claims>
        <claim name="aud">
            <value>api-client-id</value>
        </claim>
    </required-claims>
</validate-jwt>
```

---

# 🔌 9️⃣ Criar Azure API Management

```bash
az apim create \
--name apim-pagamentos \
--resource-group RG-APIPagamento \
--publisher-email seuemail@email.com \
--publisher-name Rodrigo \
--sku-name Consumption
```

---

# 🔗 🔟 Importar API para o API Management

Você pode importar via:

- OpenAPI (Swagger)
- URL da API
- Manualmente

---

# ⚙️ 1️⃣1️⃣ Aplicar Políticas de Segurança

No API Management:

- validar JWT
- aplicar rate limit
- habilitar logging

Exemplo de rate limit:

```xml
<rate-limit calls="100" renewal-period="60" />
```

---

# 🌍 1️⃣2️⃣ Testar API

Use ferramentas como:

- Postman
- curl

Exemplo:

```bash
curl -H "Authorization: Bearer TOKEN" \
https://apim-url/payments
```

---

# 📊 Fluxo Completo

```
Cliente
   ↓
JWT Token (Azure AD)
   ↓
API Management (validação + políticas)
   ↓
App Service (API)
   ↓
Resposta segura
```

---

# ⚠️ Boas Práticas de Segurança

- nunca expor API diretamente
- sempre usar API Gateway
- validar tokens JWT
- aplicar rate limiting
- usar HTTPS obrigatório
- proteger segredos (Key Vault recomendado)

---

# 🧹 Limpeza de Recursos

```bash
az group delete --name RG-APIPagamento
```

---

# 📚 Conclusão

Neste desafio foi possível:

- criar uma API de pagamentos
- hospedar no Azure App Service
- implementar autenticação com JWT
- proteger a API com Azure API Management

Essa arquitetura representa um padrão real de mercado para construção de **APIs seguras e escaláveis na nuvem**.