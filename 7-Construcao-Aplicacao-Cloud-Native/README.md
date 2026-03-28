# 🚗 Módulo Final: Aplicação Cloud-Native de Aluguel de Carros na Azure

Este projeto implementa uma aplicação completa de **aluguel de veículos (Rent-Car)** utilizando uma arquitetura **cloud-native, distribuída e orientada a eventos na Microsoft Azure**.

O sistema foi projetado utilizando **microsserviços, serverless e mensageria**, garantindo:

- escalabilidade
- desacoplamento
- resiliência
- alta disponibilidade

---

# 🧠 Visão Geral da Arquitetura

A aplicação é composta por múltiplos serviços integrados:

- Frontend (interface do usuário)
- Backend for Frontend (BFF)
- Azure Functions (processamento serverless)
- Service Bus (mensageria)
- Bancos de dados distribuídos
- Serviços de monitoramento e segurança

---

# 🏗 Arquitetura Geral

```
Usuário
   │
DNS
   │
Frontend (Container Apps)
   │
BFF (Node.js)
   │
Azure Function (RentProcess)
   │
PostgreSQL + Service Bus (PaymentQueue)
   │
Azure Function (PaymentProcess)
   │
Cosmos DB (Status de pagamento)
   │
Service Bus (NotificationQueue)
   │
Logic Apps (EmailNotification)
```

---

# 🧩 Componentes da Arquitetura

## 🌐 Frontend (Container Apps)

Interface do usuário responsável por:

- exibir veículos
- realizar solicitações de aluguel
- interagir com o backend

---

## 🔁 BFF (Backend For Frontend)

Responsável por:

- centralizar chamadas do frontend
- orquestrar serviços backend
- simplificar comunicação

---

## ⚙️ Azure Functions

### RentProcess

- processa solicitação de aluguel
- salva dados no PostgreSQL
- envia mensagem para fila de pagamento

### PaymentProcess

- consome mensagens da fila
- processa pagamento
- salva status no Cosmos DB
- envia evento para notificação

---

## 📨 Service Bus (Mensageria)

Filas utilizadas:

- **PaymentQueue**
- **NotificationQueue**

Função:

- desacoplar serviços
- garantir processamento assíncrono
- aumentar resiliência

---

## 🗄 Bancos de Dados

### PostgreSQL

- dados transacionais (aluguel)

### Cosmos DB

- status de pagamento (NoSQL)

---

## 📧 Logic Apps

Responsável por:

- envio de e-mails
- automação de notificações

---

## 🔐 Key Vault

Armazena:

- strings de conexão
- segredos
- credenciais

---

## 📊 Monitoramento

### Azure Monitor

- métricas
- logs

### Application Insights

- performance
- rastreamento de requisições

---

# 🔄 Fluxo da Aplicação

1. Usuário acessa o sistema via DNS
2. Frontend envia requisição ao BFF
3. BFF chama a Function **RentProcess**
4. RentProcess:
   - salva no PostgreSQL
   - envia mensagem para **PaymentQueue**
5. PaymentProcess:
   - consome a fila
   - processa pagamento
   - salva status no Cosmos DB
   - envia mensagem para **NotificationQueue**
6. Logic App:
   - consome a fila
   - envia e-mail ao usuário

---

# 🛠️ Passo a Passo de Implementação

## 1️⃣ Criar Resource Group

```bash
az group create --name lab007 --location eastus
```

---

## 2️⃣ Criar Azure Container Registry (ACR)

```bash
az acr create \
  --resource-group lab007 \
  --name acrlab007 \
  --sku Basic
```

Login:

```bash
az acr login --name acrlab007
```

---

## 3️⃣ Criar Container Apps

```bash
az containerapp env create \
  --name capp-dev-eastus \
  --resource-group lab007 \
  --location eastus
```

---

## 4️⃣ Build e Push da Imagem

```bash
docker build -t rentcar-app .
docker tag rentcar-app acrlab007.azurecr.io/rentcar-app:v1
docker push acrlab007.azurecr.io/rentcar-app:v1
```

---

## 5️⃣ Criar Azure Functions

### RentProcess

```bash
az functionapp create \
  --name fapp-lab007-dev-eastus \
  --resource-group lab007 \
  --consumption-plan-location eastus \
  --runtime dotnet \
  --os-type Linux \
  --storage-account <storage>
```

---

### PaymentProcess

```bash
az functionapp create \
  --name fnapp-paymentProcess-dev-east-us \
  --resource-group lab007 \
  --runtime dotnet \
  --os-type Linux \
  --storage-account <storage>
```

---

## 6️⃣ Criar Service Bus

```bash
az servicebus namespace create \
  --name sb-dev-eastus \
  --resource-group lab007 \
  --location eastus \
  --sku Basic
```

Criar filas:

```bash
az servicebus queue create --name paymentqueue --namespace-name sb-dev-eastus
az servicebus queue create --name notificationqueue --namespace-name sb-dev-eastus
```

---

## 7️⃣ Criar Banco PostgreSQL

```bash
az postgres flexible-server create \
  --resource-group lab007 \
  --name postgres-lab007 \
  --location eastus
```

---

## 8️⃣ Criar Cosmos DB

```bash
az cosmosdb create \
  --name cdb-dev-westus \
  --resource-group lab007 \
  --locations regionName=westus
```

---

## 9️⃣ Criar Logic App

- criar via portal
- configurar trigger (Service Bus)
- enviar e-mail

---

## 🔟 Criar Key Vault

```bash
az keyvault create \
  --name akv-dev-eastus \
  --resource-group lab007 \
  --location eastus
```

---

# ⚙️ Configuração das Functions

## RentProcess

Responsável por:

- inserir dados no PostgreSQL
- enviar mensagem para Service Bus

---

## PaymentProcess

Responsável por:

- consumir fila
- atualizar Cosmos DB
- enviar notificação

---

# 🔐 Configuração de Variáveis

Exemplo:

```
SERVICE_BUS_CONNECTION
POSTGRES_CONNECTION
COSMOS_CONNECTION
QUEUE_NAME
```

---

# 📦 Boas Práticas Aplicadas

## Arquitetura

- Microsserviços
- Serverless
- Event-driven

---

## Escalabilidade

- Azure Functions (auto scale)
- Service Bus (buffer)

---

## Segurança

- Key Vault
- isolamento de serviços

---

## Observabilidade

- Application Insights
- Azure Monitor

---

# 📊 Padrões Arquiteturais Utilizados

| Padrão | Uso |
|------|------|
| Microsserviços | separação de responsabilidades |
| Serverless | processamento sob demanda |
| Event-driven | comunicação assíncrona |
| BFF | otimização do frontend |
| Multi-database | melhor uso por contexto |

---

# 🎯 Conclusão

Este projeto demonstra a construção de uma aplicação moderna utilizando:

- arquitetura cloud-native
- microsserviços
- processamento assíncrono
- múltiplos serviços Azure integrados

A solução garante:

- alta escalabilidade
- baixo acoplamento
- resiliência
- facilidade de evolução

---

# 🚀 Próximos Passos (Melhorias)

- autenticação com Azure AD
- CI/CD com GitHub Actions
- uso de Terraform/Bicep
- implementação de cache (Redis)
- API Management
