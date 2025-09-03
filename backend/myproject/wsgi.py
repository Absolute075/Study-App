
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()

# WhiteNoise — подключаем через метод add_files (рекомендовано в документации)
from whitenoise import WhiteNoise
application = WhiteNoise(application)

