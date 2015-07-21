# PyJAX 2015 Django tutorial app


## Requirements

* [Python 3](http://python.org)
* [Git](http://www.git-scm.com/)

## Instructions to run locally

```bash
python3 -m venv PyJAXenv
source PyJAXenv/bin/activate
git clone https://github.com/neo00/foodie.git
cd foodie/
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

After the last command, the application should be running on
http://localhost:8000 but will crash due to an empty database.
Visit the admin site to add some restaurants, then try again.

http://localhost:8000/admin
