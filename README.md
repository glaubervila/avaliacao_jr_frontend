# Avaliação para Dev Junior 

## Objetivo:
Criar uma aplicação Web com javascript que permita listar, criar, excluir e atualizar uma lista de Catalogos astronomicos e seus respectivos objetos.

## Objetivos Opcional:
A aplicação deve ter uma interface de detalhe, que permita selecionar um catalogo e ter acesso aos objetos associados a ele. 

Deve ser possivel fazer uma busca pelo nome do Catalogo. 

Deve ser possivel paginar a lista de catalogo.

Na interface de detalhe ao lado da lista de objetos, deve ser utilizado o component Aladin, que permite exibir uma imagem do Céu. ao clicar em um objeto deve-se posicionar o Aladin nas coordendas do objeto utilizando a função ```aladin.gotoRaDec()```. essa função espera os atributos ra, dec da api catalog_objects. 
Pagina oficial Aladin: http://aladin.u-strasbg.fr/AladinLite/ 
Docs: http://aladin.u-strasbg.fr/AladinLite/doc/API/
Exemples: http://aladin.u-strasbg.fr/AladinLite/doc/API/examples/


Descrever o git. 



1 - Fazer o clone do repositório https://github.com/linea-it/avaliacao_jr_backend e seguir os passos descritos no Readme para iniciar o backend. 

2 - Criar um novo repositório para o Frontend. 


senha de usuario: 123mudar

Comando para fazer o build do container
```
docker build -t backend_avaliacao .
```


Comando para executar o container
```
docker run -it -p 5000:5000 -v ${PWD}/app:/app -v ${PWD}/db:/db --rm backend_avaliacao
```

testar em 
http://localhost:5000/








## APIs:
### Catalog
URL: http://localhost:5000/api/catalog
metodos: ['GET', 'POST', 'DELETE', 'PUT', 'PATCH']

### Catalog Objects
URL: http://localhost:5000/api/catalog_objects
metodos: ['GET']

Exemplo de retorno: 
```
{
	"objects": [{
			"catalog_id": 1,
			"dec": 41.2454558,
			"description": "The Andromeda Galaxy (/\u00e6n\u02c8dr\u0252m\u026ad\u0259/), also known as Messier 31, M31, or NGC 224, is a spiral galaxy approximately 780 kiloparsecs (2.5 million light-years) from Earth, and the nearest major galaxy to the Milky Way",
			"id": 1,
			"name": "Andromeda Galaxy",
			"ra": 10.6706957,
			"wikipedia": "https://en.wikipedia.org/wiki/Andromeda_Galaxy",
            "catalog": {
				"id": 1,
				"name": "Galaxies"
			},
		}],
    "page": 1,
	"total_pages": 1,
    "num_results": 6
}

```




Links uteis sobre a API
HTTP methods: https://flask-restless.readthedocs.io/en/stable/customizing.html#http-methods

Fetching: https://flask-restless.readthedocs.io/en/latest/fetching.html

Format of Requests and Responses: https://flask-restless.readthedocs.io/en/stable/requestformat.html#requestformat

Making Search Queries: https://flask-restless.readthedocs.io/en/stable/searchformat.html





