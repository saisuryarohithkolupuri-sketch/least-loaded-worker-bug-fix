from flask import Flask
from flask import jsonify

from workers import workers
from load_balancer import LeastLoadedBalancer

app = Flask(__name__)

balancer = LeastLoadedBalancer(workers)


@app.route("/assign", methods=["GET"])
def assign():

    worker = balancer.assign_task()

    return jsonify({

        "assigned_worker": worker,

        "active_tasks": balancer.workers

    })


if __name__ == "__main__":

    app.run(debug=True)