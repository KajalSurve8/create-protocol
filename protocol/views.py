from django.shortcuts import render
from django.http import HttpResponse
from .models import TestListMaster, ProtocolNew, TestTable2, Testtable3, SampleId, DateTable, ScheduleOne
from .forms import pageoneform, pagetwoform
from django.http import HttpResponseRedirect
# from .models import Table2fillerManager
from fpdf import FPDF
import numpy as np
from datetime import datetime, date
# import pandas as pd
from dateutil.relativedelta import relativedelta
from django_tables2 import SingleTableView
from .tables import PersonTable

def page_1(request):
     context ={}
     global newda,newdaf
     # create a form instance and populate it with data from the request:
     form = pageoneform(request.POST)
     print(request)
     # check whether it's valid:
     if (request.method=="POST"):
          print('first')
          if form.is_valid():
               # process the data in form.cleaned_data as required
               form.save()
               
               TestTable2.objects.all().delete()
               TestTable2obj=TestTable2()
               
               newdaf=ProtocolNew.objects.values('formulation_type')
               newdaf=newdaf.last()
               newdaf=newdaf.get('formulation_type')
               medata=TestListMaster.objects.filter(formulation=newdaf)
               print(newdaf)

               newda=ProtocolNew.objects.values('protocolid')
               newda=newda.last()
               newda=newda.get('protocolid')
               print(newda)

               ssd=ProtocolNew.objects.values('study_start_date')
               ssd=ssd.last()
               ssd=ssd.get('study_start_date')
               
               
               for i in medata:
                    print(i.test)
                    TestTable2obj=TestTable2.objects.create(protocolid=newda,test=i.test,formulation=newdaf, study_start_date=ssd)
                    # TestTable2obj=TestTable2.objects.create(formulation=newdaf)
                    # TestTable2obj=TestTable2.objects.create(protocolid=newda)

             
               # TestTable2.objects.update(protocolid=newda)
               # TestTable2.objects.update(formulation=ProtocolNew.formulation_type)
               
               print('before redirect')
               # redirect to a new URL:
               return HttpResponseRedirect("/protocol_page2")
          else:
               return HttpResponse('Form sahi nai hai')
     
     context['form']= form
     return render(request, "Page1.html", context)
  
     





def page_2(request):
     context ={}
   
     # create a form instance and populate it with data from the request:
     form = pagetwoform(request.POST)
     mydata = TestTable2.objects.all()
     newda=ProtocolNew.objects.values('protocolid')
     newda=newda.last()
     newda=newda.get('protocolid')
     newdaf=ProtocolNew.objects.values('formulation_type')
     newdaf=newdaf.last()
     newdaf=newdaf.get('formulation_type')
     ssd=ProtocolNew.objects.values('study_start_date')
     ssd=ssd.last()
     ssd=ssd.get('study_start_date')

     context['form']= form
     if (request.method=="POST"):
          TestTable2.objects.all().delete()
          form.save()
          item_ids = request.POST.getlist('checktest')
          print(item_ids)
          for i in item_ids:
               print(i)
               TestTable2obj=TestTable2.objects.create(protocolid=newda,test=i,formulation=newdaf, study_start_date=ssd)
          #return HttpResponse(item_ids)
          return HttpResponseRedirect("/protocol_page3")
    
     context = {
     'all_tests': mydata,
     }
     print('yo')
     return render(request, 'Page2.html',context)




