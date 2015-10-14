# Developing

## Development server

```console
$ docker-compose build
```

## Basic application

```console
$ compose run web bash
$ flask -a app.py --help
...
Commands:
  assets   Web assets commands.
  bower    Generate a bower.json file.
  collect  Collect static files.
  db       Database commands.
  run      Runs a development server.
  shell    Runs a shell in the app context.
```

Running a development server:

```console
$ flask -a app.py run
app
 * Serving Flask app "app"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Starting a shell:

```console
$ flask -a app.py shell
app
Python 3.5.0 (default, Sep 14 2015, 20:19:17)
[GCC 4.9.2] on linux
App: app
Instance: /tmp/demo-instance
>>>
```

## Webserver in docker

Start containers:

```console
$ docker-compose up
Attaching to demo2_web_1
web_1 |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
web_1 |  * Restarting with stat
```

Go to http://<docker ip>:5000/
