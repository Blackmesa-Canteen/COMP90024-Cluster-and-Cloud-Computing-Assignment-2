FROM python:3.10

ENV WORKDIR="/twitter_crawler"
RUN mkdir $WORKDIR
WORKDIR $WORKDIR

# Copy codes into docker
ADD ./common_util $WORKDIR/common_util
ADD ./covid_twitter_util $WORKDIR/covid_twitter_util
ADD ./crawlers $WORKDIR/crawlers
ADD ./db_util $WORKDIR/db_util
ADD ./historical_twitter_util $WORKDIR/historical_twitter_util
ADD ./nlp_util $WORKDIR/nlp_util
ADD ./twitter_stream_util $WORKDIR/twitter_stream_util
ADD ./twitter_util $WORKDIR/twitter_util
ADD ./main_app.py $WORKDIR/main_app.py
ADD ./path_helper.py $WORKDIR/path_helper.py
ADD ./requirements.txt $WORKDIR/requirements.txt

# Copy config files from the host folder where Dockerfile is stored to the container
ADD ./config $WORKDIR/config

# dependencies
RUN pip install -r requirements.txt

# Running params, when run the docker image build by this script,
# `docker run --name="crawler" -e SCENARIO="1" image_name` to select senario
ENV SCENARIO=""

# CMD python main_app.py -s $SCENARIO