def page_3(request):
     context ={}
     Testtable3obj=Testtable3()
     SampleIDobj=SampleId()
     newda=ProtocolNew.objects.values('protocolid')
     newda=newda.last()
     newda=newda.get('protocolid')
     # create a form instance and populate it with data from the request:
     #form = pagetwoform(request.POST)
     seltest=TestTable2.objects.filter(protocolid=newda).values_list('test', flat=True)
     my2data = seltest
     #context['form']= form
     if (request.method=="POST"):
         
         #form.save()
         durations = request.POST.getlist('duration')
         frequency = request.POST.getlist('freq')
         duplicate = request.POST.getlist('duplicate')
         abc=TestTable2.objects.values('protocolid')
         abc=abc.last()
         abc=abc.get('protocolid')
         cdef=TestTable2.objects.values('formulation')
         cdef=cdef.last()
         cdef=cdef.get('formulation')
         ssd2=ProtocolNew.objects.values('study_start_date')
         ssd2=ssd2.last()
         ssd2=ssd2.get('study_start_date')
             
         print(durations,frequency,seltest)

         for (i,j,k,l) in zip(seltest,frequency,durations,duplicate):
               print(i,j,k,l)
               #TestTable3obj=Testtable3.objects.create(protocolid=abc,test=i,formulation=cdef, frequency=j, duration=k, duplicate_value=l, study_start_date=ProtocolNew.objects.filter(pk=abc).get('study_start_date'))
               TestTable3obj=Testtable3.objects.create(protocolid=abc,test=i,formulation=cdef, frequency=j, duration=k, duplicate_value=l, study_start_date=ssd2)
               f=0


               startdate=ProtocolNew.objects.values("study_start_date").get(pk=abc)
               startdate=startdate.get('study_start_date')


               durcal=Testtable3.objects.values('duration')
               durcal=durcal.last()
               durcal=durcal.get('duration')
               frecal=Testtable3.objects.values('frequency')
               frecal=frecal.last()
               frecal=frecal.get('frequency')
               testidcal=Testtable3.objects.values('testid')
               testidcal=testidcal.last()
               testidcal=testidcal.get('testid')
               dupcal=Testtable3.objects.values('duplicate_value')
               dupcal=dupcal.last()
               dupcal=dupcal.get('duplicate_value')
               durcal=int(durcal)
               frecal=int(frecal)
               dupcal=int(dupcal)
               sampno=((durcal/frecal)+1)*(dupcal+1)
               # while(f<sampno):
               #      # caldate = startdate + relativedelta(months=n*frecal)
               #      SampleIDobj=SampleId.objects.create(testid=testidcal)
               #      f=f+1
               n=0
               i = frecal
               j = 0
               caldate = startdate
               while(n<=durcal):
                         #DateTableobj=DateTable.objects.create(testid=testidcal)
                         #caldate=np.datetime64(startdate) + np.timedelta64(n*frecal, 'M')
                         caldate = caldate + relativedelta(months=j)
                         # today = date.today()
                         if (caldate>date.today()):
                              statusvar='Active'
                         elif (caldate==date.today()):
                              statusvar='Today'
                         else :
                              statusvar='Elapsed'

                         DateTableobj = DateTable.objects.create(testid=testidcal, date=caldate, status=statusvar, protocolid=abc)
                         n=n+i 
                         j = frecal

               # DateTable.objects.filter(date=today).update(status="Today")
               # DateTable.objects.filter(date__lt=today).update(status="Elapsed")

               totaltestids = DateTable.objects.filter(testid=testidcal).count()
               print("total test ids=", totaltestids)
               testdates = DateTable.objects.filter(testid=testidcal).values_list('date', flat=True)
               print("test dates=", testdates)
               nooftimes = (sampno / totaltestids)
               print("no of times=", nooftimes)
               # while(f<sampno):
               for i in testdates:
                    print("i=", i)
                    j = 0
                    while (j < nooftimes):
                         if (i > date.today()):
                              statusvar='Active'
                         elif (i == date.today()):
                              statusvar='Today'
                         else :
                              statusvar='Elapsed'

                         SampleIDobj=SampleId.objects.create(testid=testidcal, date=i, status=statusvar)
                         j = j + 1

         #return HttpResponse("Done!")
     #     return HttpResponseRedirect("/protocol_page3")
    
     context = {
     'sel_tests': my2data,
     }
     return render(request, 'Page3.html',context)




# def showtestdate(request):
#      testd = TestDate.objects.values('test_date')
#      testd = testd.last()
#      testd = testd.get('test_date')
#      # rows = TestDate.objects.values('test_date').count()
#      i=1
#      while (i<=13):
#           testd = pd.to_datetime(testd) + pd.DateOffset(months = 1)
#           # testd = testd.date()
#           print("Test Dates: ", testd)
#           i = i + 1

#      curdate = date.today()
#      newdate = curdate + pd.DateOffset(days=7)
#      newdate = newdate.date()

     # for j in testd:
          # testd = testd.date()
          # print(j)
          # if i < newdate:
          #      print(testd)

