from dataclasses import field
import copy


def default_field(obj):
    return field(default_factory=lambda: copy.copy(obj))
