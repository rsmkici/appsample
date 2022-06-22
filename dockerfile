FROM python:3.9
WORKDIR /appsample
COPY appsample /appsample/
RUN pip -r install requirements.txt
ENTRYPOINT ["python"]
CMD ["./main.py"]

