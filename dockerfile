FROM python:3.9
WORKDIR /applocal
COPY . /applocal
RUN pip  install -r requirements.txt
ENTRYPOINT ["python"]
CMD [" python ./mainlinux.py"]

