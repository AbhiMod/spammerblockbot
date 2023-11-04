FROM python:3.9.5-buster
WORKDIR /app
RUN chmod 777 /app
RUN pip3 install -U pip
COPY a.txt .
RUN pip3 install --no-cache-dir -U -r a.txt
COPY . .
CMD ["python", "am.py"]
