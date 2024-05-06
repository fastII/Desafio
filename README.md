# Desafio NTConsult

Abaixo estão as especicações do Desafio NTconsult

# Considerações Gerais

Você deve fazer um desenho de arquitetura de um cloud provider da sua preferencia que atenda/resolva o problema proposto.

Na avaliação você tera que defender a sua arquitetura respondendo perguntas direcionado ao que foi apresentado como solução.

Considere como um projeto novo, pense em uma construção visando desde ao fluxo de desenvolvimento, publicação do artefato e deploy da aplicação.

Implemente diferentes ambientes de deploy (desenvolvimento, teste, produção) com configurações apropriadas.


# O Problema

O desafio que você deve resolver é a implantação da infraestrutura (obrigatório) e da aplicação de Comentários em versão API (opcional) usando ferramentas open source da sua preferência.

Você precisa criar o ambiente de execução desta API com o maior número de passos automatizados possível, inclusive a esteira de deploy.

A aplicação será uma API REST cuja a função está disponível neste arquivo. Através dela os internautas enviarão comentários em texto de uma máteria e acompanharão o que outras pessoas estão falando sobre o assunto em destaque. O funcionamento básico da API consiste em uma rota para inserção dos comentários e uma rota para listagem.

Os comandos de interação com a API são os seguintes:

* Criando e listando comentários por matéria

```
# matéria 1
curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"alice@example.com","comment":"first post!","content_id":1}'
curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"alice@example.com","comment":"ok, now I am gonna say something more useful","content_id":1}'
curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"bob@example.com","comment":"I agree","content_id":1}'

# matéria 2
curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"bob@example.com","comment":"I guess this is a good thing","content_id":2}'
curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"charlie@example.com","comment":"Indeed, dear Bob, I believe so as well","content_id":2}'
curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"eve@example.com","comment":"Nah, you both are wrong","content_id":2}'

# listagem matéria 1
curl -sv host/api/comment/list/1

# listagem matéria 2
curl -sv host/api/comment/list/2
```


# O que será avaliado na sua solução?

* Automação da infra, provisionamento dos hosts/Containers (IaaS/PaaS) - Obrigatório

* Automação de setup e configuração dos hosts/Containers (IaaC/PaaS) - Obrigatório

* Pipeline de deploy automatizado - Desejável (Pode utilizar o seu repositório pessoal para registrar os commits e a construção da Pipeline)

* Monitoramento dos serviços e métricas da aplicação - Desejável

* Desenvolvimento da API será considerado um diferencial - Diferencial


# Passos Realizados

1) Automação da infra, provisionamento dos hosts/Containers (IaaS/PaaS) - Feito
  Procedimento Realizado via Terraform

2) Automação de setup e configuração dos hosts/Containers (IaaC/PaaS) - Feito
  Procedimento Realizado Terraform

3) Pipeline de deploy automatizado - Desejável (Pode utilizar o seu repositório pessoal para registrar os commits e a construção da Pipeline)
  Procedimento Realizado via GitHu

4) Monitoramento dos serviços e métricas da aplicação - Desejável
   Procedimento realizado via HelmChart

Segue abaixo detalhamento dos Passos

O referido Projeto tem como objetivo descrever e apresentar de forma eficaz todo o desenvolvimento de uma Gestão de Orquestração de Contairners no Provedor da AWS. Temos duas opções são elas:
Quando se trata de escolher entre EKS (Amazon Elastic Kubernetes Service) com Fargate e EC2 (Amazon Elastic Compute Cloud), existem algumas considerações importantes a ter em mente.

# EKS com Fargate:

O Fargate permite executar contêineres sem precisar gerenciar as instâncias do EC2 subjacentes. Com o Fargate, você simplesmente define seus recursos de CPU e memória para cada contêiner e o AWS cuida do dimensionamento e gerenciamento da infraestrutura subjacente.
É uma opção excelente para equipes que desejam simplificar a gestão e a escalabilidade de contêineres sem se preocupar com a infraestrutura subjacente.

# EC2:

EC2 oferece mais controle sobre a infraestrutura subjacente. Você pode escolher os tipos de instância EC2, configurar a rede e o armazenamento conforme necessário.
É uma opção mais flexível se você precisa de controle granular sobre a infraestrutura, tem requisitos específicos de hardware ou deseja aproveitar recursos como GPUs para cargas de trabalho específicas.
A escolha entre EKS com Fargate e EC2 depende das necessidades específicas do seu projeto. Se você valoriza a simplicidade e a automação, EKS com Fargate pode ser a escolha certa. Se você precisa de mais controle sobre a infraestrutura ou tem requisitos específicos de hardware, EC2 pode ser a melhor opção.

