#FROM python:3.10
FROM lcarles/anacondaenv

# RUN pip install --no-cache-dir -r requirements.txt
COPY ./ ./

CMD ["python.exe","yawnoc.py","0","800","100"]


