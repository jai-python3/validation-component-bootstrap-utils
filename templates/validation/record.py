import re
import logging

from enum import Enum
from typing import Union


import pydantic


{% for attribute_name in lookup %}
# TODO: implement pattern regex for {{ field_name }}
{{ attribute_name | upper }}_PATTERN = r'^$'
{% endfor %}



{% for attribute_name in lookup %}
class Invalid{{ lookup[attribute_name].class_name }}Error(Exception):
    """TODO: insert docstring for this Invalid{{ lookup[attribute_name].class_name }}Error class."""
    def __init__(self, value: str, message: str) -> None:
        """Class constructor for Invalid{{ lookup[attribute_name].class_name }}Error class."""
        self.value = value
        self.message = message
        super().__init__(message)

{% endfor %}

class Record(pydantic.BaseModel):
    """Class for encapsulating the rows in {{ file_type }} files."""
    {%- for attribute_name in lookup %}
    {{ attribute_name }}: {{ lookup[attribute_name].datatype }}
    {%- endfor %}


    @pydantic.root_validator(pre=True)
    @classmethod
    def is_record_valid(cls, values) -> None:
        # TODO: need to implement the root validator
        # raise InvalidRecordError(message="")
        pass

    {% for attribute_name in lookup %}

    @pydantic.validator("{{ attribute_name }}")
    @classmethod
    def is_{{ attribute_name }}_valid(cls, value):
        """Validate value for {{ lookup[attribute_name].column_name }} column (column number {{lookup[attribute_name].column_position}})."""
        if value:
            # TODO: implement validation here
            return value
        else:
            raise Invalid{{ lookup[attribute_name].class_name}}Error(value=value, message=f"{{ lookup[attribute_name].column_name }} (in column number {{ lookup[attribute_name].column_position }}) should ...  TODO")

    {% endfor %}
