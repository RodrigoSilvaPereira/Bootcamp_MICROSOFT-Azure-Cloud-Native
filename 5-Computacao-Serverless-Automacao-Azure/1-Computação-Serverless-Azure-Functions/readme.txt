Módulo: Computação Serverless com Azure Functions e LogicApps

• O Azure Functions é um serviço de solução sem 
servidor
• A infraestrutura de nuvem fornece todos os recursos 
atualizados necessários para manter seus aplicativos 
em execução
• Dimensionamento do Azure Functions de acordo com a 
demanda
Descobrir o Azure Functions (1 de 3)
Visão geral
• Considere o Functions para 
tarefas como processamento de 
imagens ou pedidos, 
manutenção de arquivos ou 
tarefas que você deseja 
executar de maneira agendada.
• O Azure Functions dá suporte 
a gatilhos, que iniciam a 
execução do seu código, e 
associações, 
que simplificam a codificação 
de dados de entrada e de saída.
Hubs de Notificação
Grade de Eventos
Armazenamento
Hubs de 
Eventos
Cosmos DB
Twilio
Azure 
Funções
Queue
Blob
Tabela
Barramento de Serviço
Tópicos
Filas
Descobrir o Azure Functions (2 de 3)
Comparar o Azure Functions e os Aplicativos Lógicos do Azure
Funções Aplicativos Lógicos
Desenvolvimento Primeiro o código (obrigatória) Primeiro o designer (declarativa)
Conectividade
Cerca de doze tipos internos de associação 
+ possibilidade de escrita de código para 
associações personalizadas
Grande conjunto de conectores + Enterprise Integration 
Pack para cenários de B2B + possibilidade de criar 
conectores personalizados
Ações Cada atividade é uma função do Azure. 
Escrever código para funções de atividade Grande conjunto de ações predefinidas
Monitoramento Azure Application Insights Portal do Azure, logs do Azure Monitor
Gerenciamento API REST, Visual Studio Portal do Azure, API REST, PowerShell, Visual Studio
Contexto de 
execução
Podem ser executadas no local ou na 
nuvem Oferece suporte a cenários de run-anywhere
Descobrir o Azure Functions (3 de 3)
Comparar Functions e WebJobs
Funções WebJobs com o SDK do WebJobs
Modelo de aplicativo sem servidor com 
dimensionamento automático Sim No
Desenvolver e testar no navegador Sim No
Preço de pagamento por uso Sim No
Integração com os Aplicativos Lógicos Sim No
Eventos de gatilho
Temporizador
Filas e blobs do Armazenamento do Azure
Filas e tópicos do Barramento de Serviço 
do Azure
Azure Cosmos DB
Hubs de Eventos do Azure
HTTP/WebHook (GitHub Slack)
Grade de Eventos do Azure
Temporizador
Filas e blobs do Armazenamento do Azure
Filas e tópicos do Barramento de Serviço 
do Azure
Azure Cosmos DB
Hubs de Eventos do Azure
Sistema de arquivos
Comparar as opções de hospedagem do Azure Functions (1 de 3)
Três planos de hospedagem 
básicos:
• Plano de Consumo
• Plano Premium
• Plano dedicado (Serviço de Aplicativo)
Opções adicionais para maior 
controle e isolamento:
• Ambiente do Serviço de Aplicativo
Os planos de hospedagem ditam:
• Como o aplicativo de funções 
é dimensionado.
• Os recursos disponíveis para cada instância 
do aplicativo de funções.
• Suporte para funcionalidades avançadas, 
como conectividade à Rede Virtual do Azure.
• Kubernetes
Comparar as opções de hospedagem do Azure Functions (2 de 3)
Plano de Consumo
• O plano de hospedagem 
padrão. 
• Ele dimensiona 
automaticamente e você paga 
apenas quando as funções 
estiverem em execução. 
• As instâncias do host do 
Functions são adicionadas 
e removidas de maneira 
dinâmica com base no número 
de eventos de entrada.
Plano Premium
• Usa trabalhadores pré
aquecidos para dimensionar 
automaticamente com base 
na demanda.
• É executado em instâncias 
mais poderosas e se conecta a 
redes virtuais.
Plano dedicado
• Execute suas funções em 
um plano do Serviço de 
Aplicativo com taxas regulares 
do Plano do Serviço de 
Aplicativo.
• Melhor para cenários de 
execução longa em que 
o Durable Functions não 
pode ser usado.
Comparar as opções de hospedagem do Azure Functions (3 de 3)
Duração do tempo limite do 
aplicativo de funções
• A propriedade functionTimeout no 
arquivo de projeto host.json especifica 
a duração do tempo limite.
• O plano de consumotem um tempo 
limite padrão de 5 minutos e um tempo 
limite máximo de 10 minutos.
• Os planos Premium e Dedicado têm um 
tempo limite padrão de 30 minutos 
e nenhuma duração máxima.
Requisitos da conta de armazenamento
• Em qualquer plano, o aplicativo de funções 
exige uma conta geral do Armazenamento 
do Azure.
• O Azure Functions usa o Armazenamento 
do Azure para operações como gerenciamento 
de gatilhos e registro 
em log de execuções de função.
Dimensionar o Azure Functions (1 de 3)
• A unidade de escala para o Azure Functions é o aplicativo de funções.
• Um controlador de escala monitora a taxa de eventos para determinar se deve 
aumentar ou reduzir. 
• O número de instâncias pode ser “reduzido” a zero quando nenhuma função está 
em execução em um aplicativo de funções.
• A próxima solicitação tem a latência (inicialização a frio) de escala de zero para 
um
Dimensionar o Azure Functions (2 de 3)
Comportamentos de escala
O dimensionamento pode variar em uma série de fatores e ser diferente com 
base no gatilho e na linguagem selecionada. 
• Máximo de instâncias: um único aplicativo de funções só é escalado 
horizontalmente para no máximo 200 instâncias. Uma única instância pode 
processar mais de uma mensagem ou solicitação por vez, portanto, não há 
um limite definido de número de execuções simultâneas.
• Nova taxa de instância: Para gatilhos HTTP, novas instâncias são alocadas, 
no máximo, uma vez por segundo. Para gatilhos não HTTP, novas instâncias 
são alocadas, no máximo, uma vez a cada 30 segundos.
Dimensionar o Azure Functions (3 de 3)
Limitar escala horizontal
• Você pode restringir o número máximo 
de instâncias que um aplicativo usou para 
escalar horizontalmente.
• Comum quando um componente 
downstream, como um banco de dados, 
tem taxa de transferência limitada. 
• Defina o valor functionAppScaleLimit
como zero para irrestrito ou para um 
valor entre um e o máximo do aplicativo
Dimensionamento em um plano 
dedicado
• Usando um Plano do Serviço de Aplicativo, 
você pode manualmente escalar 
horizontalmente, adicionando mais 
instâncias de VM.
• Você também pode habilitar o 
dimensionamento automático.
Resumo e verificação de conhecimentos
Neste módulo, você aprendeu a:
• Explicar as diferenças funcionais 
entre o Azure Functions, os 
Aplicativos Lógicos do Azure e o 
WebJobs
• Descrever as opções do plano de 
hospedagem do Azure Functions
• Descrever como o Azure Functions 
escala para atender às necessidades 
dos negócios
1
Qual plano de hospedagem do Azure Functions 
é melhor quando a escala preditiva e os custos 
são necessários?
2 Qual fluxo de trabalho sem servidor você 
escolheria se a solução exigisse um modelo 
de desenvolvimento designer-first?
Desenvolver o Azure 
Functions
[21]
Introdução
Toda função tem duas partes importantes:
• Ocódigo, que pode ser escrito em uma variedade de linguagens.
• Algumas configurações, o arquivo function.json.
• Dependendo da linguagem escolhida, o arquivo function.json pode ser 
gerado automaticamente
Explorar o desenvolvimento do Azure Functions (1 de 3)
• O arquivo function.json define o gatilho, 
as associações e outras definições de 
configuração da função.
• Cada função tem apenas um gatilho. 
• O runtime usa o arquivo de configuração 
para determinar os eventos a serem 
monitorados, bem como para passar e 
retornar dados de uma execução da 
função. 
• A propriedade associações é onde você 
configura gatilhos e associações. 
{
}
"disabled":false,
"bindings":[
// ... bindings here
{
"type": "bindingType",
"direction": "in",
"name": "myParamName",
// ... more depending on binding
}
]
Criar gatilhos e associações (1 de 7)
Visão geral
• Os gatilhos fazem com que uma função seja executada. Um gatilho define 
como uma função é invocada e uma função deve ter exatamente um gatilho.
• A associação a uma função é uma forma de conectar declarativamente 
outro recurso à função
• As associações podem ser conectadas como associações de entrada, 
associações de saída ou ambas. 
• Você pode misturar e combinar diferentes associações para atender às 
suas necessidades.
• Gatilhos e associações permitem evitar codificar o acesso a outros serviços.
Criar gatilhos e associações (2 de 7)
Definições de associação e gatilho
• Os gatilhos e as associações são definidos de 
forma diferente, dependendo da linguagem 
de desenvolvimento.
• C# class library - identificação de métodos 
e parâmetros com atributos C#
• Java -identificação de métodos e parâmetros 
com anotações Java
• JavaScript/PowerShell/Python/TypeScript 
atualização do esquema function.json
{
}
"dataType": "binary",
"type": "httpTrigger",
"name": "req",
"direction": "in"
Criar gatilhos e associações (3 de 7)
Direção de associação
• Todos os gatilhos e associações têm uma propriedade de direção no 
arquivo function.json:
• Para gatilhos, a direção é sempre de entrada, in
• Associações de entrada e saída usam in e out, respectivamente
• Algumas associações tem suporte para uma direção especial, inout. Se você 
usar inout, apenas o Editor avançado está disponível na guia Integrar
no portal.
• Quando você usa atributos em uma biblioteca de classes para configurar 
associações e gatilhos, a direção é fornecida em um construtor de atributo 
ou inferida do tipo de parâmetro.
Criar gatilhos e associações (4 de 7)
Exemplo de gatilho e associação do Azure Functions
Cenário: suponha que você quer gravar uma 
nova linha no Armazenamento de Tabelas do 
Azure sempre que uma nova mensagem 
aparece no Armazenamento de Filas do Azure.
Esse cenário pode ser implementado usando 
um gatilho do Armazenamento de Filas do 
Azure e uma associação de saída do 
Armazenamento de Tabelas do Azure.
"bindings": [
{
"type": "queueTrigger",
"direction": "in",
"name": "order",
"queueName": "myqueue-items",
"connection": "STORAGE_ACCT_SETTING"
},
{
"type": "table",
"direction": "out",
"name": "$return",
"tableName": "outTable",
"connection": "STORAGE_ACCT_SETTING"
}
Criar gatilhos e associações (5 de 7)
Exemplo de script C#
Código de script C# que funciona 
com o gatilho anterior e a associação 
especificada.
...
publicstaticPersonRun(JObjectorder, ILoggerlog)
{
returnnew Person() { 
PartitionKey = "Orders", 
RowKey= Guid.NewGuid().ToString(), 
Name= order["Name"].ToString(),
MobileNumber = order["MobileNumber"].ToString() 
}; 
}
publicclassPerson
{
publicstringPartitionKey { get; set; }
publicstringRowKey{ get; set; }
publicstringName{ get; set; }
publicstringMobileNumber { get; set; }
}
Criar gatilhos e associações (6 de 7)
Exemplo de JavaScript
Código JavaScript que funciona com o gatilho anterior e a associação especificada.
module.exports= asyncfunction(context, order) {
order.PartitionKey= "Orders";
order.RowKey= generateRandomId(); 
context.bindings.order= order;
};
functiongenerateRandomId() {
returnMath.random().toString(36).substring(2, 15) +
Math.random().toString(36).substring(2, 15);
}
Criar gatilhos e associações (7 de 7)
Exemplo de biblioteca de classes
publicstaticclassQueueTriggerTableOutput
{
[FunctionName("QueueTriggerTableOutput")]
[return: Table("outTable", Connection= "CONNECTION")]
publicstaticPersonRun(
[QueueTrigger("myqueue-items", Connection= "CONNECTION")]JObjectorder,
ILogger log)
{
returnnew Person() {
PartitionKey= "Orders",
RowKey= Guid.NewGuid().ToString(),
Name= order["Name"].ToString(),
MobileNumber= order["MobileNumber"].ToString() };
}
...
Conectar funções a serviços do Azure (1 de 2)
Visão geral
• Seu projeto de função faz referência 
a informações de conexão por nome 
a partir do provedor de configuração.
• Ele não aceita diretamente os detalhes 
da conexão, permitindo que eles sejam 
alterados nos ambientes.
• O provedor de configuração padrão 
usa variáveis de ambiente. Elas podem 
ser definidas pelas Configurações de 
Aplicativos quando executadas no 
serviço do Azure Functions ou pelo 
arquivo de configurações local se o 
desenvolvimento for feito localmente.
Valores de conexão
• Quando o nome da conexão é resolvido 
para um único valor exato, o runtime identifica o 
valor como uma cadeia de conexão, 
que normalmente inclui um segredo. 
• Os detalhes de uma cadeia de conexão são 
definidos pelo serviço ao qual você deseja 
se conectar.
• Um nome de conexão também pode se referir 
a uma coleção de vários itens de configuração. 
• Para que variáveis de ambiente sejam 
tratadas como uma coleção, use um prefixo 
compartilhado que termina com sublinhados 
duplos, "__".
Conectar funções a serviços do Azure (2 de 2)
Configurar uma conexão baseada 
em identidade
• Algumas conexões no Azure Functions 
são configuradas para usar uma 
identidade em vez de um segredo. O 
suporte depende da extensão que usa a 
conexão.
• Em alguns casos, uma cadeia de conexão 
ainda pode ser necessária no Functions, 
embora o serviço ao qual você está se 
conectando ofereça suporte a conexões 
baseadas em identidade.
Conceder permissão para 
a identidade
• Qualquer identidade que esteja sendo 
usada deve ter permissões para executar 
as ações pretendidas.
• Isso normalmente é feito atribuindo uma 
função no RBAC do Azure ou especificando 
a identidade em uma política de acesso, 
dependendo do serviço ao qual você está 
se conectando.
LogicApps
[35]
Azure logic apps
Solução de fluxo de trabalho de automação:
• Designer sem código para criação rápida de soluções de integração
• Modelos pré-criados para simplificar os primeiros passos
• Suporte pronto para uso para software como serviço (SaaS) popular e 
integrações locais
• APIs do BizTalk disponíveis para soluções de integração avançadas
Definição de fluxo de trabalho baseada em JSON:
• Pode ser implantado usando modelos do Azure Resource Manager
Components
• Workflow
• O processo de negócios descrito como uma série de etapas
• Triggers
• A etapa que invoca uma nova instância de fluxo de trabalho
• Actions
• Uma etapa individual em um fluxo de trabalho, normalmente um 
conector ou aplicativo de API personalizado
• Connectors
• Um caso especial de um aplicativo de API pré-criado e pronto para 
integração com um serviço ou fonte de dados específico.
Workflow components
Workflow
Action Action Connector
Action Connector Action
Trigger
Conectividadehíbrida
• Conecte aplicativos locais, híbridos e em nuvem
• Execute cenários de integração complexos e de missão crítica
On-premises data gateway
Logic app Cognitive 
Services
Service Bus
Machine 
Learning 
API 
Management BB2B and 
electronic data 
interchange
BizTalk
Server
Logic Apps Desiner
Casos de Uso
[41]
Caso de Uso Serviço 
Recomendado Benefícios Observações/Desafios
Processamento de Eventos em 
Tempo Real Azure Functions Escalabilidade, baixo custo, 
execução rápida
Monitoramento e logging podem 
precisar de configurações 
adicionais.
Integração com APIs e Serviços 
Externos Azure Functions Flexibilidade na linguagem, 
integração com diversas APIs
Gerenciamento de dependências 
e segurança são essenciais.
Processamento Assíncrono via 
Filas e Mensageria Azure Functions
Capacidade de lidar com cargas 
variáveis e processamento 
escalável
Dependência do gerenciamento 
das filas e latência variável.
Orquestração de Processos de 
Negócio Logic Apps
Facilidade de configuração 
visual, integração com vários 
conectores padrão
Pode ter limitações em cenários 
de alta complexidade lógica.
Caso de Uso Serviço 
Recomendado Benefícios Observações/Desafios
Integração de Sistemas Legados Logic Apps Conectores prontos e integração 
nativa com serviços híbridos
Dependência de gateways e 
configurações de rede.
Automatização de Fluxos de Trabalho 
Internos Logic Apps
Redução de erros manuais, 
integração simples com serviços 
Office 365 e outros
Pode demandar customizações para 
regras de negócio específicas.
Transformação e Manipulação de 
Dados Azure Functions
Flexibilidade para aplicar lógicas 
complexas, integração com pipelines 
de dados
Exige cuidados com performance para 
grandes volumes de dados.
Notificações e Alertas AutomatizadosLogic Apps
Configuração rápida, integração com 
serviços de comunicação (SMS, email, 
Teams, etc.)
Dependência de conectores e limites de 
chamadas.