#      context = {
#     'testdates': testd, 
#      }
     # return render(request, 'schedulepage.html')


# def genprotocolreport(request):
#      productname=ProtocolNew.objects.values('product_name')
#      productname=productname.last()
#      productname=str(productname['product_name'])
#      genericname=ProtocolNew.objects.values('generic_name')
#      genericname=genericname.last()
#      genericname=str(genericname['generic_name'])
#      formulationtype=ProtocolNew.objects.values('formulation_type')
#      formulationtype=formulationtype.last()
#      formulationtype=str(formulationtype['formulation_type'])
#      generalinfo=ProtocolNew.objects.values('general_info')
#      generalinfo=generalinfo.last()
#      generalinfo=str(generalinfo['general_info'])
#      batchnumber=ProtocolNew.objects.values('batch_number')
#      batchnumber=batchnumber.last()
#      batchnumber=str(batchnumber['batch_number'])
#      batchsize=ProtocolNew.objects.values('batch_size')
#      batchsize=batchsize.last()
#      batchsize=str(batchsize['batch_size'])
#      qtysampled=ProtocolNew.objects.values('qty_sampled')
#      qtysampled=qtysampled.last()
#      qtysampled=str(qtysampled['qty_sampled'])
#      mfgdate=ProtocolNew.objects.values('mfg_date')
#      mfgdate=mfgdate.last()
#      mfgdate=str(mfgdate['mfg_date'])
#      protocolidpdf=ProtocolNew.objects.values('protocolid')
#      protocolidpdf=protocolidpdf.last()
#      protocolidpdf=str(protocolidpdf['protocolid'])


     
#      # exp_date = models.DateField(db_column='EXP Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#      # study_start_date = models.DateField(db_column='Study Start Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#      # specification_number = models.CharField(db_column='Specification Number', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#      # revision_number = models.CharField(db_column='Revision Number', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#      # change_control_number = models.CharField(db_column='Change Control Number', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#      # effective_date = models.DateField(db_column='Effective Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#      # date_of_release = models.DateField(db_column='Date of Release', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#      # analysed_by = models.CharField(db_column='Analysed By', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#      # prepared_by = models.CharField(db_column='Prepared By', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#      # checked_by = models.CharField(db_column='Checked By', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#      # approved_by = models.CharField(db_column='Approved By', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    
#      class PDF(FPDF):
#           def header(self):
#                # Rendering logo:
#                self.image(".\protocol\stabicarelims.png", 10, 8, 33)
#                self.code39("*stb*", x=150, y=8)
#                # Setting font: helvetica bold 15
#                self.set_font("helvetica", "B", 15)
               
#                # Moving cursor to the right:
#                self.cell(80)
#                # Printing title:
#                self.cell(30, 10, "Protocol Report",align="C")
#                # Performing a line break:
#                self.ln(20)

#           def footer(self):
#                # Position cursor at 1.5 cm from bottom:
#                self.set_y(-15)
#                # Setting font: helvetica italic 8
#                self.set_font("helvetica", "I", 8)
#                # Printing page number:
#                self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")
#      pdf = PDF()
#      pdf.add_page()
#      #pdf.code39("stabicare", x=30, y=50, w=4, h=20)
#      # pdf.set_font('helvetica', size=12)
#      pdf.set_font("helvetica", 'B', 12)
#      pdf.cell(20, 5, txt='Protocol ID : ', align="L")
#      pdf.cell(40, 5, txt=protocolidpdf, ln=1, align="R")
#      # pdf.ln()

#      # pdf.set_font(style='B')
#      pdf.cell(20, 5, txt='Product Name : ', align="L")
#      pdf.cell(40, 5, txt=productname, ln=1, align="R")
#      # pdf.ln()

#      # pdf.set_font(style='B')
#      pdf.cell(20, 5, txt='Generic Name : ', align="L")
#      pdf.cell(40, 5, txt=genericname, ln=1, align="R")
#      # pdf.ln()

#      pdf.cell(20, 5, txt='General Info : ', align="L")
#      pdf.cell(40, 5, txt=generalinfo, ln=1, align="R")
#      # pdf.ln()

#      pdf.cell(20, 5, txt='Formulation Type : ', align="L")
#      pdf.cell(40, 5, txt=formulationtype, ln=1, align="R")
#      # pdf.ln()

