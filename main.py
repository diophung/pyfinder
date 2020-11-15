from flask import Flask
from datetime import datetime
import threading

app = Flask(__name__)

@app.route("/")
def home():
	curr_thread_id = threading.current_thread().ident
	timestamp = datetime.now()

	return "HTTP 200 | thread_ident: {} | {}".format(curr_thread_id, timestamp)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)