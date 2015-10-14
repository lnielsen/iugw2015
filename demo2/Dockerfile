FROM python:3.5
RUN apt-get install git
# Node.js, bower, less, clean-css, uglify-js, requirejs
RUN apt-get update
RUN apt-get -qy upgrade --fix-missing --no-install-recommends
RUN apt-get -qy install --fix-missing --no-install-recommends curl
RUN curl -sL https://deb.nodesource.com/setup_iojs_2.x | bash -

# Install dependencies
RUN apt-get -qy install --fix-missing --no-install-recommends gcc git iojs

# Slim down image
RUN apt-get clean autoclean
RUN apt-get autoremove -y
RUN rm -rf /var/lib/{apt,dpkg}/
RUN find /usr/share/doc -depth -type f ! -name copyright -delete
RUN find /usr/share/doc -empty -delete
RUN rm -rf /usr/share/man/* /usr/share/groff/* /usr/share/info/*

# Basic Python and Node.js tools
RUN pip install --upgrade pip setuptools ipython gunicorn
RUN npm update && npm install --silent -g bower less clean-css uglify-js requirejs

RUN mkdir /stuff
RUN git clone https://github.com/inveniosoftware/cookiecutter-invenio-module.git /stuff/cookiecutter-invenio-module
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
WORKDIR /code
# RUN cookiecutter /stuff/cookiecutter-invenio-module --no-input
WORKDIR /code/invenio-fungenerator
#RUN git init && git add -A
RUN pip install -e .[all]
#RUN check-manifest -u || true
RUN python setup.py build_sphinx
RUN python setup.py compile_catalog
#RUN ./run-tests.sh
RUN pip install jsmin
WORKDIR /code/invenio-fungenerator/examples
RUN mkdir -p /tmp/demo-instance
RUN flask -a app.py bower
WORKDIR /tmp/demo-instance
RUN bower install --allow-root --config.interactive=false
WORKDIR /code/invenio-fungenerator/examples
RUN flask -a app.py collect
RUN flask -a app.py assets build
RUN flask -a app.py db init
RUN flask -a app.py db create
CMD bash
