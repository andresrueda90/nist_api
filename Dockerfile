# Usa una imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expone el puerto en el que correrá Django
EXPOSE 8000

# Ejecuta las migraciones y levanta el servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]