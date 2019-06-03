

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