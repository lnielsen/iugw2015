FROM python:3.5
RUN apt-get install git
RUN mkdir /stuff
RUN git clone https://github.com/inveniosoftware/cookiecutter-invenio-module.git /stuff/cookiecutter-invenio-module
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
WORKDIR /code
CMD bash
