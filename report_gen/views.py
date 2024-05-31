from django.shortcuts import render
from django.http import HttpResponse
from .models import ProtocolNew, Testtable3, DateTable
from fpdf import FPDF
from collections import Counter


def genprotocolreport(request):
     pidfromuser = request.POST.get("pid")
     pid = ProtocolNew.objects.get(protocolid=pidfromuser)
     proid = pid.protocolid
     proid = str(proid)
     productname = pid.product_name
     productname = str(productname)
     genericname = pid.generic_name
     genericname = str(genericname)
     formulationtype = pid.formulation_type
     formulationtype = str(formulationtype)
     generalinfo = pid.general_info
     generalinfo = str(generalinfo)
     batchnumber = pid.batch_number
     batchnumber = str(batchnumber)
     batchsize = pid.batch_size
     batchsize = str(batchsize)
     qtysampled = pid.qty_sampled
     qtysampled = str(qtysampled)
     mfgdate = pid.mfg_date
     mfgdate = str(mfgdate)
     expdate = pid.exp_date
     expdate = str(expdate)
     ssdate = pid.study_start_date
     ssdate = str(ssdate)
     specnumber = pid.specification_number
     specnumber = str(specnumber)
     revnumber = pid.revision_number
     revnumber = str(revnumber)
     ccnumber = pid.change_control_number
     ccnumber = str(ccnumber)
     effecdate = pid.effective_date
     effecdate = str(effecdate) 
     dateofrelease = pid.date_of_release
     dateofrelease = str(dateofrelease)
     analysedby = pid.analysed_by
     analysedby = str(analysedby)
     preparedby = pid.prepared_by
     preparedby = str(preparedby)
     checkedby = pid.checked_by
     checkedby = str(checkedby)
     approvedby = pid.approved_by
     approvedby = str(approvedby)

     pidtt3 = Testtable3.objects.filter(protocolid=pidfromuser)

     all_tests = []
     for obj in pidtt3:
          all_tests.append(obj.test)
     # all_tests = str(all_tests)
     totaltests = len(all_tests)

     testdate = DateTable.objects.filter(protocolid=pidfromuser).values_list('date', flat=True)
     testids = DateTable.objects.filter(protocolid=pidfromuser).values_list('testid', flat=True)
     
     # testdate = DateTable.objects.filter(protocolid=pidfromuser)
     # test_dates = []
     # for i in testdate:
          # a=i.get('date')  #using get(), we're getting 2024-05-20 format of date but it's only fetching the last date of the same protocol id 
          # test_dates.append(i.date)  #using array, we're getting the answer in the list or dict form
     # test_dates = str(test_dates)


     final_dates = []
     for date in testdate:
          formatted_date = date.strftime("%Y-%m-%d")
          final_dates.append(formatted_date)
          # print(f"Formatted date: {formatted_date}")
     

     # final_dates = str(final_dates)
     # print(f"Final dates: {final_dates}")

     # for date in testdate:
     #      formatted_date = date.strftime("%Y-%m-%d")
     #      final_dates.append(formatted_date)
     #      print(f"Formatted date: {formatted_date}")



     # pidtt3 = Testtable3.objects.get(protocolid=pidfromuser)
     # frequency = pidtt3.frequency
     # frequency = str(frequency)
     # duration = pidtt3.duration
     # duration = str(duration)


     # if (proid):
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
     #      testname=Testtable3.objects.values('test')
     #      testname=testname.last()
     #      testname=str(testname['test'])
     #      frequency=Testtable3.objects.values('frequency')
     #      frequency=frequency.last()
     #      frequency=str(frequency['frequency'])
     #      duration=Testtable3.objects.values('duration')
     #      duration=duration.last()
     #      duration=str(duration['duration'])
     # protocolidpdf=ProtocolNew.objects.values('protocolid')
     # protocolidpdf=protocolidpdf.last()
     # protocolidpdf=str(protocolidpdf['protocolid'])


     class PDF(FPDF):
          def header(self):
               # Rendering logo:
               self.image(".\protocol\stabicarelims.png", 10, 8, 33)
               # self.code39("*stb*", x=150, y=8)
               # Setting font: helvetica bold 15
               self.set_font("helvetica", "B", 20)
               
               # Moving cursor to the right:
               self.cell(80)
               # Printing title:
               self.cell(30, 10, "Protocol Report",align="C")
               # Performing a line break:
               self.ln(20)

          def footer(self):
               # Position cursor at 1.5 cm from bottom:
               self.set_y(-15)
               # Setting font: helvetica italic 8
               self.set_font("helvetica", "I", 8)
               # Printing page number:
               self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")
     
# -------------------------------------------------------------------------- Way 1    

     # TABLE_DATA = (
     # ("Protocol ID", "Product Name", "Formulation Type", "Test"),
     # (proid, productname, formulationtype, all_tests),
     # )
     pdf = PDF(orientation='L')
     pdf.add_page()
     pdf.set_font("Times", size=12)
     # with pdf.table(text_align="CENTER") as table:
     #      for data_row in TABLE_DATA:
     #           row = table.row()
     #           for datum in data_row:
     #                row.cell(datum)
     
     # pdf.ln()

