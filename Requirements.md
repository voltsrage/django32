## Create django project

```
python -m django startproject {{project-name}} .
python -m django startproject project1 .
```

## Create a django secret key

```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
## To create json of table

```
python manage.py dumpdata {{table}} --indent 4 > fixtures/{{table}}.json
```