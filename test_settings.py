"""
These settings are here to use during tests, because django requires them.

In a real-world use case, apps in this project are installed into other
Django applications, so these settings will not be used.
"""

from os.path import abspath, dirname, join


def root(*args):
    """
    Get the absolute path of the given path relative to the project root.
    """
    return join(abspath(dirname(__file__)), *args)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'default.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'token_utils',
)

LOCALE_PATHS = [
    root('token_utils', 'conf', 'locale'),
]

ROOT_URLCONF = 'token_utils.urls'

SECRET_KEY = 'insecure-secret-key'

MIDDLEWARE = (
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
)

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': False,
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',  # this is required for admin
            'django.contrib.messages.context_processors.messages',  # this is required for admin
        ],
    },
}]


TOKEN_SIGNING = {
    'JWT_ISSUER': 'token-test-issuer',
    'JWT_SIGNING_ALGORITHM': 'RS512',
    'JWT_SUPPORTED_VERSION': '1.2.0',
    'JWT_PRIVATE_SIGNING_JWK': """
        {
            "kid": "token-test-sign",
            "kty": "RSA",
            "key_ops": [
                "sign"
            ],
            "n": "o5cn3ljSRi6FaDEKTn0PS-oL9EFyv1pI7dRgffQLD1qf5D6sprmYfWWokSsrWig8u2y0HChSygR6Jn5KXBqQn6FpM0dDJLnWQDRXHLl3Ey1iPYgDSmOIsIGrV9ZyNCQwk03wAgWbfdBTig3QSDYD-sTNOs3pc4UD_PqAvU2nz_1SS2ZiOwOn5F6gulE1L0iE3KEUEvOIagfHNVhz0oxa_VRZILkzV-zr6R_TW1m97h4H8jXl_VJyQGyhMGGypuDrQ9_vaY_RLEulLCyY0INglHWQ7pckxBtI5q55-Vio2wgewe2_qYcGsnBGaDNbySAsvYcWRrqDiFyzrJYivodqTQ",
            "e": "AQAB",
            "d": "HIiV7KNjcdhVbpn3KT-I9n3JPf5YbGXsCIedmPqDH1d4QhBofuAqZ9zebQuxkRUpmqtYMv0Zi6ECSUqH387GYQF_XvFUFcjQRPycISd8TH0DAKaDpGr-AYNshnKiEtQpINhcP44I1AYNPCwyoxXA1fGTtmkKChsuWea7o8kytwU5xSejvh5-jiqu2SF4GEl0BEXIAPZsgbzoPIWNxgO4_RzNnWs6nJZeszcaDD0CyezVSuH9QcI6g5QFzAC_YuykSsaaFJhZ05DocBsLczShJ9Omf6PnK9xlm26I84xrEh_7x4fVmNBg3xWTLh8qOnHqGko93A1diLRCrKHOvnpvgQ",
            "p": "3T3DEtBUka7hLGdIsDlC96Uadx_q_E4Vb1cxx_4Ss_wGp1Loz3N3ZngGyInsKlmbBgLo1Ykd6T9TRvRNEWEtFSOcm2INIBoVoXk7W5RuPa8Cgq2tjQj9ziGQ08JMejrPlj3Q1wmALJr5VTfvSYBu0WkljhKNCy1KB6fCby0C9WE",
            "q": "vUqzWPZnDG4IXyo-k5F0bHV0BNL_pVhQoLW7eyFHnw74IOEfSbdsMspNcPSFIrtgPsn7981qv3lN_staZ6JflKfHayjB_lvltHyZxfl0dvruShZOx1N6ykEo7YrAskC_qxUyrIvqmJ64zPW3jkuOYrFs7Ykj3zFx3Zq1H5568G0",
            "dp": "Azh08H8r2_sJuBXAzx_mQ6iZnAZQ619PnJFOXjTqnMgcaK8iSHLL2CgDIUQwteUcBphgP0uBrfWIBs5jmM8rUtVz4CcrPb5jdjhHjuu4NxmnFbPlhNoOp8OBUjPP3S-h-fPoaFjxDrUqz_zCdPVzp4S6UTkf6Hu-SiI9CFVFZ8E",
            "dq": "WQ44_KTIbIej9qnYUPMA1DoaAF8ImVDIdiOp9c79dC7FvCpN3w-lnuugrYDM1j9Tk5bRrY7-JuE6OaKQgOtajoS1BIxjYHj5xAVPD15CVevOihqeq5Zx0ZAAYmmCKRrfUe0iLx2QnIcoKH1-Azs23OXeeo6nysznZjvv9NVJv60",
            "qi": "KSWGH607H1kNG2okjYdmVdNgLxTUB-Wye9a9FNFE49UmQIOJeZYXtDzcjk8IiK3g-EU3CqBeDKVUgHvHFu4_Wj3IrIhKYizS4BeFmOcPDvylDQCmJcC9tXLQgHkxM_MEJ7iLn9FOLRshh7GPgZphXxMhezM26Cz-8r3_mACHu84"
        }
    """,  # noqa: E501,

    'JWT_PUBLIC_SIGNING_JWK_SET': """
        {
          "keys": [
            {
              "kid": "token-test-sign",
              "kty": "RSA",
              "n": "o5cn3ljSRi6FaDEKTn0PS-oL9EFyv1pI7dRgffQLD1qf5D6sprmYfWWokSsrWig8u2y0HChSygR6Jn5KXBqQn6FpM0dDJLnWQDRXHLl3Ey1iPYgDSmOIsIGrV9ZyNCQwk03wAgWbfdBTig3QSDYD-sTNOs3pc4UD_PqAvU2nz_1SS2ZiOwOn5F6gulE1L0iE3KEUEvOIagfHNVhz0oxa_VRZILkzV-zr6R_TW1m97h4H8jXl_VJyQGyhMGGypuDrQ9_vaY_RLEulLCyY0INglHWQ7pckxBtI5q55-Vio2wgewe2_qYcGsnBGaDNbySAsvYcWRrqDiFyzrJYivodqTQ",
              "e": "AQAB"
            },
            {
              "kid": "token-test-wrong-key",
              "kty": "RSA",
              "n": "o5cn3ljSRi6FaDEKTn0PS-oL9EFyv1pI7dRgffQLD1qf5D6sprmYfWWokSsrWig8u2y0HChSygR6Jn5KXBqQn6FpM0dDJLnWQDRXHLl3Ey1iPYgDSmOIsIGrV9ZyNCQwk03wAgWbfdBTig3QSDYD-sTNOs3pc4UD_PqAvU2nz_1SS2ZiOwOn5F6gulE1L0iE3KEUEvOIagfHNVhz0oxa_VRZILkzV-zr6R_TW1m97h4H8jXl_VJyQGyhMGGypuDrQ9_vaY_RLEulLCyY0INglHWQ7pckxBtI5q55-Vio2wgewe2_qYcGsnBGaDNbySAsvYcWRrqDiFyzrJYivodqTQ",
              "e": "AQAB"
            }
          ]
        }
    """,  # noqa: E501
}
