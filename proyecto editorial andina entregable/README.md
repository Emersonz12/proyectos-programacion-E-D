📚 Editorial Andina S.A.S. - Sistema de Gestión:


Sistema de escritorio para la gestión de autores y libros, desarrollado en Python usando Tkinter para la interfaz gráfica y Django para el backend y la API REST. Diseñado para facilitar el registro, visualización y administración de información editorial.

🧰 Tecnologías utilizadas
Python 3.x

Tkinter (Interfaz de usuario)

Django (Backend y API)

Django REST Framework (API REST)

SQLite3 (Base de datos)

requests (Comunicación entre frontend y backend)

Ejecución del proyecto:
1. Clonar el repositorio
 git clone
 cd proyectoandina
2. Instalar dependencias
✅ Asegúrate de tener Python instalado (versión 3.6 o superior).
✅ Se recomienda usar un entorno virtual (venv).
 Django,djangorestframework
 pip install 
 
 ⚠️ Si no tienes Django instalado, puedes instalarlo ejecutando:
 pip install django
Y para la API REST:
pip install djangorestframework

3. Ejecutar el backend (API Django)
 cd backend
 python manage.py makemigrations
 python manage.py migrate
 python manage.py runserver
 (La API estará disponible en http://127.0.0.1:8000/api/)

4. Ejecutar la aplicación de escritorio (frontend)
 cd frontend
 python -m app

Funcionalidades principales:
- Registro de autores (nombre, nacionalidad, edad)
- Registro de libros (título, género, páginas, año)
- Visualización en tabla
- Eliminación por ID
- Validación de campos
- Prevención de duplicados
- Respaldo automático de datos cada minuto en archivos de texto plano
API REST:
GET /api/autores/ -> Lista de autores
POST /api/autores/ -> Crear autor
DELETE /api/autores/{id}/ -> Eliminar autor
GET /api/libros/ -> Lista de libros
POST /api/libros/ -> Crear libro
DELETE /api/libros/{id}/ -> Eliminar libro

🎯 Objetivo del Proyecto

Mejorar la eficiencia de la editorial al gestionar información.

Brindar una solución local, rápida y sin dependencias externas.

🎓 Autor

Daniel alejandro luna rojas

Estudiante de la universidad del valle

📋 Licencia
Este proyecto fue desarrollado como parte de un ejercicio académico para la empresa Editorial Andina S.A.S.. Su distribución está limitada a fines educativos y demostrativos.