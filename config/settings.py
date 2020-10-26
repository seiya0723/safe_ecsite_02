"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#gitなどでシークレットキー流出を防ぐため。local_settings.pyにSECRET_KEYを指定、読み込ませる
SECRET_KEY = "シークレットキー文字列を入力する"
try:
    from .local_settings import *
except ImportError:
    pass



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#localhostsのアクセスを許可する
ALLOWED_HOSTS = [ "127.0.0.1" ]



#################django-allauthでのメール認証設定ここから###################

#djangoallauthでメールでユーザー認証する際に必要になる認証バックエンド
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

#ログイン時の認証方法はemailとパスワードとする
ACCOUNT_AUTHENTICATION_METHOD   = "email"

#ログイン時にユーザー名(ユーザーID)は使用しない
ACCOUNT_USERNAME_REQUIRED       = "False"

#ユーザー登録時に入力したメールアドレスに、確認メールを送信する事を必須(mandatory)とする
ACCOUNT_EMAIL_VARIFICATION  = "mandatory"

#ユーザー登録画面でメールアドレス入力を要求する(True)
ACCOUNT_EMAIL_REQUIRED      = True


#ここにメール送信設定を入力する(Sendgridを使用する場合)
EMAIL_BACKEND   = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST      = 'smtp.sendgrid.net'
EMAIL_USE_TLS   = True
EMAIL_PORT      = 587


#【超重要】メールのパスワードとメールアドレスの入力後、GitHubへのプッシュはダメ!!絶対!!不正アクセスされるよ!!
"""
EMAIL_HOST_USER     = ''
EMAIL_HOST_PASSWORD = ''
"""
#DEBUGがTrueのとき、メールの内容は全て端末に表示させる
if DEBUG:
    EMAIL_BACKEND   = "django.core.mail.backends.console.EmailBackend"

#CHECK:認証時のメールの本文等の編集は templates/allauth/account/email/ から行うことができる

#################django-allauthでのメール認証設定ここまで###################

#django-allauth関係。django.contrib.sitesで使用するSITE_IDを指定する
SITE_ID = 1
#django-allauthログイン時とログアウト時のリダイレクトURL
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'




#3桁区切りでカンマ
NUMBER_GROUPING = 3

# Application definition

#DBを使用するアプリを読み込む
#humanizeでカンマ区切りで表示できる
#TODO:djangoallauth一式を追加。予めpipコマンドでdjangoallauthをインストールしておく。 pip install django-allauth
#TIPS:allauth.socialaccountを使用することでSNSアカウントを使用したログインも可能になる。
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.humanize',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'shopping.apps.ShoppingConfig',
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

ROOT_URLCONF = 'config.urls'


#'DIRS'にos.path.join(BASE_DIR,"templates")を含める
#allauthのテンプレートも読み込ませる。
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,"templates"),
            os.path.join(BASE_DIR, 'templates', 'allauth')
            ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/


#CODEはja、TIME_ZONEはAsia/Tokyoを指定
LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


#デプロイ後の静的ファイルの指定
PROJECT_NAME = os.path.basename(BASE_DIR)
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = '/var/www/{}/static'.format(PROJECT_NAME)

STATIC = "/var/www/{}/static".format(PROJECT_NAME)

