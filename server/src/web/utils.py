from werkzeug.exceptions import BadRequest


def filter_name(name):
    # Enforce that the quantity is a string
    if not isinstance(name, str):
        raise BadRequest(description=f"Invalid product name")

    # To prevent injections, only accept product names with no spaces
    return name.split(" ")[0]
