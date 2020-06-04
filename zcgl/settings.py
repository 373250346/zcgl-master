import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将apps加入到sources root列表中
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '74+-r=c=(lv+%n1@&o$hu6c@2mrkv9l^90iailhhzlrjmk)k^j'

# SECURITY WARNING: don't run with debug turned on in production!
# 部署到生产中需要将debug改为false
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pure_pagination',
    'users',
    'servers',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zcgl.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'zcgl.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zcgl',
        'USER': 'root',
        'PASSWORD': 'Abc@dyg2019.',
        'HOST': '192.168.221.173',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# 静态文件相关设置
STATIC_URL = '/static/'

# 部署到生产中将此选项注释
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'static')
]

# 部署到生产中将此选项注释取消
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 扩展django自带的user model，添加字段
AUTH_USER_MODEL = 'users.UserProfile'

# 分页的相关设置
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 6,
    'MARGIN_PAGES_DISPLAYED': 1,
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}

# 定义全局的变量
per_page = 15  # 定义html页面中列表每页显示的数量

# 全局404配置，名称必须是handler404
handler404 = 'users.views.page_not_found'

# 全局500配置，名称必须是handler500
handler500 = 'users.views.page_error'
