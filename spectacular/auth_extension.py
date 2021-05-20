from drf_spectacular.contrib.rest_framework_simplejwt import SimpleJWTScheme


class SimpleJWTTokenUserScheme(SimpleJWTScheme):
    name = "CustomJWTAuth"
    target_class = "custom_jwt.authentication.CustomJWTAuthentication"
