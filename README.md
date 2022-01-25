# Environment variables

```python
API=http://api.openweathermap.org/data/2.5/weather
API_KEY=
CACHE_HOST=redis
CACHE_PORT=6379
```

# Quickstart
Choose one of the following installation methods

### Docker
```bash
docker-compose up
```

### Pipenv
```bash
pipenv install
pipenv shell
python manage.py runserver
```

# Run tests
```bash
python manage.py test
```

# Usage
```python
curl -L --request GET \
  --url 'http://localhost:8000/weather?city=Cali&country=co'
```
