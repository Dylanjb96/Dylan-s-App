from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,  # Importing TokenRefreshView for handling token refresh functionality
)

urlpatterns = [
    # URL pattern for obtaining JWT tokens
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # URL pattern for refreshing JWT tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # URL pattern for user registration
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    
    # URL pattern for a test endpoint, likely used for testing purposes
    path('test/', views.testEndPoint, name='test'),
    
    # URL pattern for getting API route information (likely a view that returns the list of available routes)
    path('', views.getRoutes),

    # Todo URL patterns
    # URL pattern to list todos for a specific user
    path("todo/<user_id>/", views.TodoListView.as_view()),
    
    # URL pattern to get detailed information about a specific todo item for a user
    path("todo-detail/<user_id>/<todo_id>/", views.TodoDetailView.as_view()),
    
    # URL pattern to mark a specific todo item as completed
    path("todo-mark-as-completed/<user_id>/<todo_id>/", views.TodoMarkAsCompleted.as_view()),

    # Chat message URL patterns
    # URL pattern to get messages for the logged-in user
    path("my-messages/<user_id>/", views.MyInbox.as_view()),
    
    # URL pattern to get messages between a specific sender and receiver
    path("get-messages/<sender_id>/<reciever_id>/", views.GetMessages.as_view()),
    
    # URL pattern to send a new message
    path("send-messages/", views.SendMessage.as_view()),

    # Profile and user search URL patterns
    # URL pattern to get detailed information about a user profile
    path("profile/<int:pk>/", views.ProfileDetail.as_view()),
    
    # URL pattern to search for users by username
    path("search/<username>/", views.SearchUser.as_view()),
]