#      pdf.cell(20, 5, txt='Batch Number : ', align="L")
#      pdf.cell(40, 5, txt=batchnumber, ln=1, align="R")
#      # pdf.ln()

#      pdf.cell(20, 5, txt='Batch Size : ', align="L")
#      pdf.cell(40, 5, txt=batchsize, ln=1, align="R")
#      # pdf.ln()

#      pdf.cell(20, 5, txt='QTY Sampled : ', align="L")
#      pdf.cell(40, 5, txt=qtysampled, ln=1, align="R")
#      # pdf.ln()

#      pdf.cell(20, 5, txt='MFG Date : ', align="L")
#      pdf.cell(40, 5, txt=mfgdate, ln=1, align="R")

#      pdf.output("report.pdf")
#      pdf_data = pdf.output()

#      print("PDF generated successfully: report.pdf")
#      # return HttpResponse(bytes(pdf.output()), content_type="application/pdf")
#      return HttpResponse(pdf_data, content_type="application/pdf") 



# def schedule(request):
#      context ={}
     
#      today_date=date.today()
#      today_date1=today_date+relativedelta(days=1)
#      today_date2=today_date+relativedelta(days=2)
#      today_date3=today_date+relativedelta(days=3)
#      today_date4=today_date+relativedelta(days=4)
#      today_date5=today_date+relativedelta(days=5)
#      today_date6=today_date+relativedelta(days=6)

#      data0=DateTable.objects.filter(date=today_date).values_list('testid', flat=True)
#      # data0=data0.list()
#      rows = data0.count()
#      data1=DateTable.objects.filter(date=today_date1).values_list('testid', flat=True)
#      # data1=data1.get('testid')
#      data2=DateTable.objects.filter(date=today_date2).values_list('testid', flat=True)
#      #data2=data2.get('testid')
#      data3=DateTable.objects.filter(date=today_date3).values_list('testid', flat=True)
#      #data3=data3.get('testid')
#      data4=DateTable.objects.filter(date=today_date4).values_list('testid', flat=True)
#      #data4=data4.get('testid')
#      data5=DateTable.objects.filter(date=today_date5).values_list('testid', flat=True)
#      #data5=data5.get('testid')
#      data6=DateTable.objects.filter(date=today_date6).values_list('testid', flat=True)
#      #data6=data6.get('testid')

#      context = {
#     'rows': rows, 'today_date': today_date,'today_date1': today_date1,'today_date2': today_date2,'today_date3': today_date3,'today_date4': today_date4,'today_date5': today_date5,'today_date6': today_date6, 'data0' : data0, 'data1' : data1, 'data2' : data2, 'data3' : data3, 'data4' : data4, 'data5' : data5, 'data6' : data6
#       }
#      print('yo')
#      print("Rows:", rows)
#      return render(request, 'schedulepage.html',context)
     

