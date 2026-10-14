import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
  env_name = os.environ.get("ENVIRONMENT", "Development")
  return (
      f"Hello from Cloud Run Version 2! Running in {{env_name}} environment. Revision:"
      f" {{os.environ.get('K_REVISION', 'unknown')}}"
  )


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
