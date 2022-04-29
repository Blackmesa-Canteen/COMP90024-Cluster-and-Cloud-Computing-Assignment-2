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

# config file will not copy into container,
# Instead, use volume mapping.
#ADD ./config $WORKDIR/config

# dependencies
RUN pip install -r requirements.txt

# Running params, when run the docker image build by this script,
# build docker: docker build -t crawler_demo:v1 .
# `docker run --name="crawler" -e SCENARIO="1" --mount type=bind,source=E:\projects\COMP90024-Cluster-and-Cloud-Computing-Assignment-2\twitter_crawler\sample\partial_covid_id_file_compressed\,target=/data/covid-tweet-ids crawler_demo`
ENV SCENARIO=""

CMD python main_app.py -s $SCENARIO