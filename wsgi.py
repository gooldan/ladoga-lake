from whitenoise import WhiteNoise

from app import my_app

application = WhiteNoise(my_app)
application.add_files('static/', prefix='static/')