#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fantacycricket.settings")

    from django.core.management import execute_from_command_line

<<<<<<< HEAD
    execute_from_command_line(sys.argv)
=======
    execute_from_command_line(sys.argv)
>>>>>>> 63db62f4c73dc5f00ed00e4a89f79f9634d8944c
