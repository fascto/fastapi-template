# {{ cookiecutter.project_name }}

Proyecto FastAPI minimalista con versionado y estructura modular.

## Cómo correr

### Local
```bash
uvicorn src.main:app --reload
```

### Docker
```bash
docker build -t {{ cookiecutter.project_slug }} .
docker run -p 8000:8000 {{ cookiecutter.project_slug }}
```