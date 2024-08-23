from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Subquery, OuterRef, Q
from api.models import User, Todo, ChatMessage, Profile

from api.serializer import MyTokenObtainPairSerializer, RegisterSerializer, TodoSerializer, ChatMessageSerializer, ProfileSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

# Custom token obtain view using JWT
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Register view for creating new users
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)  # Allow registration for any user
    serializer_class = RegisterSerializer

# Endpoint to list available API routes
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]
    return Response(routes)

# Test endpoint to verify API functionality for GET and POST requests
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)

# View to list and create Todo items for a specific user
class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = User.objects.get(id=user_id)
        todo = Todo.objects.filter(user=user)  # Filter todos by the user
        return todo

# View to retrieve, update, or delete a specific Todo item for a user
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs['user_id']
        todo_id = self.kwargs['todo_id']
        user = User.objects.get(id=user_id)
        todo = Todo.objects.get(id=todo_id, user=user)  # Get todo item specific to the user
        return todo

# View to mark a specific Todo item as completed
class TodoMarkAsCompleted(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs['user_id']
        todo_id = self.kwargs['todo_id']
        user = User.objects.get(id=user_id)
        todo = Todo.objects.get(id=todo_id, user=user)  # Get todo item specific to the user
        todo.completed = True  # Mark as completed
        todo.save()
        return todo

# View to list messages in the inbox of a specific user
class MyInbox(generics.ListAPIView):
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']

        # Subquery to get the latest message ID between users
        latest_message_subquery = ChatMessage.objects.filter(
            Q(sender=OuterRef('pk'), reciever=user_id) | Q(reciever=OuterRef('pk'), sender=user_id)
        ).order_by('-date').values('id')[:1]

        # Main query to get messages based on latest message IDs
        messages = ChatMessage.objects.filter(
            Q(sender=user_id) | Q(reciever=user_id),
            id__in=Subquery(latest_message_subquery)
        ).order_by('-date')

        return messages

# View to list messages between a specific sender and receiver
class GetMessages(generics.ListAPIView):
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        sender_id = self.kwargs['sender_id']
        reciever_id = self.kwargs['reciever_id']

        try:
            messages = ChatMessage.objects.filter(
                Q(sender=sender_id, reciever=reciever_id) | 
                Q(sender=reciever_id, reciever=sender_id)
            ).order_by('date')  # Ordering by date to ensure chronological order
            return messages
        except Exception as e:
            print("Error fetching messages:", e)
            return ChatMessage.objects.none()

# View to create a new chat message
class SendMessage(generics.CreateAPIView):
    serializer_class = ChatMessageSerializer

# View to retrieve and update user profile information
class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]

# View to search for users based on username, full name, or email
class SearchUser(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]  

    def list(self, request, *args, **kwargs):
        username = self.kwargs['username']
        logged_in_user = self.request.user
        users = Profile.objects.filter(Q(user__username__icontains=username) | 
                                       Q(full_name__icontains=username) | 
                                       Q(user__email__icontains=username) &
                                       ~Q(user=logged_in_user))  # Exclude logged-in user from search results

        if not users.exists():
            return Response(
                {"detail": "No users found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