def schedule(request):
     # context ={}
     # today = date.today()
     # DateTable.objects.filter(date=today).update(status="Today")
     # DateTable.objects.filter(date__lt=today).update(status="Elapsed")

     today_date=date.today()
     today_date1=today_date+relativedelta(days=1)
     today_date2=today_date+relativedelta(days=2)
     today_date3=today_date+relativedelta(days=3)
     today_date4=today_date+relativedelta(days=4)
     today_date5=today_date+relativedelta(days=5)
     today_date6=today_date+relativedelta(days=6)

     ScheduleOne.objects.all().delete()
     scheduleobj = ScheduleOne.objects.create()

     data0=SampleId.objects.filter(date=today_date).values_list('sampleid', flat=True)
     totalidsday0 = data0.count()
     lo=ScheduleOne.objects.values('sl')
     lo=lo.first()
     lo=lo.get('sl')
     ol=lo
     if data0:
          ScheduleOne.objects.filter(sl=ol).update(day0=data0[0])
          ol += 1
          if (totalidsday0 > 1):
               i = 1
               while (i <= totalidsday0-1):
                    if not ScheduleOne.objects.filter(sl=ol).exists():
                         ScheduleOne.objects.create()
                    ScheduleOne.objects.filter(sl=ol).update(day0=data0[i])
                    i += 1
                    ol += 1
     # for x in data0:
     #      temps=ScheduleOne(day0=x)
     #      temps.save()
               

     data1=SampleId.objects.filter(date=today_date1).values_list('sampleid', flat=True)
     totalids = data1.count()
     ol=lo
     if data1:
          ScheduleOne.objects.filter(sl=ol).update(day1=data1[0])
          ol += 1
          if (totalids > 1):
               i = 1
               while (i <= totalids-1):
                    if not ScheduleOne.objects.filter(sl=ol).exists():
                         ScheduleOne.objects.create()
                    ScheduleOne.objects.filter(sl=ol).update(day1=data1[i])
                    i += 1
                    ol += 1

     # for x in data1:
     #      ScheduleOne.objects.filter(sl=ol).update(day1=x)
     #      # ScheduleOne.objects.create(day1=x)
     #      ol=ol+1
    
     data2=SampleId.objects.filter(date=today_date2).values_list('sampleid', flat=True)
     totalids = data2.count()
     ol=lo
     if data2:
          ScheduleOne.objects.filter(sl=ol).update(day2=data2[0])
          ol += 1
          if (totalids > 1):
               i = 1
               while (i <= totalids-1):
                    if not ScheduleOne.objects.filter(sl=ol).exists():
                         ScheduleOne.objects.create()
                    ScheduleOne.objects.filter(sl=ol).update(day2=data2[i])
                    i += 1
                    ol += 1

     # for x in data2:
     #      print("ol=", ol)
     #      ScheduleOne.objects.filter(sl=ol).update(day2=x)
     #      ScheduleOne.objects.create()
     #      ol=ol+1
    
     data3=SampleId.objects.filter(date=today_date3).values_list('sampleid', flat=True)
     totalids = data3.count()
     ol=lo
     if data3:
          ScheduleOne.objects.filter(sl=ol).update(day3=data3[0])
          ol += 1
          if (totalids > 1):
               i = 1
               while (i <= totalids-1):
                    if not ScheduleOne.objects.filter(sl=ol).exists():
                         ScheduleOne.objects.create()
                    ScheduleOne.objects.filter(sl=ol).update(day3=data3[i])
                    i += 1
                    ol += 1

     # for x in data3:
     #      # ScheduleOne.objects.filter(sl=ol).update(day3=x)
     #      ScheduleOne.objects.update(day3=x)
          # ol=ol+1
    
     data4=SampleId.objects.filter(date=today_date4).values_list('sampleid', flat=True)
     totalids = data4.count()
     ol=lo
     if data4:
          ScheduleOne.objects.filter(sl=ol).update(day4=data4[0])
          ol += 1
          if (totalids > 1):
               i = 1
               while (i <= totalids-1):
                    if not ScheduleOne.objects.filter(sl=ol).exists():
                         ScheduleOne.objects.create()
                    ScheduleOne.objects.filter(sl=ol).update(day4=data4[i])
                    i += 1
                    ol += 1


     # for x in data4:
     #      # ScheduleOne.objects.filter(sl=ol).update(day4=x)
     #      ScheduleOne.objects.update(day4=x)
          # ol=ol+1
    
     data5=SampleId.objects.filter(date=today_date5).values_list('sampleid', flat=True)
     totalids = data5.count()
     ol=lo
     if data5:
          ScheduleOne.objects.filter(sl=ol).update(day5=data5[0])
          ol += 1
          if (totalids > 1):
               i = 1
               while (i <= totalids-1):
                    if not ScheduleOne.objects.filter(sl=ol).exists():
                         ScheduleOne.objects.create()
                    ScheduleOne.objects.filter(sl=ol).update(day5=data5[i])
                    i += 1
                    ol += 1


     # for x in data5:
     #      # ScheduleOne.objects.filter(sl=ol).update(day5=x)
     #      ScheduleOne.objects.update(day5=x)
          # ol=ol+1
    
     data6=SampleId.objects.filter(date=today_date6).values_list('sampleid', flat=True)
     totalids = data6.count()
     ol=lo
     if data6:
          ScheduleOne.objects.filter(sl=ol).update(day6=data6[0])
          ol += 1
          if (totalids > 1):
               i = 1
               while (i <= totalids-1):
                    if not ScheduleOne.objects.filter(sl=ol).exists():
                         ScheduleOne.objects.create()
                    ScheduleOne.objects.filter(sl=ol).update(day6=data6[i])
                    i += 1
                    ol += 1


     # for x in data6:
     #      # ScheduleOne.objects.filter(sl=ol).update(day6=x)
     #      ScheduleOne.objects.update(day6=x)
          # ol=ol+1
    
     
     table = PersonTable(ScheduleOne.objects.all())
     #table.paginate(page=request.GET.get("page", 1), per_page=25)
     # data1 = list(data1)
     context = { "table": table, 
                'rows': totalidsday0, 
                }
     print('yo')
     return render(request, 'schedulepage.html', context)


