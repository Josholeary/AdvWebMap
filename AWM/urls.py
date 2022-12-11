"""AWM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('world.urls')),
    # Django PWA is deprecated with Django beyond 4.0 due to Django.conf.urls
    # After a lot of research the following pull request was found in relation to the matter:
    # https://stackoverflow.com/questions/71713923/django-pwa-error-cannot-import-name-url-from-django-conf-urls
    # First approach was to change the source code of Django-PWA but this is impossible to deploy in a docker container
    # Instead Django was set to 3.2.16
    path('', include('pwa.urls')),
]
