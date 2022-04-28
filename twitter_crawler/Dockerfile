FROM python:3.10

ENV WORKDIR="/twitter_crawler"
WORKDIR $WORKDIR

# Copy codes into docker
COPY ./common_util $WORKDIR/common_util
COPY ./covid_twitter_util $WORKDIR/covid_twitter_util
COPY ./crawlers $WORKDIR/crawlers
COPY ./db_util $WORKDIR/db_util
COPY ./historical_twitter_util $WORKDIR/historical_twitter_util
COPY ./nlp_util $WORKDIR/nlp_util
COPY ./twitter_stream_util $WORKDIR/twitter_stream_util
COPY ./twitter_util $WORKDIR/twitter_util
ADD ./main_app.py $WORKDIR/main_app.py
ADD ./path_helper.py $WORKDIR/path_helper.py
ADD ./requirements.txt $WORKDIR/requirements.txt

# Copy config files from the host folder where Dockerfile is stored to the container
COPY ./config $WORKDIR/config

# dependencies
RUN pip install -r requirements.txt

# Running params, when run the docker image build by this script,
# `docker run --name="crawler" -e SCENARIO="1" image_name` to select senario
ENV SCENARIO=""

CMD ["python", '$WORKDIR/main_app.py -s $SCENARIO']