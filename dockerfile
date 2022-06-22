FROM python:3.9
ADD main.py .
ADD templates/* .
RUN pip install requests beautifulsoup4 python-dotenv
WORKDIR /
CMD ["python","./main.py"]

