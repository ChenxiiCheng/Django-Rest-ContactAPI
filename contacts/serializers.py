from rest_framework.serializers import ModelSerializer
from .models import Contact

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'country_code', 'phone_number','contact_picture', 'is_favorite']