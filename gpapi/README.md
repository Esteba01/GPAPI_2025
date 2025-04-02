# Proyecto GPAPI

Este proyecto utiliza Python 3.7. A continuación, se detallan los pasos para configurar y ejecutar el proyecto.

## Pasos para arrancar el proyecto

1. **Crear un entorno virtual de Python 3.7**  
    Ejecuta el siguiente comando en la terminal para crear un entorno virtual:
    ```bash
    python3.7 -m venv venv
    ```
    - En Windows (el que me funcionó)
      ```bash
      py -3.7 -m venv venv
      ```


2. **Activar el entorno virtual**  
    - En Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - En macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3. **Instalar dependencias**  
    Asegúrate de instalar las dependencias necesarias ejecutando:
    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecutar el script principal**  
    Una vez configurado el entorno, ejecuta el siguiente comando para iniciar el proyecto:
    ```bash
    python run_gpapi.py
    ```

## Notas adicionales
- Asegúrate de tener Python 3.7 instalado en tu sistema.
- Si no tienes un archivo `requirements.txt`, consulta la documentación del proyecto para conocer las dependencias necesarias.
## Crear contraseñas de aplicaciones de Google

5. **Crear una contraseña de aplicación de Google**  
    Si necesitas acceso a servicios de Google, crea una contraseña de aplicación siguiendo estos pasos:  
    - Accede al siguiente enlace: [Google App Passwords](https://myaccount.google.com/u/0/apppasswords?rapt=AEjHL4M3ovyeWlkUURdrF3OEvLbTCho24puGH0IcKXKD1TZlIyrqiovPbgwDJZ81eYGmrO3NFXihcuG4z_nxsUTzqDMt2-UR1LG8Pn7UXRWLlwus0L4Rt0Y&pageId=none).  
    - Inicia sesión con tu cuenta de Google.  
    - Sigue las instrucciones para generar una contraseña de aplicación.  
    - Guarda la contraseña generada en un lugar seguro, ya que será necesaria para la configuración del proyecto.