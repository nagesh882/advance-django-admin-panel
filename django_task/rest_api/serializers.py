from rest_framework import serializers
from login.models import Products, Register

# Product Serializer is used for de-serialize complex data to netive python data
class productSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Products
        fields = ["product_id", "product_name", "product_price", "hsn_code", "manufacture_date", "expiry_date", "created_datetime", "updated_datetime", "created_by"]


# Register Serializer is used for de-serialize complex data to netive python data
class registerSerializer(serializers.HyperlinkedModelSerializer):
    product_buyer_name = productSerializer(many=True, read_only=True)
    class Meta:
        model = Register
        fields = ["user_id", "user_name", "user_email", "user_phone", "user_dob", "gender", "aadhar", "pan", "marital_status", "address", "city", "district", "state", "country", "pin_code","product_buyer_name"]
