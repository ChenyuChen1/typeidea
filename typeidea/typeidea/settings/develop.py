from .base import *     # NOQA
# NOQA这个注释的作用是：告诉PEP8规范检测工具，这个地方不用检测。

# 我们把base.py中的DEBUG=True也剪切粘贴过来。
# 在开发环境中，DEBUG=True是正常的，但是如果到线上环境依然开启此配置，那就是一场灾难
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}