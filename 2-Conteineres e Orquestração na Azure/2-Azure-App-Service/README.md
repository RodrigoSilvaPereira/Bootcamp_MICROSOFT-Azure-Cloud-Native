# 🌐 Módulo: Aplicações Web com Azure App Service

O **Azure App Service** é um serviço da plataforma Microsoft Azure baseado em **HTTP**, utilizado para hospedar:

- aplicações web
- APIs REST
- back-ends mobile

Ele permite que desenvolvedores publiquem aplicações rapidamente sem precisar gerenciar diretamente servidores, sistemas operacionais ou infraestrutura.

Os aplicativos hospedados podem ser executados em ambientes baseados em **Windows ou Linux**, com suporte nativo para diversas linguagens e frameworks.

---

# ☁️ O que é o Azure App Service

O **Azure App Service** é uma plataforma **PaaS (Platform as a Service)** que fornece um ambiente totalmente gerenciado para desenvolvimento, implantação e escalabilidade de aplicações web.

Com ele é possível:

- hospedar aplicações web
- criar APIs REST
- integrar pipelines de CI/CD
- escalar aplicações automaticamente
- gerenciar autenticação e segurança

---

# 🚀 Principais Recursos

O Azure App Service oferece diversos recursos importantes para aplicações modernas.

## Dimensionamento Automático

O serviço permite escalar aplicações automaticamente com base em:

- número de requisições
- uso de CPU
- uso de memória

Isso garante maior **disponibilidade e performance da aplicação**.

---

## Integração e Implantação Contínua (CI/CD)

O App Service possui integração nativa com ferramentas de deploy como:

- GitHub
- Azure DevOps
- Bitbucket
- Git

Isso permite implementar pipelines de **integração contínua e entrega contínua**.

---

## Deployment Slots

Os **slots de implantação** permitem publicar novas versões da aplicação sem afetar o ambiente de produção.

Exemplo de fluxo:

```
Production
Staging
Testing
```

Depois de validar a aplicação no slot de teste, é possível realizar **swap para produção** sem downtime.

---

# 📊 Planos do App Service

Os **App Service Plans** definem:

- recursos de computação
- capacidade de escalabilidade
- preço do serviço

Eles determinam **como a aplicação é executada e dimensionada**.

Entre os principais fatores controlados pelo plano estão:

- CPU
- memória
- número de instâncias
- escalabilidade automática

---

# 🏷 Camadas de Uso

O App Service possui diferentes camadas de serviço.

Exemplos:

- **Free** – ideal para testes e aprendizado
- **Shared** – recursos compartilhados
- **Basic** – aplicações simples
- **Standard** – suporte a autoscale
- **Premium** – alto desempenho e recursos avançados

Cada camada oferece diferentes níveis de **performance, escalabilidade e recursos de rede**.

---

# 🔐 Autenticação Integrada

O Azure App Service possui suporte nativo para autenticação utilizando diversos provedores de identidade.

Entre eles:

- Microsoft
- Google
- Facebook
- Apple
- OpenID Connect

Isso permite implementar autenticação em aplicações sem necessidade de desenvolver todo o sistema de login manualmente.

---

# 🌐 Recursos de Rede

O App Service oferece diferentes configurações de rede para atender diferentes cenários.

## Ambiente Multilocação

No modelo **multilocação**, várias aplicações compartilham a mesma infraestrutura gerenciada pela plataforma Azure.

Esse modelo oferece:

- alta escalabilidade
- baixo custo
- gerenciamento simplificado

---

## Ambiente de Locatário Único

No modelo de **locatário único**, a aplicação utiliza recursos dedicados.

Isso permite:

- maior controle de rede
- isolamento de infraestrutura
- maior segurança

---

# 🛠 Configurando e Publicando uma API em um Web App

A seguir está um exemplo de fluxo para publicar uma API no **Azure App Service**.

---

# 1️⃣ Criar um Resource Group

Primeiro crie um **Resource Group** para organizar os recursos da aplicação.

Esse grupo armazenará:

- Web App
- banco de dados
- configurações de rede
- outros serviços relacionados

---

# 2️⃣ Criar um Web App

Criar um novo recurso **Web App** no portal do Azure.

Durante a criação será necessário configurar:

- nome da aplicação
- assinatura
- resource group
- região

---

# 3️⃣ Configurar Instância e Stack

Selecionar:

- sistema operacional (Linux ou Windows)
- stack da aplicação

Exemplos de stacks suportadas:

- .NET
- Node.js
- Python
- Java
- PHP

---

# 4️⃣ Configurar Recursos Adicionais

Durante a criação do Web App também é possível configurar:

- **Database**
- **Deployment**
- **Network**
- **Tags**

Essas configurações permitem integrar a aplicação com outros serviços da plataforma.

---

# 5️⃣ Criar o Web App

Após revisar as configurações, finalize a criação do recurso.

O Azure provisionará automaticamente toda a infraestrutura necessária para executar a aplicação.

---

# 6️⃣ Criar uma API de Teste

Desenvolver uma pequena API utilizando a stack escolhida.

Exemplo de aplicações possíveis:

- API REST em .NET
- API Node.js
- API Python (Flask ou FastAPI)

Essa API será utilizada para testar o deploy no App Service.

---

# 7️⃣ Publicar a Aplicação

A aplicação pode ser publicada diretamente pelo **Visual Studio**.

Passos:

1. Clique em **Publish**
2. Selecione **Azure**
3. Escolha o **Web App criado**
4. Configure as opções de deploy

Após a publicação, o Visual Studio realizará automaticamente o **deploy da aplicação para o Azure**.

---

# 🌍 Acessando a Aplicação

Após a publicação, o Azure fornecerá uma URL pública semelhante a:

```
https://nome-do-app.azurewebsites.net
```

Essa URL poderá ser utilizada para acessar a aplicação ou API hospedada no App Service.

---

# 📚 Conclusão

O **Azure App Service** é uma solução poderosa para hospedar aplicações web e APIs na nuvem sem a necessidade de gerenciar infraestrutura.

Neste módulo foram apresentados conceitos importantes como:

- hospedagem de aplicações web na Azure
- planos de App Service
- dimensionamento automático
- autenticação integrada
- deployment de APIs

Esses recursos tornam o App Service uma ferramenta essencial para desenvolvimento de aplicações **cloud-native na plataforma Azure**.