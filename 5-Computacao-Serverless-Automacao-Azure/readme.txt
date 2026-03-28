# ⚡ Computação Serverless e Automação na Azure
Este diretório reúne conteúdos relacionados à **computação serverless na plataforma Microsoft Azure**, utilizando serviços como:

- **Azure Functions**
- **Azure Logic Apps**

O módulo aborda tanto os **conceitos fundamentais de execução baseada em eventos** quanto a **implementação prática de um serviço serverless**, aplicando validação, processamento e integração entre camadas.

---

# 📂 Estrutura do Módulo

Este módulo está dividido em duas partes principais: **conteúdo conceitual** e **desafio prático**.

---

# 📘 1 - Computação Serverless com Azure Functions

```
1-Computação-Serverless-Azure-Functions/
```

Contém a documentação dos principais conceitos relacionados ao modelo **serverless na Azure**.

Entre os tópicos abordados estão:

- funcionamento do Azure Functions
- gatilhos e associações (triggers e bindings)
- planos de hospedagem
- escalabilidade automática
- integração com serviços Azure
- comparação com Logic Apps e WebJobs

Esse conteúdo fornece a base para compreender **como construir aplicações orientadas a eventos e altamente escaláveis**.

---

# 🧪 2 - Desafio: Serviço Autenticador de Boletos

```
2-Desafio/
```

Contém um laboratório prático onde foi construída uma solução serverless para **validação de boletos**.

A aplicação implementada utiliza:

- **Azure Functions** para processamento backend
- **HTTP Trigger** para comunicação com a interface
- **Validação de código de barras** no backend
- **Interface web (HTML/JavaScript)** para interação com o usuário

Esse desafio demonstra na prática:

- criação de funções serverless
- processamento de requisições HTTP
- validação de dados em múltiplas camadas
- integração entre frontend e backend

---

# 🎯 Objetivo do Módulo

Ao final deste módulo é possível compreender:

- como funciona o modelo serverless na Azure
- como utilizar Azure Functions para processamento de eventos
- como integrar aplicações com serviços externos
- como construir APIs leves e escaláveis
- como aplicar validação e boas práticas em aplicações distribuídas

---

# ⚡ Visão Arquitetural

```
Usuário
   │
Interface Web (UI)
   │
HTTP Request
   │
Azure Functions (Serverless)
   │
Processamento e validação
   │
Resposta ao cliente
```

---

# 📚 Conclusão

A computação serverless com **Azure Functions e Logic Apps** permite construir aplicações modernas com:

- alta escalabilidade
- baixo custo operacional
- execução baseada em eventos
- integração com múltiplos serviços

A aplicação prática de validação de boletos demonstra como esses conceitos podem ser utilizados para criar soluções reais, eficientes e alinhadas com arquiteturas modernas baseadas em eventos.