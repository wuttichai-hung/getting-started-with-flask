# Clone me

After you clone my git by this command

```bash
git clone https://github.com/wuttichai-hung/getting-started-with-flask
```

You will see the hierarchy of the folder like this

```
getting-started-with-flask
├─ templates
│   └─ index.html
├─ Dockerfile
├─ main.py
└─ requirements.txt
```

You can ignore other files that I do not mention to

# Setting up

You can set up all dependencies by this command

```requirements:requirements.txt
pip install -r requirements.txt
```

# Let's look at main.py

It contains your flask code that is shown in the figure below

```python:main.py
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")                 # render ./templates/index.html

@app.route('/api', methods=["POST", "GET"])              # allow http method
def api():
    if request.method == "POST":                         # http method condition
        return jsonify(msg="Post Method Ok", value="30") # return velue as a json
    else:
        return jsonify(msg="Get Methood Ok", value="30")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Now you can run `main.py`

```bash
python main.py
```

# Deployment

Now you can put them into the container that you can shift and run anywhere

```Dockerfile:Dockerfile
FROM python:3.8-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
```

## Build

You can build you `Dockerfile` to be a container

```bash
docker build -t flask .
```

## Run

Are you ready?, let's run it.

```bash
docker run -p 8000:5000 --name flask -d flask
```
