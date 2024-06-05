import logging

import awsgi
import flask

import board
import common

app = flask.Flask(__name__)


def configure_logger(l: logging.Logger):
    l.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter(
            fmt="%(asctime)s.%(msecs)03d|%(levelname)s|%(name)s|%(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    l.addHandler(handler)
    l.propagate = False


logger = common.LOGGER
configure_logger(logger)


# Future ideas:
# 1. Add an annotation that computes execution time and adds to the response


@app.route("/sudoku/board_parse", methods=["POST"])
def board_parse():
    logger.info("Board parse triggered")
    data = flask.request.get_json()

    try:
        board.parse_user_input(data)
    except common.AppError as e:
        return flask.jsonify({"error": e.message}), e.http_code

    response = {"status": "ok", "data": data}
    return flask.jsonify(response), 200


def lambda_handler(event, context):
    """AWS Lambda handler."""
    logger.info(
        "Lambda handler triggered for %s:%s",
        event.get("path", "?"),
        event.get("httpMethod", "?"),
    )
    return awsgi.response(app, event, context)


# Enable running locally.
if __name__ == "__main__":
    app.run(debug=True)
