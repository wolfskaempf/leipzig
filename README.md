# leipzig [![Build Status](https://travis-ci.org/wolfskaempf/leipzig.svg?branch=master)](https://travis-ci.org/wolfskaempf/leipzig) [![Stories in Ready](https://badge.waffle.io/wolfskaempf/leipzig.png?label=ready&title=Ready)](https://waffle.io/wolfskaempf/leipzig) [![Code Issues](https://www.quantifiedcode.com/api/v1/project/f4a66d367ed64893af1f44817ef1dbf2/badge.svg)](https://www.quantifiedcode.com/app/project/f4a66d367ed64893af1f44817ef1dbf2)
A web app for the 80th International Session of the European Youth Parliament
***
## What is `leipzig`?
While programming this web app I tried to make it as easily modifiable as possible, allowing future sessions to fork it and to modify it to their liking. However, it's main purpose was serving as a web app for the 80th International Session of the European Youth Parliament. In the future I might make it even more accessible to other sessions.
***
## Usage
### Standard
To run this web app locally, clone the repository, cd into it and execute the following commands.

`pip install virtualenv`

`virtualenv .`

`source bin/activate`

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py runserver`

Please note that this is only a development server which should never be used for production scenarios.

You can now login to the [admin area of your local development server](http://localhost:8000/admin/) and start creating sample content.

### Troubleshooting

If you run into problems try installing the dependencies from `requirements.txt` using `pip install -r requirements.txt` but be aware whether you're in a virtual environment or not. We do not want to alter the system's actual environment.
