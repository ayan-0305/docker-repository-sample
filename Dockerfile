FROM ubuntu:16.04

RUN uname -a

RUN apt-get update

RUN apt-get install -y --no-install-recommends python-setuptools
RUN apt-get install -y --no-install-recommends python-pip

RUN pip install --upgrade pip

ENV HOME /root
RUN echo $HOME

RUN mkdir $HOME/target

ENV WORKPATH $HOME/target

COPY user-influence.py $WORKPATH/user-influence.py

RUN pwd
RUN python $WORKPATH/user-influence.py