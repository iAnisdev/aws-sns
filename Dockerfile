FROM python:3.14.2-slim

WORKDIR /app

# setup uv 

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

COPY main.py ./

EXPOSE 8000

CMD ["uv", "run", "fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8000"]