from rest_framework import serializers
from .models import *

class AnnouncementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = '__all__'
        
class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = '__all__'
        
class EvBannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventBanners
        fields = '__all__'
        
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
        
class MajorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Majors
        fields = '__all__'
        
class OrgCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationCategories
        fields = '__all__'
        
class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = '__all__'
        
class RegulationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regulations
        fields = '__all__'
        
class ScholarshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarships
        fields = '__all__'
        
class SemestersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semesters
        fields = '__all__'

class ShortlinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortlinks
        fields = '__all__'
        
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['name', 'npm', 'gender', 'year_generation']
        
class StudentsSerializer_dt(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
        
class StudyPSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPrograms
        fields = '__all__'
        
class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'
        
class WsbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whistleblows
        fields = ['title', 'organization', 'description', 'attachment']