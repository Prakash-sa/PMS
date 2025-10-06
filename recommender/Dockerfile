FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml /app/
RUN pip install -U pip && pip install -e .
COPY . /app
CMD ["python", "-m", "pms_rec.train", "--no-train"]
