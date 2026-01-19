
FROM mcr.microsoft.com/playwright/python:v1.49.0-jammy


WORKDIR ..


COPY requirements.txt .


RUN python  pip install requirements.txt
RUN python3 -m playwright install chromium
RUN python3 -m playwright codegen google.com





COPY . .

CMD ["python", "search_script.py"]
