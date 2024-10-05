from django_api_example.app_core import models
from rest_framework import serializers, viewsets


class _EmailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Emails
        fields = "__all__"
        read_only_fields = [
            "created_at",
            "updated_at",
        ]


class EmailsViewSet(viewsets.ModelViewSet):
    queryset = models.Emails.objects.all()
    serializer_class = _EmailsSerializer
