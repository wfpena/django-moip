# Integração Django Moip Assinaturas

Projeto de integração entre Django, AngularJS e o API do Moip para criação de assinaturas.

## Inicializando

### Token e Chave

No `settings.py` insira seu token e sua chave nas variáveis `MOIP_TOKEN` e `MOIP_KEY`, respectivamente.

Elas também podem ser setadas por variáveis de ambiente ou através de algum arquivo de configuração. Isso fica á escolha do desenvolvedor.

### Pré-requisitos

O projeto utiliza o Django Rest Framework e os scripts do AngularJS, Bootstrap, etc. O Django Rest Framework deve ser instalado. Os scripts do já estão incluídos dentro do app.
 

### Estrutura

Até o momento apenas dois modelos foram criados, um para armazenar os clientes `Client(models.Model)` e outro para as assinaturas `Subscriptions(models.Model)`. Eles estão sendo usados mais para ilustrar as possibilidades que o desenvolvedor tem para utilizar estas informações.

O Moip utiliza códigos (`codes`) para referenciar tanto os clientes (`customers`) cadastrados quando as assinaturas. Estes códigos são criados pelo próprio desenvolvedor ou dono da conta Moip.

Neste app, até o momento estes códigos são criados de acordo com a id na base de dados do item inserido, prefixado por `cliente` no caso de cliente e `assinatura` no caso de assinatura.

### Utilização do Programa

A utilização é bem básica, dentro do programa existem apenas duas abas, uma de Assinatura e outra de Cliente.

#### Criando Assinatura

Na  aba Assinatura podem ser criados assinaturas de duas formas, usando os clientes já cadastrados na sua conta Moip ou cadastrando um novo cliente e simultaneamente criando a assinatura para ele.

#### Cadastrando Clientes

Na aba Cliente podem ser cadastrados novos clientes. Estes são inseridos tanto na base de dados quanto na sua conta Moip.

### TODO
