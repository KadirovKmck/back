# vercel_app.py
import os, django
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

django.setup()
if os.environ.get("VERCEL"):
    # миграции быстро, данные не трогаем
    call_command("migrate", run_syncdb=True, interactive=False, verbosity=0)

app = get_wsgi_application()
