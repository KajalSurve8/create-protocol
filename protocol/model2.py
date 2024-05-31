# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ProtocolNew(models.Model):
    product_name = models.CharField(db_column='Product Name', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    generic_name = models.CharField(db_column='Generic name', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    formulation_type = models.CharField(db_column='Formulation Type', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    general_info = models.CharField(db_column='General Info', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    batch_number = models.IntegerField(db_column='Batch Number')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    batch_size = models.FloatField(db_column='Batch Size', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    qty_sampled = models.FloatField(db_column='QTY Sampled', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mfg_date = models.DateField(db_column='MFG Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exp_date = models.DateField(db_column='EXP Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    specification_number = models.CharField(db_column='Specification Number', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    revision_number = models.CharField(db_column='Revision Number', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    change_control_number = models.CharField(db_column='Change Control Number', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    effective_date = models.DateField(db_column='Effective Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_release = models.DateField(db_column='Date of Release', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    analysed_by = models.CharField(db_column='Analysed By', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prepared_by = models.CharField(db_column='Prepared By', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    checked_by = models.CharField(db_column='Checked By', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    approved_by = models.CharField(db_column='Approved By', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    protocolid = models.AutoField(db_column='ProtocolID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'protocol_new'
        db_table_comment = 'Form data in  Create Protocol.'


class SampleId(models.Model):
    testid = models.IntegerField(db_column='TestID', blank=True, null=True)  # Field name made lowercase.
    sampleid = models.AutoField(db_column='SampleID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sample_id'


class ScheduleOne(models.Model):
    day0 = models.IntegerField(blank=True, null=True)
    day1 = models.IntegerField(blank=True, null=True)
    day2 = models.IntegerField(blank=True, null=True)
    day3 = models.IntegerField(blank=True, null=True)
    day4 = models.IntegerField(blank=True, null=True)
    day5 = models.IntegerField(blank=True, null=True)
    day6 = models.IntegerField(blank=True, null=True)
    sl = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'schedule_one'

        
class TestListMaster(models.Model):
    serial = models.AutoField(db_column='Serial', primary_key=True)  # Field name made lowercase.
    formulation = models.CharField(db_column='Formulation', max_length=45, blank=True, null=True)  # Field name made lowercase.
    test = models.CharField(db_column='Test', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_list_master'


class TestTable2(models.Model):
    serial = models.AutoField(db_column='Serial', primary_key=True)  # Field name made lowercase.
    protocolid = models.IntegerField(db_column='ProtocolID', blank=True, null=True)  # Field name made lowercase.
    formulation = models.CharField(db_column='Formulation', max_length=45, blank=True, null=True)  # Field name made lowercase.
    test = models.CharField(db_column='Test', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_table_2'
        db_table_comment = 'Selected formulation-tests, frequency, study duration and duplicates.'


class Testtable3(models.Model):
    protocolid = models.IntegerField(db_column='ProtocolID', blank=True, null=True)  # Field name made lowercase.
    formulation = models.CharField(db_column='Formulation', max_length=45, blank=True, null=True)  # Field name made lowercase.
    test = models.CharField(db_column='Test', max_length=45, blank=True, null=True)  # Field name made lowercase.
    frequency = models.IntegerField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    duplicate_value = models.IntegerField(db_column='Duplicate Value', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    testid = models.AutoField(db_column='TestID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'testtable3'


class DateTable(models.Model):
    serial = models.AutoField(db_column='Serial', primary_key=True)  # Field name made lowercase.
    protocolid = models.IntegerField(db_column='ProtocolID', blank=True, null=True)  # Field name made lowercase.
    testid = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'date_table'
