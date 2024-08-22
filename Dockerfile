# Imagen base de Python
FROM python:3.12.5-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requirements.txt al contenedor
COPY requirements.txt .

# Crear y activar el entorno virtual, luego instalar las dependencias
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt

# Copiar el resto del código de la aplicación al contenedor
COPY . .

# Exponer el puerto que Django usa por defecto
EXPOSE 8000

# Comando para ejecutar el servidor de Django
CMD ["/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]