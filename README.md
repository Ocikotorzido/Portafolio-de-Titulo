# Mechanic Car Services (M.C.S.)
[![Python](https://img.shields.io/badge/Python-3.7.7-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2.3-green.svg)](https://www.djangoproject.com/)
[![Oracle](https://img.shields.io/badge/Oracle-18c-red.svg)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/TailWind-2.1.4-yellow.svg)](https://www.tailwindcss.com/)

[![screenshot](./pantallazos/pantallazo_00.png)](https://github.com/Ocikotorzido/congenial-funicular/tree/master/pantallazos/)

## ¿Qué es esto?
Sistema de gestión y administración web del taller mecánico "ServiExpress".

## ¿Quién es el patrocinador?
- **Juan Pedro**, mecánico automotriz.

## ¿Qué necesito instalar?
- Python 3
- Dependencias de terceros `pip install -r requirements.txt`
  - **También es posible instalar las dependencias por separado.**
  - Django (`pip install django`)
  - cx_oracle (`pip install cx_oracle`)
  - Pandas (`pip install pandas`)
  - Xlwt (`pip install xlwt`)
  - OpenPyXL (`pip install openpyxl`)
  - Docx2PDF (`pip install docx2pdf`)
  - Python-Docx (`pip install python-docx`)
- Oracle 18c (cliente/servidor dependiendo de la ubicación de la base de datos).
- LibreOffice/MS-Office 365

## ¿Qué debo configurar?
### Usuario Súper-administrador
Se debiera crear un usuario administrador.

- `python manage.py createsuperuser`

### Archivo de configuración para envío de emails.
Crear un archivo de configuración (**settings.ini**) con la siguiente información:
```
[Settings]
EMAIL_HOST_USER = MI_CORREO_ELECTRONICO@gmail.com
EMAIL_HOST_PASSWORD = CONTRASEÑA_PARA_APLICACIÓN_CON_SEGURIDAD_DESHABILITADA
```

Se debe tener en cuenta:

- Este archivo debe llamarse **settings.ini** y debe estar al mismo nivel de **manage.py**.

- La constante **EMAIL_HOST_USER** debe tener un correo GMAIL.

- La constante **EMAIL_HOST_PASSWORD** debe tener una clave de aplicación con verificación en dos pasos y acceso a aplicaciones 'poco seguras'.

## ¿Cómo lo echo a andar?
Si todo se instaló correctamente, es tan simple como hacer click en **up**.

**Usuarios de Windows**
- **Doble click en** `up`.
- Saltará el navegador.
- Ya puedes ver el proyecto.
- Yera.

---

**Linux**

Por línea de comandos: 

- Escribir en la terminal `python3 manage.py runserver`
- Abrir el navegador en [localhost:8000](http://localhost:8000/) o [127.0.0.1:8000](http://127.0.0.1:8000/).

## ¿Qué lenguajes/bases de datos/control de versiones se utilizaron?
- **FrontEnd**: Html5, JavaScript, CSS, Tailwind
- **BackEnd**: Python 3.9.4 (Django 3.2.3) 
- **Motor de base de datos**: Oracle 18c
- **Control de versiones**: Git & GitHub.

## Librerías extras de terceros.
- Validador de rut. [github.com/gevalenz/rut-chile](https://github.com/gevalenz/rut-chile)
- docx2pdf. [github.com/AlJohri/docx2pdf](https://github.com/AlJohri/docx2pdf)

## Sobre los desarrolladores
Estos son los desarrolladores que hicieron esto posible:

[![Grupo_en_Discord](./pantallazos/grupo_portafolio_discord.png)](https://github.com/Ocikotorzido/congenial-funicular/tree/master/pantallazos/)

- Fabian Astorga [@Ocikotorzido](https://github.com/Ocikotorzido)
- Francisco Marfull [@Marfullsen](https://github.com/Marfullsen)
- José Lorca [@JoseLorca](https://github.com/JoseLorca)

## Agradecimientos
Agradecemos de corazón a todos los que hicieron esto posible, sin su ayuda, nos hubiera costado mucho más terminar este proyecto.
- Centro de Innovación y Transferencia Tecnológica (CITT).

[![logo_Citt](./Mantenedor/static/img/logo_citt.png)](https://www.duoc.cl/citt/)