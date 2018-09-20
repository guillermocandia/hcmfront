## Instrucciones para crear entorno de desarrollo

1.  **Instalación de aplicación y requisitos.**
    *   Clonar repositorio.

    ```
    $ git clone git@github.com:guillermocandia/hcmfront.git
    ```

    *   Para el resto de de las instrucciones el directorio de trabajo será el del proyecto.

    ```
    $ cd hcmfront
    ```

    *   Creación de entorno virtual.

    ```
    $ virtualenv --python=/usr/bin/python2.7 .venv
    $ source .venv/bin/activate
    ```

    *   Instalación de dependencias.

    ```
    (.venv)$ pip install -r requirements.txt
    ```

    *   Aplicar migraciones.

    ```
    (.venv)$ ./manage.py migrate
    ```

    *   Crear administrador.

    ```
    (.venv)$ ./manage.py createsuperuser
    ```

    *   Lanzar aplicación.

    ```
    (.venv)$ ./manage.py runserver
    ```

    *   Abrir la url localhost:8000 en navegador

2.  **Linter.**

    *   flake8 esta instalado en el entorno virtual

    ```
    (.venv)$ flake8 -v
    ```
