# ☸️ Módulo: Orquestração de Contêineres com Azure Kubernetes Service

Este módulo apresenta os conceitos e ferramentas utilizadas para **orquestrar contêineres na plataforma Microsoft Azure**, utilizando o **Azure Kubernetes Service (AKS)**.

Também são explorados serviços importantes como o **Azure Container Registry (ACR)**, responsável por armazenar e gerenciar imagens de contêiner utilizadas pelas aplicações executadas no cluster Kubernetes.

---

# 🧠 Azure Kubernetes Service (AKS)

O **Azure Kubernetes Service (AKS)** é um serviço gerenciado que permite executar aplicações em contêineres utilizando **Kubernetes**, sem a necessidade de administrar manualmente toda a infraestrutura do cluster.

Com o AKS é possível:

- executar aplicações containerizadas
- escalar aplicações automaticamente
- gerenciar workloads distribuídas
- realizar deploy contínuo de aplicações

---

# 📦 Azure Container Registry (ACR)

O **Azure Container Registry (ACR)** é um serviço de registro privado utilizado para:

- criar
- armazenar
- gerenciar
- versionar

imagens de contêiner utilizadas por aplicações.

Essas imagens podem ser utilizadas por:

- Azure Kubernetes Service
- Azure Container Apps
- Azure App Services
- pipelines de CI/CD

---

# 🚀 Casos de Uso do Container Registry

Entre os principais casos de uso do **ACR** estão:

- armazenamento de imagens Docker privadas
- integração com pipelines CI/CD
- versionamento de aplicações containerizadas
- distribuição segura de imagens para clusters Kubernetes

---

# 🛠 Gerenciando Imagens com Azure CLI e Docker

Para trabalhar com imagens no **Azure Container Registry**, utilizamos comandos da **Azure CLI** e do **Docker**.

### Login no Azure

```bash
az login
```

---

### Login no Azure Container Registry

```bash
az acr login --name mycontainerregistry
```

---

### Baixar uma imagem pública

```bash
docker pull mcr.microsoft.com/hello-world
```

---

### Criar tag da imagem para o ACR

```bash
docker tag mcr.microsoft.com/hello-world myacr.azurecr.io/hello-world:v1
```

---

### Enviar imagem para o ACR

```bash
docker push myacr.azurecr.io/hello-world:v1
```

---

### Remover imagem local

```bash
docker rmi myacr.azurecr.io/hello-world:v1
```

---

# 📥 Efetuar Pull e Remover Imagens do Registro

Também é possível recuperar ou remover imagens armazenadas no registro.

### Efetuar Pull da imagem

```bash
docker pull myacr.azurecr.io/hello-world:v1
```

---

### Remover imagem do ACR

```bash
az acr repository delete --name myacr --image hello-world:v1
```

---

# 🧩 Subindo uma Aplicação no ACR

Para realizar o deploy de uma aplicação no Kubernetes, primeiro precisamos **criar uma imagem Docker e enviá-la para o Azure Container Registry**.

---

# 🖥 Criando uma Aplicação de Teste

No **VSCode**, crie um arquivo simples chamado:

```
index.html
```

Exemplo de conteúdo:

```html
<h1>Landing Page Kubernetes</h1>
<p>Aplicação rodando no Azure Kubernetes Service</p>
```

---

# 🐳 Criando o Dockerfile

Crie um arquivo chamado **Dockerfile**.

```
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html
```

Esse Dockerfile cria uma imagem baseada no **Nginx** e copia a página HTML para dentro do servidor web.

---

# 🏗 Criando a Imagem Docker

Construir a imagem da aplicação:

```bash
docker build -t user/land:latest .
```

---

# ▶️ Executando o Contêiner Localmente

Executar o contêiner para testes locais:

```bash
docker run -d -p 80:80 user/land:latest
```

Agora a aplicação estará disponível em:

```
http://localhost
```

---

# ☁️ Enviando a Imagem para o Azure Container Registry

### Login no Azure

```bash
az login
```

---

### Login no ACR

```bash
az acr login --name nome_acr
```

---

### Criar tag da imagem para o ACR

```bash
docker tag user/land:latest nome_acr.azurecr.io/user/land:latest
```

---

### Enviar imagem para o ACR

```bash
docker push nome_acr.azurecr.io/user/land:latest
```

---

# ☸️ Conceitos Fundamentais do Kubernetes

Dentro do Kubernetes existem diferentes tipos de **workloads**, responsáveis por executar aplicações.

## Pod

O **Pod** é a menor unidade executável do Kubernetes.

Ele pode conter:

- um ou mais contêineres
- armazenamento compartilhado
- rede compartilhada

---

## ReplicaSet

O **ReplicaSet** garante que um número específico de pods esteja sempre em execução.

---

## Deployment

O **Deployment** é utilizado para gerenciar atualizações e replicação de pods.

Ele permite:

- escalabilidade
- rollback de versões
- atualizações controladas

---

## StatefulSets

Utilizado para aplicações que precisam de **estado persistente**, como bancos de dados.

---

## DaemonSets

Executa um pod em **todos os nós do cluster**.

Muito utilizado para:

- monitoramento
- logging
- agentes de segurança

---

## CronJobs

Executa tarefas agendadas no Kubernetes.

Exemplo:

- backups automáticos
- rotinas de processamento

---

# 🌐 Recursos de Rede no Kubernetes

## Service

Um **Service** expõe pods para acesso interno ou externo.

Tipos comuns:

- ClusterIP
- NodePort
- LoadBalancer

---

## Ingress

O **Ingress** gerencia o acesso HTTP/HTTPS para serviços dentro do cluster.

---

## Ingress Controller

Responsável por implementar as regras definidas em objetos **Ingress**.

---

# 🚀 Deploy da Aplicação no AKS

Após enviar a imagem para o ACR, podemos executar a aplicação no **Azure Kubernetes Service**.

---

# 📄 deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: curso-ia-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: curso-ia
  template:
    metadata:
      labels:
        app: curso-ia
    spec:
      containers:
      - name: curso-ia
        image: nome_acr.azurecr.io/user/land:latest
        ports:
        - containerPort: 80
```

---

# 📄 service.yaml

```yaml
apiVersion: v1
kind: Service
metadata:
  name: landing-page
spec:
  type: LoadBalancer
  selector:
    app: curso-ia
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
```

---

# 🔑 Conectando ao Cluster AKS

Para acessar o cluster Kubernetes criado no Azure:

```bash
az aks get-credentials --resource-group nome_resource_aks --name nome_aks
```

---

# 📦 Aplicando os Arquivos Kubernetes

Criar os recursos no cluster:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

---

# 🔎 Verificando o Serviço

Listar os serviços criados:

```bash
kubectl get svc landing-page
```

O Kubernetes retornará um **EXTERNAL-IP**, que será utilizado para acessar a aplicação.

---

# 🌍 Acessando a Aplicação

Após o provisionamento do **LoadBalancer**, a aplicação poderá ser acessada através do endereço público fornecido pelo Kubernetes.

---

# 📚 Conclusão

Neste módulo foram explorados conceitos fundamentais de **orquestração de contêineres utilizando Kubernetes na plataforma Azure**.

Foram abordados:

- Azure Container Registry
- Azure Kubernetes Service
- criação de imagens Docker
- envio de imagens para o ACR
- deploy de aplicações no AKS
- recursos fundamentais do Kubernetes

Esses conceitos são essenciais para o desenvolvimento de **arquiteturas cloud-native escaláveis e resilientes**.