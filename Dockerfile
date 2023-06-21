FROM python:3.10

COPY ./ ./app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR '/app'

CMD ["python", "yawnoc.py","0","800","100"]



