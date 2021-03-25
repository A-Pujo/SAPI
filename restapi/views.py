from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication 
from .models import *
from .serializers import *

# Create your views here.

class AnnouncementsAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = AnnouncementsSerializer
    queryset = Announcements.objects.all()
    
    lookup_field = 'id'
    
    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        
        else:    
            return self.list(request)
        
    def post(self, request):
        
        return self.create(request)    
    
    def put(self, request, id = None):
        
        return self.update(request, id)
    
    def delete(self, request, id):
        
        return self.destroy(request, id)
    
class BannersAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = BannersSerializer
    queryset = Banners.objects.all()
    
    lookup_field = 'id'
    
    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        
        else:    
            return self.list(request)
        
    def post(self, request):
        
        return self.create(request)    
    
    def put(self, request, id = None):
        
        return self.update(request, id)
    
    def delete(self, request, id):
        
        return self.destroy(request, id)
        
class EvBannersAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = EvBannersSerializer
    queryset = EventBanners.objects.all()
    
    lookup_field = 'id'
    
    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        
        else:
            return self.list(request)
        
    def post(self, request):
        
        return self.create(request)    
    
    def put(self, request, id = None):
        
        return self.update(request, id)
    
    def delete(self, request, id):
        
        return self.destroy(request, id)

class EventsAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = EventsSerializer
    queryset = Events.objects.all()
    
    lookup_field = 'id'
    
    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        
        else:
            return self.list(request)
    
    def post(self, request):
        
        return self.create(request)    
    
    def put(self, request, id = None):
        
        return self.update(request, id)
    
    def delete(self, request, id):
        
        return self.destroy(request, id)

class MajorsAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = MajorsSerializer
    queryset = Majors.objects.all()
    
    lookup_field = 'id'
    
    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        
        else:
            return self.list(request)
    
    def post(self, request):
        
        return self.create(request)    
    
    def put(self, request, id = None):
        
        return self.update(request, id)
    
    def delete(self, request, id):
        
        return self.destroy(request, id)

class OrganizationCatAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = OrgCatSerializer
    queryset = OrganizationCategories.objects.all()
    
    lookup_field = 'id'
    
    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        
        else:    
            return self.list(request)
        
    def post(self, request):
        
        return self.create(request)    
    
    def put(self, request, id = None):
        
        return self.update(request, id)
    
    def delete(self, request, id):
        
        return self.destroy(request, id)
        
class OrganizationAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = OrgSerializer
    queryset = Organizations.objects.all()
    
    lookup_field = 'id'
    
    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        
        else:
            return self.list(request)
        
    def post(self, request):
        
        return self.create(request)    
    
    def put(self, request, id = None):
        
        return self.update(request, id)
    
    def delete(self, request, id):
        
        return self.destroy(request, id)
    
class RegulationAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = RegulationsSerializer
    queryset = Regulations.objects.all()
    
    lookup_field = 'id'
    
    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        
        else:
            return self.list(request)
    
    def post(self, request):
        
        return self.create(request)    
    
    def put(self, request, id = None):
        
        return self.update(request, id)
    
    def delete(self, request, id):
        
        return self.destroy(request, id)
    
class ScholarshipAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = ScholarshipsSerializer
    queryset = Scholarships.objects.all()
    
    lookup_field = 'id'
    
    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        
        else:
            return self.list(request)
        
    def post(self, request):
        
        return self.create(request)    
    
    def put(self, request, id = None):
        
        return self.update(request, id)
    
    def delete(self, request, id):
        
        return self.destroy(request, id)
    
class SemestersAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = SemestersSerializer
    queryset = Semesters.objects.all()
    
    lookup_field = 'id'
    
    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        
        else:
            return self.list(request)
        
    def post(self, request):
        
        return self.create(request)    
    
    def put(self, request, id = None):
        
        return self.update(request, id)
    
    def delete(self, request, id):
        
        return self.destroy(request, id)
    
class ShortlinksAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = ShortlinksSerializer
    queryset = Shortlinks.objects.all()
    
    lookup_field = 'id'
    
    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        
        else:
            return self.list(request)

    def post(self, request):
        
        return self.create(request)    
    
    def put(self, request, id = None):
        
        return self.update(request, id)
    
    def delete(self, request, id):
        
        return self.destroy(request, id)
    
class StudentsAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    permission_classes = [IsAuthenticated]
    
    serializer_class = StudentsSerializer
    queryset = Students.objects.all()
    
    lookup_field = 'id'
    
    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        
        else:
            return self.list(request)
        
    def post(self, request):
        
        return self.create(request)    
    
    def put(self, request, id = None):
        
        return self.update(request, id)
    
    def delete(self, request, id):
            
        return self.destroy(request, id)
        
class StudyProgramAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = StudyPSerializer
    queryset = StudyPrograms.objects.all()
    
    lookup_field = 'id'
    
    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        
        else:
            return self.list(request)
        
    def post(self, request):
        
        return self.create(request)    
    
    def put(self, request, id = None):
        
        return self.update(request, id)
    
    def delete(self, request, id):
        
        return self.destroy(request, id)
    
class SubjectsAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = SubjectsSerializer
    queryset = Subjects.objects.all()
    
    lookup_field = 'id'
    
    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        
        else:
            return self.list(request)
        
    def post(self, request):
        
        return self.create(request)    
    
    def put(self, request, id = None):
        
        return self.update(request, id)
    
    def delete(self, request, id):
        
        return self.destroy(request, id)
    
class WhistleblowsAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = WsbSerializer
    queryset = Whistleblows.objects.all()
    
    lookup_field = 'id'
    
    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        
        else:
            return self.list(request)
    
    def post(self, request):
        
        return self.create(request)    
    
    def put(self, request, id = None):
        
        return self.update(request, id)
    
    def delete(self, request, id):
        
        return self.destroy(request, id)