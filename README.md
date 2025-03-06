
# NITS CRM

Permite el registro de las vulverabilidades a traves de Api , utilizando la data de https://nvd.nist.gov/developers/vulnerabilities


## Herramientas

- djangorestframework

## Ejecución 

```
    docker build -t django_pruebas .
    docker run -p 8000:8000 django_pruebas
```


##  Endpoints

Documentación con ejemplos en Postman
https://documenter.getpostman.com/view/33336481/2sAYdmm896#79bea400-e60c-4134-b2cc-d09931786c94

- Permite cargar las vulnerabilidades en la base de datos con su gravedad antes de consumir los demas endpoints ejecutar este para cargar los datos 
```
curl --location --request POST 'http://127.0.0.1:8000/api/load-nist-vulnerabilities/'
```


- Endpoint GET que devuelve el listado total de las vulnerabilidades.
```
curl --location 'http://127.0.0.1:8000/api/vulnerabilities/'
```

- Endpoint POST que reciba la/s vuln/s fixeada/s.
```
curl --location 'http://127.0.0.1:8000/api/vulnerability-status/' \
--header 'Content-Type: application/json' \
--data '{
    "cve_id": "CVE-1999-0095"
}'
```

- Endpoint GET que devuelva el listado de vulnerabilidades exceptuando las fixeadas (ingresadas en el endpoint del punto 2).
```
curl --location 'http://127.0.0.1:8000/api/vulnerability-unfixed/'
```

- Endpoint GET que permita obtener información sumarizada de vulnerabilidades por severidad

```
curl --location 'http://127.0.0.1:8000/api/vulnerabilities/summary/'
```






