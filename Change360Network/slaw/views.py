from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

from .models import Nominees
from .serializers import NomineeSerializers, UserSerializers


class NomineesListView(viewsets.ModelViewSet):
    queryset = Nominees.objects.filter(is_approved=True)
    serializer_class = NomineeSerializers
    filterset_fields = [
        'award_category',
        'level',
        'institution',
        'course_of_study'
    ]
    permission_classes = [IsAuthenticatedOrReadOnly]


class VoteView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, nominee_id):
        nominee = get_object_or_404(Nominees, pk=nominee_id)
        nominee_data = {
            "Full Name": nominee.full_name,
            "Total Votes": nominee.votes
        }
        return Response(data=nominee_data, status=status.HTTP_200_OK)

    def post(self, request, nominee_id):
        nominee = get_object_or_404(Nominees, pk=nominee_id)
        nominee.votes = nominee.votes + 1
        nominee.save()
        return Response({'result': "Vote has been casted successfully"})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
