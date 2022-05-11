FROM python:3.10

ENV WORKDIR="/Backend"
RUN mkdir $WORKDIR
WORKDIR $WORKDIR

ADD ./config/app_config.yaml $WORKDIR/config/app_config.yaml
ADD ./controller $WORKDIR/controller
ADD ./service $WORKDIR/service
ADD ./util $WORKDIR/util
ADD ./app.py $WORKDIR/app.py
ADD ./path_helper.py $WORKDIR/path_helper.py
ADD ./requirements.txt $WORKDIR/requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]