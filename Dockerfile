
FROM mcr.microsoft.com/playwright/python:v1.49.0-jammy


WORKDIR ..


COPY requirements.txt .
RUN  pip install --no-cache-dir -r requirements.txt


RUN python3 -m playwright install chromium
RUN python -m playwright install-deps chromium





COPY . .

CMD ["python", "search_script.py"]
