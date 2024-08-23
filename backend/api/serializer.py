from api.models import User, Todo, ChatMessage, Profile
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')  # Fields to be included in the serialized output

# Serializer for the Profile model
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'full_name', 'image']  # Fields to be included in the serialized output

# Custom token serializer to include additional user profile information in JWT
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Add custom claims to the JWT token
        token['full_name'] = user.profile.full_name
        token['username'] = user.username
        token['email'] = user.email
        token['bio'] = user.profile.bio
        token['image'] = str(user.profile.image)
        token['verified'] = user.profile.verified
        
        return token

# Serializer for user registration, including password validation and confirmation
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,  # This field will not be included in the response
        required=True,
        validators=[validate_password]  # Validate password strength
    )
    password2 = serializers.CharField(write_only=True, required=True)  # Confirm password field

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')  # Fields for registration

    def validate(self, attrs):
        # Ensure the passwords match
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        # Create a new user and set the password
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        
        return user

# Serializer for the Todo model
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user', 'title', 'completed']  # Fields to be included in the serialized output

# Serializer for the ChatMessage model, including nested ProfileSerializer
class ChatMessageSerializer(serializers.ModelSerializer):
    reciever_profile = ProfileSerializer(read_only=True)  # Nested serializer for receiver's profile
    sender_profile = ProfileSerializer(read_only=True)    # Nested serializer for sender's profile

    class Meta:
        model = ChatMessage
        fields = ['id', 'user', 'sender', 'sender_profile', 'reciever', 'reciever_profile', 'message', 'read', 'date']  # Fields to be included in the serialized output
