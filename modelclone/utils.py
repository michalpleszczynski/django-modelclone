import re


def camel_to_snake(string):
    """
    Convert camel case string to snake case.

    CamelCase -> camel_case
    WhoKnowsWhat -> who_knows_what
    snake_case -> snake_case
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
