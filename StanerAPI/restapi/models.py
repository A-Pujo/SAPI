from django.db import models


class Announcements(models.Model):
    id = models.BigAutoField(primary_key=True)
    organization = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='organization')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    attachment = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'announcements'


class Banners(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banners'


class EventBanners(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_banners'


class Events(models.Model):
    id = models.BigAutoField(primary_key=True)
    organization = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='organization')
    title = models.CharField(max_length=255)
    description = models.TextField()
    committee = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    attachment = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    is_featured = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class Majors(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    contact = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'majors'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class OrganizationCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'organization_categories'


class Organizations(models.Model):
    id = models.BigAutoField(primary_key=True)
    organization_category = models.ForeignKey(OrganizationCategories, models.DO_NOTHING, db_column='organization_category')
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    chairman = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organizations'


class Regulations(models.Model):
    id = models.BigAutoField(primary_key=True)
    organization = models.ForeignKey(Organizations, models.DO_NOTHING, db_column='organization')
    title = models.CharField(max_length=255)
    regulatory_number = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    attachment = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regulations'


class Scholarships(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    agency = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    attachment = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scholarships'


class Semesters(models.Model):
    id = models.BigAutoField(primary_key=True)
    study_program = models.ForeignKey('StudyPrograms', models.DO_NOTHING, db_column='study_program')
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semesters'


class Shortlinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='user')
    title = models.CharField(max_length=255)
    description = models.TextField()
    long_url = models.TextField()
    short_url = models.CharField(max_length=255)
    visitor = models.PositiveIntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shortlinks'


class Students(models.Model):
    id = models.BigAutoField(primary_key=True)
    semester = models.ForeignKey(Semesters, models.DO_NOTHING, db_column='semester')
    name = models.CharField(max_length=255)
    npm = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    year_generation = models.PositiveIntegerField()
    year_graduation = models.PositiveIntegerField()
    class_field = models.CharField(db_column='class', max_length=255)  # Field renamed because it was a Python reserved word.
    number = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class StudyPrograms(models.Model):
    id = models.BigAutoField(primary_key=True)
    major = models.ForeignKey(Majors, models.DO_NOTHING, db_column='major')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_programs'


class Subjects(models.Model):
    id = models.BigAutoField(primary_key=True)
    semester = models.ForeignKey(Semesters, models.DO_NOTHING, db_column='semester')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    session = models.CharField(max_length=255)
    sks = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subjects'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    npm = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Whistleblows(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Users, models.DO_NOTHING, db_column='user')
    organization = models.ForeignKey(Organizations, models.DO_NOTHING, db_column='organization')
    title = models.CharField(max_length=255)
    description = models.TextField()
    attachment = models.TextField()
    is_secret = models.IntegerField()
    is_anonim = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'whistleblows'
