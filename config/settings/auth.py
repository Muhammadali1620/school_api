AUTH_USER_MODEL = 'users.CustomUser'

# LOGIN_URL = 'login'
# LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'login'


# AUTHENTICATION_BACKENDS = [
#     'apps.users.backends.ModelBackend',
# ]
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ]
}