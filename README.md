# Avaliação para Dev Junior 

## Objetivo:
Criar uma aplicação Web com javascript que permita listar, criar, excluir e atualizar uma lista de Catalogos astronomicos e seus respectivos objetos.

A funcionalidade Create pode resumida em um botão que ao ser clicado inclua um novo catalogo, não é necessário a criação de formulário. A mesma coisa para o Update um botão que ao ser clicado altere o nome de um determinado catalogo.


## Objetivos Opcionais:
A aplicação deve ter uma interface de detalhe, que permita selecionar um catalogo e ter acesso aos objetos associados a ele. 

Na interface de detalhe ao lado da lista de objetos, deve ser utilizado o component Aladin, que permite exibir uma imagem do Céu. ao clicar em um objeto deve-se posicionar o Aladin nas coordendas do objeto utilizando a função ```aladin.gotoRaDec()```. essa função espera os atributos ra, dec da api catalog_objects. 

Deve ser possivel fazer uma busca pelo nome do Catalogo. 

Deve ser possivel paginar a lista de catalogo.


## Sobre os Dados
Neste exemplo estamos usando Catalogo e Objetos. um catalogo representa uma lista de objetos astronomicos galaxias, estrelas, nebulosas etc. Um catalogo tem um dono (owner) e data de criação. 

Todo Objeto está relacionado a um catalogo, e tem informaçoes como nome do objeto, coordenada, descrição e uma link que aponta para a Wikipedia.
a coordenada é formada pelos atributos **RA** e **Dec**. 

Uma analogia de Catalogo e Objetos pode ser a relação entre Categorias e produtos por exemplo. 

**TODO** Incluir imagem do modelo. 

**TODO** Descrever a etapa do git. 

# Ambiente
A maquina está configurada com docker, npm, yarn, git, vscode, Google Chrome e Firefox. o backend está instalado no home do usuario no diretório ```/home/avaliacao_jr_backend``` dentro deste diretório tem um script start.sh que inicia o Backend. o terminal onde o ambiente está rodando deve ficar aberto o tempo todo. caso precise iniciar o backend novamente basta executar o script start, para desligar o backend usar as teclas CRTL + C no terminal que está executando. 

Ao ligar o backend a API vai estar disponivel na url http://localhost:5000

O Banco de dados está no diretório ``` /home/avaliacao_jr_backend/db```, neste exemplo está sendo usado um banco SQLite que é preenchido com as informações ao ser iniciado. caso precise resetar o banco. basta remover este arquivo e iniciar o backend novamente. 


# APIs:
## Catalog
**URL**: http://localhost:5000/api/catalog

**Metodos**: ```['GET', 'POST', 'DELETE', 'PUT', 'PATCH']```

**Descrição**: Esta API retorna todos os catalogos.

**Exemplo de retorno**: 

```json
{
  "objects": [
    {
      "id": 1, 
      "name": "Galaxies", 
      "owner": "Glauber Costa",
      "date": "2019-06-04T14:49:06.597976", 
    }, 
    ...
  ], 
  "page": 1, 
  "total_pages": 1,
  "num_results": 2 
}

```

## Catalog Objects
**URL**: http://localhost:5000/api/catalog_objects

**Metodos**: ['GET']

**Descrição**: Esta API retorna todos os objetos. Para recuperar apenas os objetos de um catalogo a URL deve ter este formato ```http://localhost:5000/api/catalog/<catalog_id>/catalog_objects```


**Exemplo de retorno**: 
```json
{
  "objects": [{
    "catalog_id": 1,
    "id": 1,
    "ra": 10.6706957,
    "dec": 41.2454558,
    "name": "Andromeda Galaxy",
    "description": "The Andromeda Galaxy, also known as Messier 31, M31, or NGC 224, is a spiral galaxy approximately 780 kiloparsecs (2.5 million light-years) from Earth, and the nearest major galaxy to the Milky Way",		
    "wikipedia": "https://en.wikipedia.org/wiki/Andromeda_Galaxy",
    "catalog": {
      "id": 1,
      "name": "Galaxies"
    },
    ...
  }],
  "page": 1,
  "total_pages": 1,
  "num_results": 6
}

```
Obs: o atributo ```catalog``` pode ser ignorado, ele representa um objeto da API catalog.


## Referências

Aladin: http://aladin.u-strasbg.fr/AladinLite/ 

Aladin Docs: http://aladin.u-strasbg.fr/AladinLite/doc/API/

Aladin Exemples: http://aladin.u-strasbg.fr/AladinLite/doc/API/examples/


Flask Restless: https://flask-restless.readthedocs.io/en/stable/

HTTP methods: https://flask-restless.readthedocs.io/en/stable/customizing.html#http-methods

Fetching: https://flask-restless.readthedocs.io/en/latest/fetching.html

Format of Requests and Responses: https://flask-restless.readthedocs.io/en/stable/requestformat.html#requestformat

Making Search Queries: https://flask-restless.readthedocs.io/en/stable/searchformat.html







