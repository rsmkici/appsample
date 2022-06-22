FROM python:3.8
WORKDIR /usr/src/app
COPY . .
RUN pip  install -r requirements.txt
ENV environment default_env_value
ENTRYPOINT ["python"]
CMD ["sh", "-c","python /usr/src/app/mainlinux.py ${environment}"]

