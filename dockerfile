FROM python:3.9
WORKDIR /appsample
COPY . /appsample/
RUN pip  install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["./main.py"]

