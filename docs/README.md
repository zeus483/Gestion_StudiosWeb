# Gestion_StudiosWeb
this is a program for the gestion, of a studio webcam
#estuctura de archivos:
Backend
/app: Contiene todo el código del backend.
/api: Define los endpoints de la API.
/endpoints: Cada archivo aquí corresponde a un grupo de endpoints relacionados con un aspecto específico de la aplicación.
/core: Configuraciones centrales y código de seguridad.
/crud: Funciones para operaciones CRUD que interactúan con la base de datos.
/db: Configuración de la base de datos y manejo de sesiones de SQLAlchemy.
/models: Define los modelos de SQLAlchemy que representan las tablas de la base de datos.
/schemas: Pydantic models para validación y serialización de datos.
/services: Servicios que contienen lógica de negocio.
main.py: Archivo principal que inicia la aplicación FastAPI.
/tests: Tests para los diferentes módulos de la aplicación.
Frontend
/src: Código fuente del frontend.
/components: Componentes de Vue reutilizables.
/views: Componentes de Vue que representan páginas completas.
/router: Configuración del enrutador Vue.
/store: Estado centralizado de Vuex.
Scripts y Documentación
/scripts: Scripts útiles para despliegue o configuración.
/docs: Documentación del proyecto.
docker-compose.yml: Para configurar servicios necesarios como bases de datos o servidores adicionales.
