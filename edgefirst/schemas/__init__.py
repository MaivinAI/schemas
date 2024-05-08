import copy
from dataclasses import field

def default_field(obj):
    return field(default_factory=lambda: copy.copy(obj))