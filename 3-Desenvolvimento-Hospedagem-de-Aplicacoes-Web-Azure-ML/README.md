# 🐳 Aplicações Contêinerizadas com Azure Container Apps

Este diretório reúne conteúdos relacionados à **execução de aplicações containerizadas na plataforma Microsoft Azure**, utilizando o serviço **Azure Container Apps**.

O módulo aborda tanto os **conceitos fundamentais** quanto a **aplicação prática** do uso de contêineres em ambientes cloud-native, com foco em **simplicidade, escalabilidade automática e arquitetura baseada em microserviços**.

---

# 📂 Estrutura do Módulo

Este módulo está dividido em duas partes principais: **conteúdo conceitual** e **desafio prático**.

---

# 📘 1 - Aplicações Contêinerizadas com Azure Container Apps

```
1-Aplicacoes-Conteinerizadas-Azure-Container-Apps/
```

Contém a documentação dos principais conceitos relacionados ao **Azure Container Apps**.

Entre os tópicos abordados estão:

- execução serverless de contêineres
- escalabilidade automática com KEDA
- suporte a microserviços
- gerenciamento de revisões e segredos
- integração com eventos
- comparação entre AKS, Container Apps e App Service

Esse conteúdo fornece a base teórica para compreender **quando e como utilizar o Azure Container Apps em arquiteturas modernas**.

---

# 🧪 2 - Desafio: Deploy de Aplicação Containerizada

```
2-Desafio/
```

Contém um laboratório prático onde foi realizado o deploy de uma aplicação web simples utilizando contêineres na Azure.

A solução implementada utiliza:

- **Docker** para containerização da aplicação
- **Azure Container Registry (ACR)** para armazenamento da imagem
- **Azure Container Apps** para execução da aplicação

Esse desafio demonstra na prática:

- criação de imagens Docker
- envio de imagens para o ACR
- deploy de aplicações containerizadas
- exposição de aplicações na internet

---

# 🎯 Objetivo do Módulo

Ao final deste módulo é possível compreender:

- como funciona a execução de contêineres na Azure
- as vantagens do modelo serverless para containers
- como escalar aplicações automaticamente
- como realizar deploy de aplicações containerizadas
- como integrar serviços de container na prática

---

# 📚 Conclusão

O **Azure Container Apps** oferece uma abordagem moderna para execução de aplicações containerizadas, combinando:

- simplicidade de uso
- escalabilidade automática
- baixo overhead operacional

Esse serviço se posiciona como uma excelente alternativa entre:

- **Azure App Service** (mais simples)
- **Azure Kubernetes Service (AKS)** (mais avançado)

Sendo ideal para aplicações que exigem **flexibilidade com menor complexidade de gerenciamento**.