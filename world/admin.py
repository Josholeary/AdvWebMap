from django.contrib.gis import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import *


admin.site.register(WorldBorder, admin.OSMGeoAdmin)


User = get_user_model()