def login(request):
     return render(request, 'loginpage.html')


def dashboard(request):
     # today_date=date.today()
     # today_date1=today_date+relativedelta(days=1)
     # today_date2=today_date+relativedelta(days=2)
     # today_date3=today_date+relativedelta(days=3)
     # today_date4=today_date+relativedelta(days=4)
     # today_date5=today_date+relativedelta(days=5)
     # today_date6=today_date+relativedelta(days=6)

     # data0=SampleId.objects.filter(date=today_date).values_list('sampleid', flat=True)
     # scheduledate0=SampleId.objects.filter(date=today_date).values_list('date', flat=True)
     # status0=SampleId.objects.filter(date=today_date).values_list('status', flat=True)

     # data1=SampleId.objects.filter(date=today_date1).values_list('sampleid', flat=True)
     # scheduledate1=SampleId.objects.filter(date=today_date1).values_list('date', flat=True)
     # status1=SampleId.objects.filter(date=today_date1).values_list('status', flat=True)

     # data2=SampleId.objects.filter(date=today_date2).values_list('sampleid', flat=True)
     # scheduledate2=SampleId.objects.filter(date=today_date2).values_list('date', flat=True)
     # status2=SampleId.objects.filter(date=today_date2).values_list('status', flat=True)

     # data3=SampleId.objects.filter(date=today_date3).values_list('sampleid', flat=True)
     # scheduledate3=SampleId.objects.filter(date=today_date3).values_list('date', flat=True)
     # status3=SampleId.objects.filter(date=today_date3).values_list('status', flat=True)

     # data4=SampleId.objects.filter(date=today_date4).values_list('sampleid', flat=True)
     # scheduledate4=SampleId.objects.filter(date=today_date4).values_list('date', flat=True)
     # status4=SampleId.objects.filter(date=today_date4).values_list('status', flat=True)

     # data5=SampleId.objects.filter(date=today_date5).values_list('sampleid', flat=True)
     # scheduledate5=SampleId.objects.filter(date=today_date5).values_list('date', flat=True)
     # status5=SampleId.objects.filter(date=today_date5).values_list('status', flat=True)

     # data6=SampleId.objects.filter(date=today_date6).values_list('sampleid', flat=True)
     # scheduledate6=SampleId.objects.filter(date=today_date6).values_list('date', flat=True)
     # status6=SampleId.objects.filter(date=today_date6).values_list('status', flat=True)

     username = request.POST.get("username")
     today = date.today()
     totalproducts = ProtocolNew.objects.values('protocolid').count()
     totalactivesamples = SampleId.objects.filter(status='Active').count()
     totalelapsedsamples = SampleId.objects.filter(status='Elapsed').count()
     context = {
          "uname": username,
          "todaydate": today,
          "totalproducts": totalproducts,
          "activesamples": totalactivesamples,
          "elapsedsamples":totalelapsedsamples,
          # 'data0': data0,
          # 'data1': data1,
          # 'data2': data2,
          # 'data3': data3,
          # 'data4': data4,
          # 'data5': data5,
          # 'data6': data6,
          # 'scheduledate0': scheduledate0,
          # 'scheduledate1': scheduledate1,
          # 'scheduledate2': scheduledate2,
          # 'scheduledate3': scheduledate3,
          # 'scheduledate4': scheduledate4,
          # 'scheduledate5': scheduledate5,
          # 'scheduledate6': scheduledate6,
     }
     return render(request, 'dashboard.html', context)


def updatesample(request):
     return render(request, 'updatesample.html')