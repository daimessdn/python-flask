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

-------------------------

## Working with HTML files

- Create HTML file  inside `templates` directory (let say `index.html`)

- Import `render_template` from flask library
  
  ```python
  from flask import render_template
  ```

- Update one of return views route (let say in `@app.route("/")`
  
  - From `return "Hello, world!"`
  
  - Into `return render_template("index.html")`
  
  ```python
  # main route
  @app.route("/")
  def index():
      return render_template("index.html")
  ```

  ----------------------------

  ## Working with Static Files

  In HTML files, we can use `"{{ url_for('static', filename='js/app.js') }}"` (for example for JS) to apply static files in `static` directory we made in `app` directory. We can apply this terms for images, CSS, and other files.