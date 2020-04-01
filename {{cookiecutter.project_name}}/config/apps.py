DJANGO_APPS = [
    "djangocms_admin_style",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

THIRD_PARTY_APPS = [
    "cms",
    "treebeard",
    "menus",
    "sekizai",
    "djangocms_text_ckeditor",
    "reversion",
    "easy_thumbnails",
    "filer",
    "mptt",
    "cmsplugin_filer_file",
    "cmsplugin_filer_folder",
    "cmsplugin_filer_link",
    "cmsplugin_filer_image",
    "cmsplugin_filer_teaser",
    "cmsplugin_filer_video",
]

LOCAL_APPS = []

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
