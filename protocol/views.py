from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def formulationpage(request):
    return render(request, "formulationpage.html")
    # return HttpResponse('This is the formulation page.')


def tabletspage(request):
    if request.method=='POST':
        ginfo = request.POST.get('ginfo')
        # product = request.POST['product']
        # gname = request.POST['gname']
        formtype = request.POST.get('formtype')
        # specificno = request.POST['specificno']
        # revno = request.POST['revno']
        # batchno = request.POST['batchno']
        # batchsize = request.POST['batchsize']
        # mandate = request.POST['mandate']
        # exdate = request.POST['exdate']
        # controlno = request.POST['controlno']
        # efdate = request.POST['efdate']
        # qtysampled = request.POST['qtysampled']
        # reldate = request.POST['reldate']
        # analysedby = request.POST['analysedby']
        # checkedby = request.POST['checkedby']
        # preparedby = request.POST['preparedby']
        # approvedby = request.POST['approvedby']
        # print(ginfo, product, gname, formtype, specificno, revno, batchno, batchsize, mandate, exdate, controlno, efdate, qtysampled, reldate, analysedby, checkedby, preparedby, approvedby)
        print(ginfo, formtype)
        print("This is tabletspage")
    return render(request, "tabletspage.html")


def hardcapsulespage(request):
    if request.method=='GET':
        print("This is hardpage")
    return render(request, "hardcapsulespage.html")


def softcapsulespage(request):
    return render(request, "softcapsulespage.html")

def frequencypage(request):
    # if request.method=='POST':
    #     ginfo = request.POST['ginfo']
    #     product = request.POST['product']
    #     gname = request.POST['gname']
    #     formtype = request.POST['formtype']
    #     specificno = request.POST['specificno']
    #     revno = request.POST['revno']
    #     batchno = request.POST['batchno']
    #     batchsize = request.POST['batchsize']
    #     mandate = request.POST['mandate']
    #     exdate = request.POST['exdate']
    #     controlno = request.POST['controlno']
    #     efdate = request.POST['efdate']
    #     qtysampled = request.POST['qtysampled']
    #     reldate = request.POST['reldate']
    #     analysedby = request.POST['analysedby']
    #     checkedby = request.POST['checkedby']
    #     preparedby = request.POST['preparedby']
    #     approvedby = request.POST['approvedby']
    #     print(ginfo, product, gname, formtype, specificno, revno, batchno, batchsize, mandate, exdate, controlno, efdate, qtysampled, reldate, analysedby, checkedby, preparedby, approvedby)
        # print("This is post")
    return render(request, "frequencypage.html")

