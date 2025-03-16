FROM python:3.9-slim


RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    libxi6 \
    libgconf-2-4 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY admin_bot.py .

CMD  ["python", "/app/admin_bot.py"]
ENTRYPOINT  ["python", "/app/admin_bot.py"]
