import jsonschema

import common

logger = common.LOGGER

USER_INPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "num_columns": {"type": "integer"},
        "num_rows": {"type": "integer"},
        "board_as_text": {"type": "string"},
    },
    "required": ["board_as_text"],
}


def parse_user_input(request):
    try:
        jsonschema.validate(instance=request, schema=USER_INPUT_SCHEMA)
    except jsonschema.ValidationError as e:
        raise common.AppError.input_error(f"Invalid request - {type(e).__name__}: {e}")
    except jsonschema.SchemaError as e:
        raise common.AppError.config_error(
            f"Invalid schema definition - {type(e).__name__}: {e}"
        )

    return request
