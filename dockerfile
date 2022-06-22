FROM alpine:3.4
WORKDIR /
COPY . /
RUN apk update
RUN apk add python
RUN pip  install -r requirements.txt
ENTRYPOINT ["python"]
CMD [" python ./mainlinux.py"]

