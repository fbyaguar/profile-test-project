# profile-test-project

profile-test-project is the django test project

## Installation

Use requirements.txt to install libraries

```bash
-r requirements.txt
```
Migrate migrations

```bash
python src/manage.py migrate
```

Use fixtures

```bash
python src/manage.py loaddata profile.json
```

## Run

```bash
python src/manage.py runserver
