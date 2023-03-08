# Autencticação Básica em API Django Rest Framework
## Um projeto que demonstra como fazer uma autenticação básica num projeto desenvolvido com  Django Rest Framework


Esse projeto tem objetivo de aplicar o recurso Basic Athentication do Django Rest Framework, para proteger acessoss de uma API.  Os recursos dessa aplicação são baseados numa operação de fluxo de caixa simples, onde tem-se operação de Saque e Depósito além de  consultar o saldo do caixa. Nesse sentido vários usuários podem fazer o cadastro e controlar seu caixa, porém esses só poderão ter acesso  exclusivamente ao caixa vinculado à sua conta de usuário, que é definido no momento do cadastro do mesmo.


## Building

Esse projeto foi desenvolvido utilizando a versão 3.2.6 do interpretador Python. Todas as dependências
estão listadas no arquivo *requiments.txt*

### Como rodar ?

* realize o clone do repositório - `git clone https://github.com/MaercioMamedes/BasicAuthAPI.git`
* [crie um ambiente virtual dentro do diretório do projeto e instale todas as dependências](https://www.alura.com.br/artigos/ambientes-virtuais-em-python)
* rode o comando `python manage.py runserver`

### End points

|         URI          |    MÉTODO    |                       RECURSO                        |
|:--------------------:|:------------:|:----------------------------------------------------:|
|       /usuario       |     GET      |                 lista todos usuários                 |
|       /usuario       |     POST     |                  Cria novo usuário                   |
| /usuario/{ user_id } |     GET      |                   retorna usuário                    |
| /usuario/{ user_id } | PUT ou PATCH |                   atualiza usuário                   |
| /usuario/{ user_id } |    DELETE    |                   atualiza usuário                   |
|        /caixa        |     GET      |            acessa saldo do usuário logado            |
|        /caixa        |     POST     | realiza saque ou depósito do caixa do usuário logado |

### Parâmetros para efetuar operações

#### SAQUE: 
`{
    "operation_field": "saque",
    "value_operation": { valor_saque }
}`

#### DEPOSOTP: 
`{
    "operation_field": "deposito",
    "value_operation": { valor_deposito }
}`