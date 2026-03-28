# ⚡ Módulo: Computação Serverless com Azure Functions e Logic Apps

Este módulo apresenta os conceitos de **computação serverless na plataforma Microsoft Azure**, utilizando os serviços:

- **Azure Functions**
- **Azure Logic Apps**

Esses serviços permitem executar código e orquestrar processos **sem a necessidade de gerenciar infraestrutura**, focando apenas na lógica de negócio.

---

# ☁️ O que é Computação Serverless

A computação serverless é um modelo onde:

- você não gerencia servidores
- a infraestrutura é totalmente gerenciada pela nuvem
- o custo é baseado no uso
- a aplicação escala automaticamente

---

# ⚡ Azure Functions

O **Azure Functions** é um serviço serverless que permite executar código sob demanda baseado em eventos.

---

## 🎯 Principais Características

- execução baseada em eventos
- escalabilidade automática
- pagamento por execução
- suporte a múltiplas linguagens
- integração com diversos serviços Azure

---

## 📌 Casos de Uso

O Azure Functions é ideal para:

- processamento de imagens
- processamento de pedidos
- tarefas agendadas (cron jobs)
- automações
- pipelines de dados
- integração entre sistemas

---

# 🔁 Gatilhos e Associações (Triggers & Bindings)

## 🔥 Gatilhos (Triggers)

Os **gatilhos** definem quando uma função será executada.

Exemplos:

- HTTP
- Timer
- Queue (fila)
- Event Hub
- Blob Storage
- Service Bus

---

## 🔗 Associações (Bindings)

As **associações** conectam a função a outros serviços sem precisar escrever código de integração.

Tipos:

- entrada (`in`)
- saída (`out`)
- entrada/saída (`inout`)

---

## 📄 Exemplo de function.json

```json
{
  "bindings": [
    {
      "type": "queueTrigger",
      "direction": "in",
      "name": "order",
      "queueName": "orders",
      "connection": "STORAGE_ACCOUNT"
    },
    {
      "type": "table",
      "direction": "out",
      "name": "$return",
      "tableName": "OrdersTable",
      "connection": "STORAGE_ACCOUNT"
    }
  ]
}
```

---

## 🧠 Conceito Importante

- Cada função possui **apenas um gatilho**
- Pode ter **múltiplas associações**
- Evita código manual para integração com serviços

---

# ⚙️ Planos de Hospedagem do Azure Functions

## 🟢 Plano de Consumo

- escala automática
- cobrança por execução
- ideal para cargas variáveis
- cold start pode ocorrer

---

## 🟡 Plano Premium

- instâncias pré-aquecidas
- menor latência
- suporte a redes virtuais
- melhor para produção crítica

---

## 🔵 Plano Dedicado (App Service)

- executa em infraestrutura fixa
- controle total de recursos
- ideal para execuções longas

---

# 📏 Escalabilidade do Azure Functions

## 🔄 Como funciona

- escala baseada em eventos
- pode escalar até **200 instâncias**
- pode escalar para **zero (cold start)**

---

## ⚠️ Comportamentos Importantes

- HTTP: escala rápida
- eventos (fila, etc): escala gradual
- latência inicial (cold start)

---

## 🔒 Limite de Escala

Você pode limitar o número de instâncias:

```json
{
  "functionAppScaleLimit": 10
}
```

---

# 🧩 Azure Functions vs Logic Apps

| Característica        | Azure Functions                | Logic Apps                          |
|----------------------|------------------------------|-------------------------------------|
| Modelo               | Code-first                   | Designer-first (visual)             |
| Desenvolvimento      | Código                       | Fluxo declarativo                   |
| Conectividade        | Bindings + código            | Conectores prontos                  |
| Monitoramento        | Application Insights         | Azure Monitor                       |
| Complexidade lógica  | Alta                         | Média                               |
| Execução             | Local ou nuvem               | Nuvem                               |

---

# 🔄 Azure Functions vs WebJobs

| Característica              | Azure Functions | WebJobs |
|----------------------------|----------------|--------|
| Serverless                 | ✅              | ❌      |
| Escalabilidade automática  | ✅              | ❌      |
| Pagamento por uso          | ✅              | ❌      |
| Execução no navegador      | ✅              | ❌      |

---

# 🔧 Desenvolvimento com Azure Functions

Uma função possui dois elementos principais:

- código (Python, C#, JS, etc.)
- configuração (function.json)

---

## 📌 Estrutura básica

```python
def main(req):
    return "Hello Azure Functions"
```

---

# 🔌 Conectando com Serviços Azure

As conexões são feitas via:

- variáveis de ambiente
- Application Settings

Exemplo:

```
STORAGE_ACCOUNT=connection_string
```

---

## 🔐 Conexões Seguras

- uso de identidades gerenciadas (Managed Identity)
- controle via RBAC
- evita uso de secrets no código

---

# 🔄 Azure Logic Apps

O **Azure Logic Apps** é um serviço serverless para **automação de workflows**.

---

## 🎯 Principais Características

- desenvolvimento visual (low-code/no-code)
- integração com diversos serviços
- automação de processos
- conectores prontos (SaaS e on-premises)

---

## 🧩 Componentes

- **Trigger** → inicia o fluxo
- **Actions** → executam tarefas
- **Connectors** → integração com serviços

---

## 🔗 Conectividade Híbrida

- integração com sistemas locais
- suporte a Data Gateway
- integração com APIs e serviços Azure

---

# 📌 Casos de Uso

## ⚡ Azure Functions

- processamento de eventos em tempo real
- processamento assíncrono
- transformação de dados
- integração com APIs

---

## 🔄 Logic Apps

- automação de workflows
- integração com sistemas legados
- notificações automatizadas
- orquestração de processos

---

# 🎯 Quando usar cada um

| Cenário                          | Serviço recomendado |
|--------------------------------|-------------------|
| Lógica complexa                | Azure Functions   |
| Integração visual rápida       | Logic Apps        |
| Processamento de eventos       | Azure Functions   |
| Orquestração de processos      | Logic Apps        |

---

# 📚 Conclusão

Neste módulo foram abordados os conceitos de **computação serverless na Azure**, utilizando:

- Azure Functions
- Azure Logic Apps

Esses serviços permitem criar aplicações:

- escaláveis
- orientadas a eventos
- altamente integradas
- com baixo custo operacional

Eles são fundamentais para arquiteturas modernas como:

- microserviços
- pipelines de dados
- sistemas orientados a eventos