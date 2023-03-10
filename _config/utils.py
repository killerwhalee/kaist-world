# utlis.py
import os
from uuid import uuid4
from django.utils import timezone

def uuid_filepath(instance, filename):
    app_name = instance.__class__._meta.app_label
    model_name = instance.__class__.__name__.lower()
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return '/'.join([
        app_name,
        model_name,
        uuid_name + extension,
    ])