import logging

import flask
import jsonschema
import aws_lambda_wsgi

app = flask.Flask(__name__)


def create_logger(name: str) -> logging.Logger:
    l = logging.getLogger(name)
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
    return l


logger = create_logger("board_parse")

request_schema = {
    "type": "object",
    "properties": {
        "num_columns": {"type": "integer"},
        "num_rows": {"type": "integer"},
        "board_as_text": {"type": "string"},
    },
    "required": ["board_as_text"],
}


@app.route("/sudoku/board_parse", methods=["POST"])
def board_parse():
    logger.info("Board parse triggered")
    data = flask.request.get_json()

    try:
        jsonschema.validate(instance=data, schema=request_schema)
    except jsonschema.ValidationError as e:
        return (
            flask.jsonify(
                {
                    "error": f"JSON input does not follow schema - {type(e).__name__}: {e}"
                }
            ),
            400,
        )
    except jsonschema.SchemaError as e:
        logging.error("request_schema is incorrect - %s: %s", type(e).__name__, e)
        return (
            flask.jsonify(
                {"error": f"Invalid schema definition - {type(e).__name__}: {e}"}
            ),
            500,
        )

    response = {"message": "Received the board data", "data": data}

    return flask.jsonify(response)


def lambda_handler(event, context):
    logger.info("Lambda handler triggered")
    return aws_lambda_wsgi.response(app, event, context)


if __name__ == "__main__":
    app.run(debug=True)
