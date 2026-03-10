# ☁️ Módulo: Fundamento das Aplicações na Azure

Este módulo apresenta os conceitos fundamentais da **computação em nuvem** e da **plataforma Microsoft Azure**, abordando modelos de serviço, arquitetura da plataforma e os principais recursos utilizados para construir aplicações modernas na nuvem.

O Microsoft Azure fornece uma infraestrutura global que permite desenvolver, implantar e escalar aplicações com **alta disponibilidade, segurança e escalabilidade**, reduzindo a necessidade de gerenciamento direto de infraestrutura física.

---

# 🌐 Computação em Nuvem

A **computação em nuvem** é o fornecimento de recursos de tecnologia da informação através da internet, permitindo acesso sob demanda a serviços como:

- Processamento
- Armazenamento
- Redes
- Bancos de dados
- Serviços de aplicações

Esses recursos são disponibilizados por provedores de nuvem e cobrados geralmente no modelo **pay-as-you-go (pague pelo uso)**.

---

# 🚀 Benefícios da Nuvem

Entre os principais benefícios da computação em nuvem estão:

### Alta disponibilidade
Serviços distribuídos globalmente que garantem funcionamento contínuo das aplicações.

### Escalabilidade
Capacidade de aumentar ou reduzir recursos de acordo com a demanda.

### Elasticidade
Expansão automática de recursos conforme o uso da aplicação.

### Confiabilidade
Infraestrutura com redundância e replicação de dados.

### Segurança
Provedores de nuvem oferecem múltiplas camadas de segurança física e digital.

### Custo sob demanda
Pagamento apenas pelos recursos utilizados.

---

# ☁️ Tipos de Serviço na Nuvem

Existem três principais modelos de serviço em computação em nuvem.

## IaaS — Infrastructure as a Service

No modelo **Infraestrutura como Serviço**, o provedor disponibiliza recursos básicos de infraestrutura.

O usuário é responsável por gerenciar:

- Sistema operacional
- Aplicações
- Configurações
- Segurança

Exemplos de recursos:

- Máquinas virtuais
- Redes virtuais
- Discos de armazenamento

---

## PaaS — Platform as a Service

No modelo **Plataforma como Serviço**, o provedor gerencia a infraestrutura e fornece um ambiente para desenvolvimento e execução de aplicações.

O desenvolvedor precisa se preocupar apenas com:

- Código da aplicação
- Configuração do serviço

Exemplos:

- Azure App Service
- Azure Functions
- Azure Container Apps

---

## SaaS — Software as a Service

No modelo **Software como Serviço**, o usuário apenas utiliza a aplicação pela internet.

Toda a infraestrutura e gerenciamento ficam sob responsabilidade do provedor.

Exemplos:

- Microsoft Office 365
- Outlook
- Canvas
- Microsoft Teams

---

# 🔐 Modelo de Responsabilidade Compartilhada

Na computação em nuvem, a responsabilidade pela segurança e gerenciamento é compartilhada entre **provedor de nuvem** e **cliente**.

### Provedor de Nuvem (Microsoft Azure)

Responsável por:

- Infraestrutura física
- Datacenters
- Rede global
- Hardware
- Segurança física

### Cliente

Responsável por:

- Dados
- Configuração das aplicações
- Controle de acesso
- Identidade e autenticação
- Segurança do sistema operacional (dependendo do modelo)

Quanto mais alto o nível do serviço (SaaS), menor é a responsabilidade do cliente.

---

# 🏗 Componentes da Arquitetura do Azure

## Regiões

As **Regiões do Azure** são compostas por um ou mais datacenters localizados em uma área geográfica específica.

Características:

- Datacenters próximos fisicamente
- Baixa latência
- Alta disponibilidade
- Conformidade com regulamentações locais de dados

---

## Zonas de Disponibilidade

As **Zonas de Disponibilidade** são datacenters fisicamente separados dentro de uma mesma região.

Cada zona possui:

- Energia independente
- Rede independente
- Sistema de resfriamento próprio

Isso garante maior **resiliência contra falhas de datacenter**.

---

## Pares de Região

As regiões do Azure são organizadas em **pares de regiões** para garantir redundância geográfica.

Características:

- Distância mínima de aproximadamente **300 milhas**
- Replicação automática de alguns serviços
- Atualizações distribuídas entre regiões
- Prioridade de recuperação em caso de falhas

---

## Regiões Soberanas do Azure

Regiões soberanas são ambientes de nuvem projetados para atender requisitos específicos de **segurança, privacidade e conformidade governamental**.

Exemplo:

- **Azure Government**

Essas regiões são utilizadas por órgãos governamentais e instituições que exigem maior controle sobre dados.

---

# 📦 Recursos do Azure

Os **recursos do Azure** são os componentes utilizados para construir soluções na nuvem.

Exemplos de recursos:

