# "Python Teacher"

Setup:
```
python -m venv .venv

# Windows
.venv\scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

Run: `python manage.py runserver`

Test: `python manage.py test`

Based on Azure's Django sample, available at https://github.com/Azure-Samples/msdocs-python-django-webapp-quickstart, MIT licensed (c) Microsoft Corporation.

The `.gitignore`, `infra`, `manage.py`, and `quickstartproject` folders/files are left as-is from the template.
A real app would probably change/specialize them.