# -------------------------------------------------------------------------- Way 2
     rows = DateTable.objects.filter(protocolid=pidfromuser).values('date').count()
     rows=str(rows)
     i=0
     j = 1
     j = str(j)
     # pdf.write_html("""
     html_table = """
     <table border="1">
          <tr>
               <th align="left">Protocol ID :</th>
               <td>""" + proid + """</td>
               <th align="left">Study Start Date :</th>
               <td>""" + ssdate + """</td>
          </tr>
     </table>
     <table border="1">
          <tr>
               <th align="left">Protocol Name :</th>
               <td>""" + productname + """</td>
               <th align="left">Specification Number :</th>
               <td>""" + specnumber + """</td>  
          </tr>
     </table>
     <table border="1">
          <tr>
               <th align="left">Generic Name :</th>
               <td>""" + genericname + """</td>
               <th align="left">Revision Number :</th>
               <td>""" + revnumber + """</td>   
          </tr>
     </table>
     <table border="1">
          <tr>
               <th align="left">Formulation Type :</th>
               <td>""" + formulationtype + """</td>
               <th align="left">Change Control Number :</th>
               <td>""" + ccnumber + """</td> 
          </tr>
     </table>
     <table border="1">
          <tr>
               <th align="left">General Information :</th>
               <td>""" + generalinfo + """</td>
               <th align="left">Effective Date :</th>
               <td>""" + effecdate + """</td>
          </tr>
     </table>
     <table border="1">
          <tr>
               <th align="left">Batch No. :</th>
               <td>""" + batchnumber + """</td>
               <th align="left">Date of Release :</th>
               <td>""" + dateofrelease + """</td>    
          </tr>
     </table>
     <table border="1">
          <tr>
               <th align="left">Batch Size :</th>
               <td>""" + batchsize + """</td>
               <th align="left">Analysed By :</th>
               <td>""" + analysedby + """</td>    
          </tr>
     </table>
     <table border="1">
          <tr>
               <th align="left">Quantity Sampled :</th>
               <td>""" + qtysampled + """</td>
               <th align="left">Prepared By :</th>
               <td>""" + preparedby + """</td>     
          </tr>
     </table>
     <table border="1">
          <tr>
               <th align="left">Manufacturing Date :</th>
               <td>""" + mfgdate + """</td>
               <th align="left">Checked By :</th>
               <td>""" + checkedby + """</td> 
          </tr>
     </table>
     <table border="1">
          <tr>
               <th align="left">Expiry Date :</th>
               <td>""" + expdate + """</td>
               <th align="left">Approved By :</th>
               <td>""" + approvedby + """</td>
          </tr>
     </table>"""
     pdf.write_html(html_table)

     html_table = """
     <table><tr><td></td></tr><tr><td></td></tr></table>"""
     pdf.write_html(html_table)

     
     testid_counts = Counter(testids)
     html_table = """
     <table border="1">
          <tr>
               <th>Test</th>
               <th>Sample No.</th>
               <th>Pullout Date</th>
          </tr>
          <tr align="center">
               <td>"""
               
     k = 0
     l = 0
     totaldates = len(final_dates)
     for id, count in testid_counts.items():
          i = 0
          j = 0
          sample = 1
          length=1
          print(f"id: {id}, count: {count}")
          if (totaltests > 1):
               while (i < 1):
                    html_table += all_tests[k] + """</td><td>""" 
                    while (j < count):
                         html_table += str(sample) + """</td><td>"""
                         html_table += final_dates[l] + """ </td></tr>"""
                         sample = sample + 1
                         l += 1
                         j += 1 
                         if (length < count):
                              html_table += """<tr align="center"><td></td><td>"""
                              length += 1
                    k += 1
                    i += 1
               html_table += """</table>"""
               if (l < totaldates):
                    html_table += """<table border="1"><tr align="center"><td>"""   
          elif(totaltests == 1):
               while (i < 1):
                    html_table += all_tests[k] + """</td><td>""" 
                    while (j < count):
                         html_table += str(sample) + """</td><td>"""
                         html_table += final_dates[l] + """ </td></tr>"""
                         sample = sample + 1
                         l += 1
                         j += 1 
                         if (length < count):
                              html_table += """<tr align="center"><td></td><td>"""
                              length += 1
                    k += 1
                    i += 1
               html_table += """</table>"""
               # html_table += """<tr align="center"><td>"""
               # html_table += """<table border="1"><tr align="center"><td>"""
                    
     # html_table += """</td><td></td><td></td></tr></table>"""

     # sample = 1
     # # for id in testids:
     # # for tid, count in testid_counts.items():
     # #      print(tid)
     # for test in all_tests:
     #      print(test)
     #      # length = len(all_tests)
     #      html_table += test + """</td><td>"""              
     #      for obj in final_dates:
     #           length = len(final_dates)
     #           html_table += str(sample) + """</td><td>"""
     #           html_table += obj + """ </td></tr>"""
     #           sample = sample + 1
     #           i = i + 1
     #           if (i < length-3):
     #                # if final_dates[i]:
     #                html_table += """<tr align="center"><td></td><td>"""
     # html_table += """</table>"""
     pdf.write_html(html_table)
     
