# Usually we create superusers in Django to manage Admin Interface.
# After setting up user registeration, signals, and possibly creating role-based access,
# you need to manually update the existing superuser with a Profile and a role - if available.
# Use this script to handle this step

from django.contrib.auth.models import User
from book_store.models import UserProfile

superusers_without_profile = User.objects.filter(
    is_superuser=True, userprofile__isnull=True
)
for superuser in superusers_without_profile:
    UserProfile.objects.create(user=superuser, role="Admin")
