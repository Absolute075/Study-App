
import os
from pathlib import Path
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Определяем BASE_DIR так же, как в settings.py
BASE_DIR = Path(__file__).resolve().parent.parent

application = get_wsgi_application()

# WhiteNoise для раздачи статики
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))

