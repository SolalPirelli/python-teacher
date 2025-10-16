# "Python Teacher"

Simple app that helps people learn Python by asking them to write a function given a description and a sequence of inputs/output pairs.

For now, the function to guess is hardcoded to be `x % 3`.
In a real-world app, this would be stored in the DB, there would be an admin panel to add some, etc.


## Running the app

Setup:
```
python -m venv .venv

# Windows
.venv\scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

Then run the app with `python manage.py runserver`, which will print the local server URL you can browse to.


## Tests

The tests are in `hello_azure/tests.py`.

Run tests with `python manage.py test`.


## Credit

The skeleton is based on Azure's Django sample, available at https://github.com/Azure-Samples/msdocs-python-django-webapp-quickstart, MIT licensed (c) Microsoft Corporation.

The `.gitignore`, `infra`, `manage.py`, and `quickstartproject` folders/files are left as-is from the template.
A real app would probably change/specialize them.
