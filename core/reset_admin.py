import os
import django

# Replace 'core' with the actual folder name if it's different
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings') 
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

try:
    # This creates a brand new admin so you don't have to guess the old username
    User.objects.create_superuser('newadmin', 'admin@example.com', 'ResetPass123!')
    print("New superuser 'newadmin' created successfully.")
except Exception as e:
    print(f"Error: {e}")