# -------------------------------------------------------------------------- Way 4  

     # sample = str(1)
     # i = 1
     # # i = str(i)
     # html_table = """
     # <table border="1">
     #      <tr>
     #           <th>Test</th>
     #           <th>Sample No.</th>
     #           <th>Pullout Date</th>
     #      </tr>
     #      <tr align="center">
     #           <td>""" + all_tests + """ </td>
     #           <td>""" + sample + """ </td>
     #           <td>"""
     # for obj in final_dates:
     #      length = len(final_dates)
     #      # length = str(length)
     #      html_table += obj + """ </td></tr>"""
     #      while i<length:
     #           if final_dates[i]:
     #                html_table += """<tr align="center"><td></td><td></td><td>"""
     #           i = i + 1
     # html_table += """</table>"""
     # pdf.write_html(html_table)


     # print(f"Final dates before loop: {final_dates}")
     # for formatted_date in final_dates:
     #      html_table += ("</td></tr>" + formatted_date + "<tr><td>")
     # html_table += """</table>"""
     # pdf.write_html(html_table)



  
     
















     # pdf.code39("stabicare", x=30, y=50, w=4, h=20)
     # pdf.set_font('helvetica', size=12)
     # pdf.set_font("helvetica", 'B', 12)
     # pdf.cell(50, 5, txt='Protocol ID : ', align="L")
     # pdf.cell(50, 5, txt=proid, ln=1, align="L")
     # # # pdf.ln()

     # # # pdf.set_font(style='B')
     # pdf.cell(50, 5, txt='Product Name : ', align="L")
     # pdf.cell(50, 5, txt=productname, ln=1, align="L")
     # # # pdf.ln()

     # # # pdf.set_font(style='B')
     # pdf.cell(50, 5, txt='Generic Name : ', align="L")
     # pdf.cell(50, 5, txt=genericname, ln=1, align="L")
     # # # pdf.ln()

     # pdf.cell(50, 5, txt='General Info : ', align="L")
     # pdf.cell(50, 5, txt=generalinfo, ln=1, align="L")
     # # # pdf.ln()

     # pdf.cell(50, 5, txt='Formulation Type : ', align="L")
     # pdf.cell(50, 5, txt=formulationtype, ln=1, align="L")
     # # # pdf.ln()

     # pdf.cell(50, 5, txt='Batch Number : ', align="L")
     # pdf.cell(50, 5, txt=batchnumber, ln=1, align="L")
     # # # pdf.ln()

     # pdf.cell(50, 5, txt='Batch Size : ', align="L")
     # pdf.cell(50, 5, txt=batchsize, ln=1, align="L")
     # # # pdf.ln()

     # pdf.cell(50, 5, txt='QTY Sampled : ', align="L")
     # pdf.cell(50, 5, txt=qtysampled, ln=1, align="L")
     # # # pdf.ln()

     # pdf.cell(50, 5, txt='MFG Date : ', align="L")
     # pdf.cell(50, 5, txt=mfgdate, ln=1, align="L")

     # pdf.cell(50, 5, txt='Test : ', align="L")
     # pdf.cell(50, 5, txt=all_tests, ln=1, align="L")

     
     # pdf.cell(50, 5, txt="Test Date : ", align='L')
     # pdf.cell(50, 5, txt=test_dates, ln=1, align="L")

     # pdf.cell(50, 5, txt='Frequency : ', align="L")
     # pdf.cell(50, 5, txt=frequency, ln=1, align="L")

     # pdf.cell(50, 5, txt='Duration : ', align="L")
     # pdf.cell(50, 5, txt=duration, ln=1, align="L")

     pdf.output("report.pdf")
     pdf_data = pdf.output()

     print("PDF generated successfully: report.pdf")
     # print("testids=", testids)
     # print("Occurences of particular testids=", testid_counts)
     # print("Formatted Dates=", formatted_date)
     # print("a=", a)
     # print("b=", b)
     # return HttpResponse(bytes(pdf.output()), content_type="application/pdf")
     return HttpResponse(pdf_data, content_type="application/pdf")
     # else:
     #    print("The searched Product id is not in the database!")
     #    msg = "The searched Product id is not in the database!"
     #    context={
     #         'errormsg': msg,
     #    }
     # return HttpResponse("The searched Product id is not in the database!")
     # return render(request, 'Reportgeneration.html')
     # return HttpResponse("Done")





def reportgeneration(request):
     return render(request, 'Reportgeneration.html')
