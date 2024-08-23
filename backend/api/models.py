from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Custom User model extending AbstractUser to use email as the username field
class User(AbstractUser):
    # Override the default username field with a CharField
    username = models.CharField(max_length=100)
    
    # Email field with unique constraint
    email = models.EmailField(unique=True)

    # Define the field used for authentication
    USERNAME_FIELD = 'email'
    
    # Fields that are required when creating a superuser
    REQUIRED_FIELDS = ['username']

    # Method to get the associated profile for this user
    def profile(self):
        return Profile.objects.get(user=self)

# Profile model associated with the User model via OneToOne relationship
class Profile(models.Model):
    # Link to the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Fields for additional user information
    full_name = models.CharField(max_length=1000, null=True, blank=True)
    bio = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="user_images", default="default.jpg", null=True, blank=True)
    verified = models.BooleanField(default=False)

    # Save method to ensure the profile's full_name is set to the username if not provided
    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = self.user.username
        super(Profile, self).save(*args, **kwargs)

# Signal handler to create a Profile when a User is created
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Signal handler to save the Profile when the User is saved
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Connect the signal handlers to the post_save signal of the User model
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

# Model for Todo items, related to a User
class Todo(models.Model):
    # Link to the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Fields for the Todo item
    title = models.CharField(max_length=1000)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    # String representation of the Todo item (first 30 characters of the title)
    def __str__(self):
        return self.title[:30]

# Model for Chat messages between users
class ChatMessage(models.Model):
    # Foreign key fields for sender and receiver, each related to the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reciever")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")

    # Fields for the message details
    message = models.CharField(max_length=1000)
    read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Order chat messages by date
        ordering = ['date']
        # Set a plural name for the model in the admin interface
        verbose_name_plural = "Message"
    
    # String representation of the ChatMessage (sender and receiver)
    def __str__(self):
        return f"{self.sender} sent {self.reciever}"
    
    # Property to get the sender's profile
    @property
    def sender_profile(self):
        return Profile.objects.get(user=self.sender)
    
    # Method to get the receiver's profile
    def reciever_profile(self):
        return Profile.objects.get(user=self.reciever)
