from rest_framework import serializers
from authentications.models import User
from phonenumber_field.serializerfields import PhoneNumberField


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=194)
    phone_number = PhoneNumberField(allow_null=False,allow_blank=False)
    password = serializers.CharField(min_length = 8,write_only = True)


    class Meta:
        model = User
        fields = [
            'username', 'first_name','last_name','email','phone_number','password'
        ]


    def validate(self,attrs):
        username_exists = User.objects.filter(username = attrs['username']).exists()
        if username_exists:
            raise serializers.ValidationError(detail='Username Exists')
        last_name_exists = User.objects.filter(last_name = attrs['last_name']).exists()
        if last_name_exists:
            raise serializers.ValidationError(detail='LastName Exists')
        email_exists = User.objects.filter(email = attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError(detail='Email Exists')
        phoneNumber_exists = User.objects.filter(phone_number = attrs['phone_number']).exists()
        if phoneNumber_exists:
            raise serializers.ValidationError(detail='phoneNumber Exists')

        return super(UserSerializer,self).validate(attrs)


    def create(self,validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            phone_number = validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