- Máquinas Virtuais
- Contas de Armazenamento
- Redes Virtuais
- Serviços de Aplicação
- Bancos de dados SQL
- Azure Functions

---

## Grupo de Recursos

Um **Grupo de Recursos** é um contêiner lógico utilizado para organizar e gerenciar recursos relacionados.

Características:

- Agrupa recursos de uma solução
- Facilita gerenciamento e monitoramento
- Cada recurso pertence a apenas um grupo

---

# 🧾 Assinaturas do Azure

Uma **assinatura do Azure** fornece acesso autenticado e autorizado aos serviços da plataforma.

Ela é utilizada para:

- Controle de cobrança
- Gerenciamento de recursos
- Controle de acesso

Cada assinatura possui:

- Limites de uso
- Estrutura de cobrança
- Permissões de acesso

---

# 💻 Computação e Redes

Os serviços de **computação do Azure** fornecem recursos sob demanda para executar aplicações e workloads.

Principais serviços:

- Máquinas Virtuais
- Azure App Services
- Instâncias de Contêiner
- Azure Kubernetes Service (AKS)
- Área de Trabalho Virtual

---

# 🐳 Serviços de Contêiner

Os contêineres no Azure fornecem um ambiente leve para execução de aplicações sem a necessidade de gerenciar sistemas operacionais completos.

## Azure Container Instances

Permite executar contêineres diretamente na nuvem sem gerenciar infraestrutura.

---

## Azure Container Apps

Plataforma gerenciada para execução de aplicações em contêineres com escalabilidade automática.

---

## Azure Kubernetes Service (AKS)

Serviço gerenciado de **orquestração de contêineres**, ideal para aplicações distribuídas e arquiteturas de microsserviços.

---

# ⚡ Azure Functions

O **Azure Functions** é um serviço serverless que executa código baseado em eventos.

Características:

- Execução sob demanda
- Escalabilidade automática
- Pagamento apenas pelo tempo de execução

É muito utilizado para:

- automações
- processamento de eventos
- integração de sistemas

---

# 🌐 Serviços de Rede

O Azure fornece diversos serviços de rede para conectar recursos e aplicações com segurança.

Principais exemplos:

- Redes Virtuais (Virtual Network)
- Balanceadores de carga
- DNS do Azure

---

# 💾 Armazenamento no Azure

O **Azure Storage** fornece soluções escaláveis e altamente disponíveis para armazenamento de dados.

---

# 📦 Contas de Armazenamento

Uma **Conta de Armazenamento** fornece acesso a diferentes serviços de armazenamento do Azure.

Características:

- Nome único global
- Acesso via internet
- Configuração de redundância

---

# 🔁 Configurações de Redundância

O Azure oferece diferentes níveis de redundância para proteger dados.

### LRS — Local Redundant Storage
Mantém múltiplas cópias dentro de um único datacenter.

### ZRS — Zone Redundant Storage
Replica dados entre diferentes zonas de disponibilidade.

### GRS — Geo Redundant Storage
Replica dados para outra região geográfica.

### GZRS — Geo Zone Redundant Storage
Combina replicação entre zonas e regiões.

---

# 📂 Serviços de Armazenamento do Azure

## Azure Blob Storage

Armazenamento otimizado para grandes volumes de dados não estruturados.

Exemplos:

- imagens
- vídeos
- backups
- arquivos

---

## Azure Disk Storage

Fornece discos gerenciados para máquinas virtuais e aplicações.

---

## Azure Queue Storage

Serviço de mensagens para comunicação entre componentes de aplicações distribuídas.

Cada mensagem pode ter até **64 KB**.

---

## Azure File Storage

Oferece compartilhamento de arquivos acessível via rede utilizando o protocolo **SMB**.

---

## Azure Table Storage

Banco de dados NoSQL baseado em **chave e atributo**, ideal para dados estruturados não relacionais.

---

# 🧊 Camadas de Acesso do Armazenamento

O armazenamento do Azure possui diferentes camadas de custo e acesso.

### Frequente (Hot)
Dados acessados com frequência.

### Esporádico (Cool)
Dados acessados ocasionalmente.

### Frio (Cold)
Dados raramente acessados.

### Arquivo Morto (Archive)
Armazenamento de longo prazo com menor custo.

---

# 📦 Azure Data Box

O **Azure Data Box** é um dispositivo físico utilizado para transferir grandes volumes de dados para o Azure.

Capacidade aproximada:

- até **80 TB de dados**

Principais usos:

- migração de grandes volumes de dados
- backup para recuperação de desastres
- transferência segura de dados para a nuvem

---

# 📚 Conclusão

A plataforma **Microsoft Azure** oferece uma ampla variedade de serviços que permitem construir aplicações modernas, escaláveis e seguras.

Compreender os conceitos de **arquitetura, computação, rede e armazenamento** é essencial para o desenvolvimento de soluções eficientes em ambientes de computação em nuvem.