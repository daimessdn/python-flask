# Python Flask Tutorial

## 1. Creating Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## 2. Setting up Virtual Environment

```bash
pip install flask

touch app.py
```

## 3. Creating `run.py`

```python
from flask import Flask

app = Flask(__name__)

# main route
@app.route("/")
def index():
    return "Hello, world"

if (__name__ == "__main__"):
    app.run(debug=True)
```

## 4. Running Flask Server

```bash
python run.py
```

or

```bash
export FLASK_APP=run.py
export FLASK_ENV=development # deprecated
export FLASK_DEBUG=1         # debug = True

flask run
```