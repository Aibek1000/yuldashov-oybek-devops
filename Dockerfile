FROM python:3.12-slim
WORKDIR /app
COPY app/ .
RUN python -m compileall .
EXPOSE 8000
CMD ["python", "-u", "main.py"]
