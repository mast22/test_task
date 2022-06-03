## Running project

```shell
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Create your own .env with token just like .env-example
# Make sure redis is running on 127.0.0.1:6379

python manage.py runserver
python manage.py rundramatiq

python manage.py migrate
python manage test
```
