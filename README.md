# leipzig [![Build Status](https://travis-ci.org/wolfskaempf/leipzig.svg?branch=master)](https://travis-ci.org/wolfskaempf/leipzig) [![Stories in Ready](https://badge.waffle.io/wolfskaempf/leipzig.png?label=ready&title=Ready)](https://waffle.io/wolfskaempf/leipzig)
A web app for the 80th International Session of the European Youth Parliament
***
## What is `leipzig`?
While programming this web app I tried to make it as easily modifiable as possible, allowing future sessions to fork it and to modify it to their liking. Of course it's main purpose was serving as a web app for the 80th International Session of the European Youth Parliament.
***
## Usage
### Standard
To run this web app locally, clone the repository, cd into it and execute the following commands.

`source bin/activate`

`python manage.py runserver`

Please not that this is only a development server which should never be used for production scenarios.

### Troubleshooting

If you run into problems try installing the dependencies from `requirements.txt` using `pip install -r requirements.txt` but be aware whether you're in a virtual environment or not. We do not want to alter the system's actual environment.
