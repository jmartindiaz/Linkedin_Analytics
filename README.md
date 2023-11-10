# Linkedin Analytics

## Objetivos

The objetive of this project is to make a Marketing Analysis for an engineering company that designs, manufactures and commercializes lifting devices, focusing on the sent requests, contacts and accepted requests and, on the other hand, the messages sent to each of the prospects.

Este proyecto tendra por finalidad realizar un analisis de Marketing de una empresa que diseña, fabrica y comercializa dispositivos de izaje, enfocándose en las solicitudes de contacto enviadas, los contactos y solicitudes aceptas, y por otra parte los mensajes enviados a cada uno de los prospectos.

## Datasets

Los datasets son descargados de la cuenta de Linkedin personal y contienen los datos vigentes hasta la fecha 23/08/2023.

- `Connections.csv`: contiene todos los registros de solicitudes aceptadas por otras personas, podría ser considerada tambien como un registro de todos los contactos de la cuenta que se posee hasta la fecha. 
- `Invitations.csv`: figuran los registros de solicitudes enviadas y recibidas.
- `messages.csv`: contiene informacion sobre todos los mensajes enviados y recibidos.

## Librerías a utilizar

- **pandas**: para analisis y transformacion de datos.
- **numpy**: para analisis y transformacion de datos.
- **fastapi**: para la api a la que le haremos consultas
- **uvicorn**: para levantar un servidor en el que este alojada la api
- **pydantic**: para validacion de datos de la api. Nos permite instanciar la clase BaseModel en nuestro main.py , esta clase nos garantiza que los tipos de datos que se almacenen en los atributos de nuestra clase se correspondan con los tipos de datos que nosotros hemos definido previamente.
- **typing**: permite que los tipos de datos que definimos para estos atributos puedan ser opcionales.