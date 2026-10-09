Se crea el proyecto con `uv init --package clasificador-paquetes`

Dependencias:

uv add pydantic scikit-learn joblib numpy scipy pytest

uv sync
uv run python -m clasificador_paquetes.inference
uv run pytest

Para ejecutar el inference:
uv run python -m clasificador_paquetes.inference

Para correr el test:
uv run pytest