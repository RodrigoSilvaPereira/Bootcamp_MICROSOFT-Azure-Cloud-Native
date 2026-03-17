# 🐳 Módulo: Aplicações Contêinerizadas com Azure Container Apps

O **Azure Container Apps** é um serviço serverless da plataforma Microsoft Azure voltado para execução de aplicações baseadas em contêineres, com foco em **microserviços e escalabilidade automática**.

Ele elimina a necessidade de gerenciar infraestrutura complexa, como clusters Kubernetes, oferecendo um ambiente totalmente gerenciado para execução de contêineres.

---

# ☁️ O que é o Azure Container Apps

O **Azure Container Apps** é uma solução que permite executar aplicações containerizadas com características de:

- execução serverless
- escalabilidade automática
- ambiente totalmente gerenciado
- suporte a microserviços
- integração com eventos e workflows

Diferente do Kubernetes, o desenvolvedor não precisa gerenciar:

- nós do cluster
- control plane
- upgrades
- networking avançado

---

# 🚀 Principais Características

## Execução Serverless

Os containers são executados sob demanda, sem necessidade de provisionar servidores manualmente.

---

## Escalabilidade Automática

O serviço escala automaticamente com base em:

- requisições HTTP
- eventos
- filas
- métricas customizadas

---

## Ambiente Gerenciado

Toda a infraestrutura é abstraída, permitindo foco total na aplicação.

---

## Suporte a Microserviços

Ideal para arquiteturas distribuídas, onde cada serviço roda em seu próprio container.

---

## Integração com Eventos

Permite integração com serviços como:

- filas
- eventos
- mensageria

---

# 📌 Casos de Uso

O Azure Container Apps é ideal para:

- aplicações web e APIs
- arquiteturas de microserviços
- processamento orientado a eventos
- ambientes de desenvolvimento e teste
- workloads intermitentes (scale-to-zero)

---

# ⚖️ Comparativo: AKS vs Container Apps vs App Service

| Critério                     | AKS (Kubernetes)                | Container Apps                    | App Service                     |
|----------------------------|--------------------------------|----------------------------------|--------------------------------|
| Complexidade               | Alta                           | Média/Baixa                      | Baixa                          |
| Gerenciamento              | Manual (cluster)               | Gerenciado                       | Totalmente gerenciado          |
| Suporte a Containers       | Completo (nativo Kubernetes)   | Nativo                           | Limitado (via Web App for Containers) |
| Escalabilidade             | Altamente configurável         | Automática (KEDA)                | Automática                     |
| Flexibilidade              | Máxima                         | Alta                             | Média                          |
| Customização               | Total                          | Moderada                         | Limitada                       |
| Casos de Uso               | Microsserviços complexos       | Microsserviços simples/moderados | Web apps e APIs                |
| Integração DevOps          | Alta                           | Alta                             | Alta                           |

---

# 🧠 Conceito: KEDA (Kubernetes Event-Driven Autoscaling)

O **KEDA (Kubernetes Event-Driven Autoscaling)** é um componente responsável por escalar aplicações com base em eventos.

Ele permite escalar containers com base em:

- mensagens em filas
- eventos de streaming
- métricas externas

No Azure Container Apps, o KEDA é utilizado internamente para permitir:

- scale automático
- scale-to-zero (quando não há uso)

---

# 🧩 Arquitetura Interna

## Ambiente de Container Apps

Todos os aplicativos são executados dentro de um:

```
Container Apps Environment
```

Esse ambiente gerencia:

- rede
- logs
- observabilidade
- integração com outros serviços

---

## Revisões (Revisions)

Cada alteração no aplicativo gera uma nova **revisão**.

Permite:

- versionamento de aplicações
- rollback
- deploy controlado

---

## Segredos (Secrets)

Permitem armazenar dados sensíveis como:

- senhas
- strings de conexão
- tokens

Esses dados não ficam expostos no código.

---

## Sidecar Pattern

É possível rodar múltiplos containers no mesmo app.

Exemplo:

- API principal
- container de logging
- container de monitoramento

---

# 🚀 Implantação de um Aplicativo no Container Apps

O Azure Container Apps permite deploy de imagens hospedadas em:

- Azure Container Registry
- Docker Hub
- outros registros privados

---

# 🛠 Criando Ambiente via Azure CLI

## Instalar extensão do Container Apps

```bash
az extension add --name containerapp --upgrade
```

Adiciona suporte ao Azure Container Apps na CLI.

---

## Registrar provedores necessários

```bash
az provider register --namespace Microsoft.App
az provider register --namespace Microsoft.OperationalInsights
```

Habilita os serviços necessários no subscription.

---

## Definir variáveis de ambiente

```bash
myRG=rodrigocontainerapp
myLocation=eastus
myAppContainerEnv=rodrigo-env-001
```

Define:

- Resource Group
- Região
- Ambiente de Container Apps

---

## Criar Resource Group

```bash
az group create --name $myRG --location $myLocation
```

Cria o agrupamento de recursos na Azure.

---

## Criar ambiente do Container Apps

```bash
az containerapp env create \
--name $myAppContainerEnv \
--resource-group $myRG \
--location $myLocation
```

Cria o ambiente onde os containers serão executados.

---

## Criar o Container App

```bash
az containerapp create \
--name rodrigocontainerapp \
--resource-group $myRG \
--location $myLocation \
--environment $myAppContainerEnv \
--image mcr.microsoft.com/azuredocs/containerapps-helloworld:latest \
--target-port 80 \
--ingress external \
--query properties.configuration.ingress.fqdn
```

### Explicação dos parâmetros:

- `--name` → nome do container app
- `--resource-group` → grupo de recursos
- `--environment` → ambiente criado
- `--image` → imagem do container
- `--target-port` → porta da aplicação
- `--ingress external` → expõe publicamente
- `--query` → retorna a URL pública da aplicação

---

# 🌍 Acessando a Aplicação

Após o deploy, será gerado um endpoint público semelhante a:

```
https://nome-app.region.azurecontainerapps.io
```

---

# 📚 Conclusão

O **Azure Container Apps** é uma solução moderna para execução de aplicações containerizadas, oferecendo um equilíbrio entre:

- simplicidade (App Service)
- flexibilidade (Kubernetes)

Ele é ideal para cenários onde se deseja:

- usar containers
- escalar automaticamente
- evitar complexidade de infraestrutura

Esse serviço se posiciona como uma excelente opção para arquiteturas **cloud-native baseadas em microserviços**.