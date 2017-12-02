# Integração Django Moip Assinaturas

Projeto de integração entre Django, AngularJS e o API do Moip para criação de assinaturas.

## Inicializando

### Token e Chave

No `settings.py` insira seu token e sua chave nas variáveis `MOIP_TOKEN` e `MOIP_KEY`, respectivamente.

Elas também podem ser setadas por variáveis de ambiente ou através de algum arquivo de configuração. Isso fica á escolha do desenvolvedor.

### Pré-requisitos

O projeto utiliza o Django Rest Framework e os scripts do AngularJS. O Django Rest Framework deve ser instalado. Os scripts do Angular já estão incluídos.
 

### Estrutura

Até o momento apenas dois modelos foram criados, um para armazenar os clientes `Client(models.Model)` e outro para as assinaturas `Subscriptions(models.Model)`. Eles estão sendo usados mais para ilustrar as possibilidades que o desenvolvedor tem para utilizar estas informações.

### Utilização do Programa


### TODO
