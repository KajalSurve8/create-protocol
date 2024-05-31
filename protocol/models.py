# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import date   

class ProtocolNew(models.Model):
    FORM_LIST ={
        ('Tablet', 'Tablet'),
        ('Soft Gelatin Capsule', 'Soft Gelatin Capsule'),
        ('Hard Gelatin Capsule', 'Hard Gelatin Capsule'),
    }
    product_name = models.CharField(db_column='Product Name', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    generic_name = models.CharField(db_column='Generic name', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    formulation_type = models.CharField(db_column='Formulation Type', max_length=45, choices=FORM_LIST)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    general_info = models.CharField(db_column='General Info', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    batch_number = models.IntegerField(db_column='Batch Number')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    batch_size = models.FloatField(db_column='Batch Size', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    qty_sampled = models.FloatField(db_column='QTY Sampled', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mfg_date = models.DateField(db_column='MFG Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exp_date = models.DateField(db_column='EXP Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    study_start_date = models.DateField(db_column='Study Start Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
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

class TestListMaster(models.Model):
    serial = models.AutoField(db_column='Serial', primary_key=True)  # Field name made lowercase.
    formulation = models.CharField(db_column='Formulation', max_length=45, blank=True, null=True)  # Field name made lowercase.
    test = models.CharField(db_column='Test', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_list_master'

#----------------------TestTable2---------------------------------------
class Table2fillerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(formulation=TestListMaster.formulation)
    
class TestTable2(models.Model):
    serial = models.AutoField(db_column='Serial', primary_key=True)  # Field name made lowercase.
    protocolid = models.IntegerField(db_column='ProtocolID', blank=True, null=True)  # Field name made lowercase.
    formulation = models.CharField(db_column='Formulation', max_length=45, blank=True, null=True)  # Field name made lowercase.
    test = models.CharField(db_column='Test', max_length=45, blank=True, null=True)  # Field name made lowercase.
    study_start_date = models.DateField(db_column='Study Start Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'test_table_2'
        db_table_comment = 'Selected formulation-tests, frequency, study duration and duplicates.'
    
    selected_formu=Table2fillerManager()
    objects = models.Manager()


class Testtable3(models.Model):
    protocolid = models.IntegerField(db_column='ProtocolID', blank=True, null=True)  # Field name made lowercase.
    formulation = models.CharField(db_column='Formulation', max_length=45, blank=True, null=True)  # Field name made lowercase.
    test = models.CharField(db_column='Test', max_length=45, blank=True, null=True)  # Field name made lowercase.
    frequency = models.IntegerField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    duplicate_value = models.IntegerField(db_column='Duplicate Value', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    testid = models.AutoField(db_column='TestID', primary_key=True)  # Field name made lowercase.
    study_start_date = models.DateField(db_column='Study Start Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'testtable3'



class SampleId(models.Model):
    testid = models.IntegerField(db_column='TestID', blank=True, null=True)  # Field name made lowercase.
    sampleid = models.AutoField(db_column='SampleID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_id'



class DateTable(models.Model):
    serial = models.AutoField(db_column='Serial', primary_key=True)  # Field name made lowercase.
    protocolid = models.IntegerField(db_column='ProtocolID', blank=True, null=True)  # Field name made lowercase.
    testid = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'date_table'


class ScheduleOne(models.Model):

     today_date=date.today()
     today_date1=today_date+relativedelta(days=1)
     today_date2=today_date+relativedelta(days=2)
     today_date3=today_date+relativedelta(days=3)
     today_date4=today_date+relativedelta(days=4)
     today_date5=today_date+relativedelta(days=5)
     today_date6=today_date+relativedelta(days=6)

     day0 = models.IntegerField(blank=True, null=True, verbose_name=today_date)
     day1 = models.IntegerField(blank=True, null=True, verbose_name=today_date1)
     day2 = models.IntegerField(blank=True, null=True, verbose_name=today_date2)
     day3 = models.IntegerField(blank=True, null=True, verbose_name=today_date3)
     day4 = models.IntegerField(blank=True, null=True, verbose_name=today_date4)
     day5 = models.IntegerField(blank=True, null=True, verbose_name=today_date5)
     day6 = models.IntegerField(blank=True, null=True, verbose_name=today_date6)
     sl = models.AutoField(primary_key=True)

     class Meta:
        managed = False
        db_table = 'schedule_one'