FROM python:3.12-slim
WORKDIR /app
COPY . .
CMD ["python", "-m", "tests.test_all"]
