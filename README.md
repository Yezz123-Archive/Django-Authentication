# Django-Authentication [![Testing](https://github.com/yezz123/Django-Authentication/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/yezz123/Django-Authentication/actions/workflows/pytest.yml)

A simple Boilerplate to Setup Authentication using Django-allauth, with a custom template for login and registration using `django-crispy-forms`.

## Getting Started

### Prerequisites

- Python 3.8.6 or higher

### Project setup

```sh
# clone the repo
$ git clone https://github.com/yezz123/Django-Authentication

# move to the project folder
$ cd Django-Authentication
```

### Creating virtual environment

- Create a `virtual environment` for this project:

```shell
# creating pipenv environment for python 3
$ virtualenv venv

# activating the pipenv environment
$ cd venv/bin #windows environment you activate from Scripts folder

# if you have multiple python 3 versions installed then
$ source ./activate
```

### Configured Enviromment

#### Environment variables

```shell
SECRET_KEY = #random string
DEBUG = #True or False
ALLOWED_HOSTS = #localhost
DATABASE_NAME = #database name (You can just use the default if you want to use SQLite)
DATABASE_USER = #database user for postgres
DATABASE_PASSWORD = #database password for postgres
DATABASE_HOST = #database host for postgres
DATABASE_PORT = #database port for postgres
ACCOUNT_EMAIL_VERIFICATION = #mandatory or optional
EMAIL_BACKEND = #email backend
EMAIL_HOST = #email host
EMAIL_HOST_PASSWORD = #email host password
EMAIL_USE_TLS = # if your email use tls
EMAIL_PORT = #email port
```

> change all the environment variables in the `.env.sample` and don't forget to rename it to `.env`.

### Run the project

After Setup the environment, you can run the project using the `Makefile` provided in the project folder.

```makefile
help:
 @echo "Targets:"
 @echo "    make install" #install requirements
 @echo "    make makemigrations" #prepare migrations
 @echo "    make migrations" #migrate database
 @echo "    make createsuperuser" #create superuser
 @echo "    make run_server" #run the server
 @echo "    make lint" #lint the code using black
 @echo "    make test" #run the tests using Pytest
```

## Preconfigured Packages

Includes preconfigured packages to kick start Django-Authentication by just setting appropriate configuration.

| Package                                                      | Usage                                                            |
| ------------------------------------------------------------ | ---------------------------------------------------------------- |
| [django-allauth](https://django-allauth.readthedocs.io/en/latest/)        | Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.           |
| [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) | django-crispy-forms provides you with a `crispy` filter and `{% crispy %}` tag that will let you control the rendering behavior of your Django forms in a very elegant and DRY way.     |

## Contributing

- Django-Authentication is a simple project, so you can contribute to it by just adding your code to the project to improve it.
- If you have any questions, please feel free to open an issue or create a pull request.

## License

This project is licensed under the terms of the MIT license.
