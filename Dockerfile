FROM python

COPY ./ ./

CMD ["python","yawnoc.py","0","800","100"]

