from django.conf import settings

EXCLUDE_PATH = settings.SPECTACULAR_SETTINGS["EXCLUDE_PATH"]


def remove_apis_from_list(endpoints):
    return [
        (path, path_regex, method, callback)
        for (path, path_regex, method, callback) in endpoints
        if path not in EXCLUDE_PATH
    ]