Para essa Arquitetura escolhemos o EKS Fargate, conforme dito acima, com ele não precisamos ter a gestão das máquinas EC2 ( Infraestrutura)

O Amazon Elastic Kubernetes Service (EKS) com AWS Fargate é uma combinação poderosa para orquestração de contêineres. Aqui estão algumas vantagens e desvantagens:

# Vantagens:

Facilidade de Uso: Com o EKS, você pode gerenciar seus clusters Kubernetes com mais facilidade, e o Fargate elimina a necessidade de gerenciar servidores subjacentes.

Elasticidade Automática: O AWS Fargate permite escalar automaticamente seus contêineres com base na demanda, garantindo alta disponibilidade sem a necessidade de provisionar ou gerenciar servidores.

Custo Efetivo: Com o Fargate, você paga apenas pelos recursos de computação consumidos pelos contêineres, o que pode resultar em economia significativa em comparação com a manutenção de instâncias EC2 tradicionais.

Isolamento de Recursos: Cada contêiner é executado em seu próprio ambiente isolado, garantindo segurança e isolamento de recursos.

# Desvantagens:

Maior Custo por Recurso: Embora o Fargate ofereça economia de custos em termos de gerenciamento de infraestrutura, o custo por recurso pode ser maior em comparação com a execução de contêineres em instâncias EC2, especialmente para cargas de trabalho de longa duração e consistentes.

Limitações de Configuração: Como o Fargate gerencia automaticamente a infraestrutura subjacente, pode haver algumas limitações em termos de personalização e configuração avançada, especialmente para casos de uso específicos.

Complexidade de Migração: Migrar cargas de trabalho existentes para o EKS com Fargate pode ser complexo, especialmente se você estiver vindo de uma infraestrutura diferente ou uma configuração personalizada.

Dependência da Nuvem: Ao optar pelo EKS com Fargate, você está vinculado à infraestrutura da AWS, o que pode limitar a portabilidade das cargas de trabalho para outras nuvens ou ambientes locais.

Considerando esses aspectos, o EKS com Fargate pode ser uma excelente escolha para muitos casos de uso, especialmente para equipes que buscam uma maneira fácil e eficiente de executar aplicativos em contêineres sem se preocupar com a infraestrutura subjacente.

# Segue abaixos estimativas de valores com as duas tecnologias, utilizei a família t3a.large e uma instância do fargate a maioria quem saiu mais em conta foi a do fargate, abaixo somente uma ilustração

![estimulate_eks_ec2jpg](https://github.com/fastII/desafio/assets/16465756/317fac72-4406-46ea-96a6-119a7219a264)
![estimulate_eks_fargate](https://github.com/fastII/desafio/assets/16465756/0cf3b0ba-91c2-44d5-9ade-8c968d727236)


# Segue desenho da Arquitetura proposta
![desafiot](https://github.com/fastII/desafio/assets/16465756/d5dc6337-c529-4d1e-8e6e-ea932e53166a)

Ressalvas criei 04 sub-redes, delas 02 são públicas e 02 privadas para o ELB. Marquei com tag para os ELB internos e públicos.
Nat Gateway
Rotas
Policy
EKS
Role e Profile Fargate 

# Obs.: Na criação do profile fargate pelo terraform foi encontrado um problema na execução dos pods do COREDNS no NS kube-system, nesse step criei uma função IAM onde determinava a execução dos Pods Core_DNS. Como solução de contorno excluir a que foi criada pelo terraform e criei outra pela ConsoleAWS, fazendo uma busca posteriormente vi que é possível adicionar um ADD-ON na estrutura terraform para termos este problema, entratanto não declarei este passo no Terraform devido tempo.

Segue abaixo link fonte
https://docs.aws.amazon.com/pt_br/eks/latest/userguide/managing-coredns.html
https://docs.aws.amazon.com/eks/latest/userguide/fargate-getting-started.html


## ESTRUTURA CI&CD ##
Para esse projeto escolhi o Github+Gitactions para receber fonte do projeto, estrutura pipeline e estrutura dos arquivos do Terraform. Não irei abordar a fundo conceitos de CI&CD
Mas a ideia foi:  
Criar uma estrutura com todos os steps para realizar o deployment no ambiente EKS Fargate, utilizei alguns recursos já disponível no marketplace do Github, como por exemplo o checkout e docker build.

# Foto meramente ilustrativa
![integracaocontinua](https://github.com/fastII/desafio/assets/16465756/addee989-a847-4c0d-8426-591f5cc2ed50)

Para o Workflow de GIT para Deploy, adotei uma abordagem que utilizo algum temp, no qual eu realizo os deployers nos ambientes sem aprovação para dev, stg e para produção através de aprovação no caso do GitActions ela será realizada através de um PullRequest que dispara pra a branch main ( Produção)
Branches criadas DEV, STG











