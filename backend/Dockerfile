FROM python:3.10

# ENV WORKDIR="/COMP90024-Backend"
# RUN mkdir $WORKDIR

# COPY requirements.txt ./
# RUN pip install -r requirements.txt
# COPY . .
COPY . /Backend

WORKDIR /Backend

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]