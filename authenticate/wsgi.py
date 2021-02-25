"""
WSGI config for authenticate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, 'authenticate/.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'authenticate.settings')

application = get_wsgi_application()