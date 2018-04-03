# Objetivo

Criar uma aplicação Django, com API para consulta de produtos, e uma página usando a
camada de view e templates que consulte em uma lista de produtos e abra uma pagina do
detalhe do produto.

As informações que devem ser armazenadas de cada local são:
* Nome do Produto
* Valor
* Quantidade
* Imagem

# Requisitos

* Desenvolvimento em Django e Rest Framework.
* Testes
* Gerar logs das ações
* Instruções de como rodar o projeto
* Opcional (AngularJs, React Native) caso deseje fazer o front fora do Django usando API.

# Operações desejadas

* Lista de produto (tipo vitrine de e-commerce)
	- Listar produtos em uma página web. Pelo menos 3 produtos.
* Página com um produto selecionado (tipo página de produto de e-commerce)
	- Selecionar o produto na página de vitrine e abrir a página de produto.
* API de produtos
	- Criar API de produtos em Rest Framework.
	
# Passo a passo
##### Prepararando ambiente

* Crie um virtualenv com **Python 3.6**, preferencialmente utilizando virtualenvwrapper:

```
mkvirtualenv --python=/usr/bin/python3.6 desafio-dress
```
* Instalando dependências, migrando banco de dados e rodando servidores (node e Django):

```
sh ./prepare.sh
```

_Pronto! O sistema já deve estar disponível em localhost:8000_

##### Rodando o projeto após já ter executado a preparação do ambiente

* Mude para o diretório do projeto Django:
```
cd desafiodress
```
* Execute a diretiva **run** do Makefile:
```
make run
```