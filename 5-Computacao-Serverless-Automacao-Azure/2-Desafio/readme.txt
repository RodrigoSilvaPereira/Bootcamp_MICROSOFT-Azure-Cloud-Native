# 💳 Desafio: Criando um Serviço Autenticador de Boletos com Azure Functions

Este desafio tem como objetivo construir um serviço serverless capaz de:

- receber um boleto
- validar seu código de barras
- processar informações
- retornar dados validados

A solução utiliza **Azure Functions** para processamento e pode incluir uma camada de interface (UI) para interação com o usuário.

---

# 🎯 Objetivo

Criar um sistema de autenticação de boletos com:

- validação de código de barras
- processamento serverless
- integração entre frontend e backend
- boas práticas de arquitetura

---

# 🧱 Arquitetura da Solução

```
Usuário
   │
UI (Interface Web)
   │
HTTP Request
   │
Azure Functions
   │
Validação e processamento
   │
Resposta (dados do boleto)
```

---

# ☁️ 1️⃣ Criar Resource Group

```bash
az group create --name RG-Boletos --location eastus
```

---

# ⚙️ 2️⃣ Criar Function App

```bash
az functionapp create \
--resource-group RG-Boletos \
--consumption-plan-location eastus \
--runtime python \
--functions-version 4 \
--name func-boletos-rodrigo \
--storage-account storageboletos001
```

---

# 📦 3️⃣ Estrutura do Projeto

```
/boletos-function
│
├── function_app.py
├── requirements.txt
└── .env
```

---

# 🔢 4️⃣ Recuperando o Código de Barras

O código de barras de um boleto normalmente contém:

- banco emissor
- valor
- data de vencimento
- identificador

Exemplo de entrada:

```
34191790010104351004791020150008291070026000
```

---

# 🧠 5️⃣ Implementando a Azure Function

## 📄 function_app.py

```python
import azure.functions as func
import json

def validar_codigo_barras(codigo):
    return len(codigo) in [44, 47] and codigo.isdigit()

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        codigo = body.get("codigo_barras")

        if not codigo:
            return func.HttpResponse("Código não informado", status_code=400)

        if not validar_codigo_barras(codigo):
            return func.HttpResponse("Código inválido", status_code=400)

        return func.HttpResponse(
            json.dumps({
                "status": "válido",
                "codigo": codigo
            }),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
```

---

# 🔐 6️⃣ Criando Namespace e Configuração do Lab

No contexto do Azure:

- criar Function App
- configurar Storage Account
- definir variáveis de ambiente

Exemplo:

```bash
az storage account create \
--name storageboletos001 \
--resource-group RG-Boletos \
--location eastus \
--sku Standard_LRS
```

---

# 🌐 7️⃣ Criando a Camada de UI

Você pode criar uma interface simples com HTML + JS.

## 📄 index.html

```html
<!DOCTYPE html>
<html>
<head>
  <title>Validador de Boletos</title>
</head>
<body>

<h2>Validador de Boletos</h2>

<input type="text" id="codigo" placeholder="Digite o código de barras">
<button onclick="validar()">Validar</button>

<p id="resultado"></p>

<script>
async function validar() {
  const codigo = document.getElementById("codigo").value;

  const response = await fetch("URL_DA_FUNCTION", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ codigo_barras: codigo })
  });

  const data = await response.text();
  document.getElementById("resultado").innerText = data;
}
</script>

</body>
</html>
```

---

# ✅ 8️⃣ Validações na Camada de UI

Antes de enviar para o backend:

- verificar se está vazio
- validar tamanho mínimo
- permitir apenas números

Exemplo:

```javascript
if (!codigo || codigo.length < 44) {
  alert("Código inválido");
  return;
}
```

---

# 🔐 9️⃣ Boas Práticas de Segurança

- validar dados no frontend e backend
- nunca confiar apenas na UI
- usar HTTPS
- aplicar autenticação (opcional com API Management)
- proteger variáveis sensíveis

---

# 🚀 🔟 Publicando a Function

```bash
func azure functionapp publish func-boletos-rodrigo
```

---

# 🧪 1️⃣1️⃣ Testando o Serviço

Exemplo com curl:

```bash
curl -X POST URL_DA_FUNCTION \
-H "Content-Type: application/json" \
-d '{"codigo_barras": "34191790010104351004791020150008291070026000"}'
```

---

# 📊 Fluxo Completo

```
Usuário digita código
   ↓
UI valida entrada
   ↓
Requisição HTTP
   ↓
Azure Function valida e processa
   ↓
Resposta ao usuário
```

---

# 📚 Conclusão

Neste desafio foi possível:

- criar um serviço serverless com Azure Functions
- validar códigos de barras de boletos
- implementar uma interface simples
- aplicar boas práticas de validação e segurança

Esse tipo de solução é aplicável em:

- fintechs
- sistemas de pagamento
- validação de documentos
- APIs financeiras