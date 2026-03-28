# 🔌 Gerenciamento de segurança em APIs com Azure API Management

Este diretório reúne conteúdos relacionados ao **gerenciamento, segurança e exposição de APIs na plataforma Microsoft Azure**, utilizando o serviço **Azure API Management (APIM)**.

O módulo aborda tanto os **conceitos fundamentais de governança de APIs** quanto a **implementação prática de uma API segura**, aplicando autenticação, controle de acesso e boas práticas de arquitetura.

---

# 📂 Estrutura do Módulo

Este módulo está dividido em duas partes principais: **conteúdo conceitual** e **desafio prático**.

---

# 📘 1 - Gerenciamento de APIs com Azure API Management

```
1-Gerenciamento-APIs-Azure-API-Management/
```

Contém a documentação dos principais conceitos relacionados ao **Azure API Management**.

Entre os tópicos abordados estão:

- papel do gerenciamento de APIs
- funcionamento do API Gateway
- organização de APIs em produtos e grupos
- uso de políticas para controle e segurança
- autenticação e proteção de APIs
- monitoramento e governança

Esse conteúdo fornece a base teórica para compreender **como expor e gerenciar APIs de forma segura e escalável**.

---

# 🧪 2 - Desafio: API de Pagamentos Segura

```
2-Desafio/
```

Contém um laboratório prático onde foi construída uma **API de pagamentos segura**, utilizando serviços da Azure.

A solução implementada utiliza:

- **Azure App Service** para hospedagem da API
- **Azure API Management** para gerenciamento e proteção
- **JWT (JSON Web Token)** para autenticação
- **Azure Active Directory** para emissão de tokens

Esse desafio demonstra na prática:

- criação e publicação de APIs
- aplicação de autenticação baseada em token
- uso de API Gateway para proteção
- aplicação de políticas de segurança e controle de acesso

---

# 🎯 Objetivo do Módulo

Ao final deste módulo é possível compreender:

- como funciona o gerenciamento de APIs na Azure
- como proteger APIs utilizando autenticação moderna (JWT)
- como utilizar API Gateway para controle e segurança
- como aplicar boas práticas no design de APIs REST
- como expor APIs de forma segura para clientes e parceiros

---

# 🔐 Visão Arquitetural

```
Cliente
   │
JWT (Azure AD)
   │
Azure API Management (Gateway)
   │
Azure App Service (API)
   │
Backend (Lógica de Negócio)
```

---

# 📚 Conclusão

O **Azure API Management** é uma peça fundamental em arquiteturas modernas baseadas em APIs, permitindo:

- controle de acesso
- segurança centralizada
- monitoramento de uso
- governança de serviços

A combinação com autenticação via **JWT e Azure Active Directory** garante que as APIs sejam expostas de forma **segura, escalável e profissional**, seguindo padrões utilizados no mercado.