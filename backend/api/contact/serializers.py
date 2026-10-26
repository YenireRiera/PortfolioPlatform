
from rest_framework import serializers

from apps.contact.models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "company",
            "service",
            "subject",
            "message",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "El nombre no puede estar vacío."
            )
        return value.strip()

    def validate_subject(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "El asunto no puede estar vacío."
            )
        return value.strip()

    def validate_message(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "El mensaje no puede estar vacío."
            )
        return value.strip()
