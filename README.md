Herramienta
-----------
escáner de seguridad para APIs en Python. Este script:

✅ Descubre endpoints automáticamente en una API mediante fuzzing de rutas comunes.
✅ Detecta vulnerabilidades básicas como SQL Injection (SQLi), XSS y SSRF.
✅ Genera un reporte en formato JSON con los hallazgos.




🛠 Cómo Usarlo:
------------------

Copia el repositorio del github
---------------------------------
sudo git clone https://github.com/TekillaSMR/TekillaSMR.git

Instala requests si no lo tienes:
---------------------------------

bash

pip install requests

Ejecuta el script e ingresa la URL de la API que deseas analizar:
----------------------------------------------------------------

bash

python api_scanner.py

El script probará endpoints comunes y generará un reporte JSON con las vulnerabilidades detectadas.
---------------------------------------------------------------------------------------------------
