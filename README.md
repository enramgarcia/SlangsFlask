# SlangsFlask


Script de python para conectarse a una BD de Redis usando redis-py y flask para aceptar requests HTTP, en el script existen las siguientes variables para poder crear el connection string.

- HOST = "localhost"
- PORT = 6379

## Endpoints

|Endpoint|Metodo|Descripcion|
| ------ | ------ | ------ |
|/|GET|Index principal que muestra un JSON de todas las palabras con sus descripciones|
|/palabras/<word>|GET|Busca una palabra en el BD de redis, retorna 404 si no se encuentra y en caso tal se encuentre se retorna un JSON de la palabra con descripción.|
|/palabras|POST|Crea un registro en la BD retorna HTTP 500 si ya existe.|
|/palabras/<word>|PUT|Edita un registro, HTTP Put, retorna HTTP 404 si la palabra no se encuentra.|
|/palabras/<word>|DELETE|Elimina un registro, retorna HTTP 404 si la palabra no se encuentra.|
