from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import User, Event
from .serializers import UserSerializer


class EventSerializer:
    pass


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'])
    def invite_to_event(self, request, pk=None):
        # Implement invite logic here
        user = self.get_object()
        event_id = request.data.get('event_id')
        # Add code to invite user to event
        return Response({'message': f'Invited user {user.name} to event {event_id}'})

    @action(detail=True, methods=['post'])
    def accept_invitation(self, request, pk=None):
        # Implement accept invitation logic here
        user = self.get_object()
        event_id = request.data.get('event_id')
        # Add code to accept event invitation
        return Response({'message': f'User {user.name} accepted invitation to event {event_id}'})

    @action(detail=True, methods=['post'])
    def invite_collaborator(self, request, pk=None):
        event = self.get_object()
        collaborator_id = request.data.get('collaborator_id')

        try:
            collaborator = User.objects.get(id=collaborator_id)
            event.collaborators.add(collaborator)
            event.save()
            return Response({'message': f'Invited collaborator {collaborator.name} to event {event.title}'})
        except User.DoesNotExist:
            return Response({'message': 'Collaborator not found'}, status=400)
    class EventViewSet(viewsets.ReadOnlyModelViewSet):
        queryset = Event.objects.all()
        serializer_class = EventSerializer

        def get_queryset(self):
            queryset = Event.objects.all()
            user_id = self.request.query_params.get('user_id')
            if user_id:
                queryset = queryset.filter(creator_id=user_id)  # Filter events by creator
            return queryset