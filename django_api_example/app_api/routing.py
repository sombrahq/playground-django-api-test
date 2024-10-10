from django_api_example.app_api.resources import emails
from rest_framework import routers

api_router = routers.DefaultRouter()

api_router.register(r"emails", emails.EmailsViewSet)
