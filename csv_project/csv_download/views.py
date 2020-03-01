from django.shortcuts import render
from django.http import HttpResponse
import csv, io
from django.contrib import messages
from .models import Titanic



# Create your views here.
def index(request):
    return render(request,'csv_download/index.html')



def download(request):
    file_name = (request.POST.get('file_name')).split(':')
    items = Titanic.objects.all()[int(file_name[0]):int(file_name[1])]

    columns_name = request.POST.getlist('columns_name')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="titanic.csv"'

    writer = csv.writer(response,delimiter=',')
    writer.writerow(columns_name)

    flag =0
    for obj in items:
        dict_temp = {'passid':obj.passid, 'survived':obj.survived, 'pclass':obj.pclass, 'name':obj.name,'age':obj.age,'sibsp':obj.sibsp,'parch':obj.parch,'ticket':obj.ticket,'fare':obj.fare,'embarked':obj.embarked}
        clms = []
        for column in columns_name:
            if column in dict_temp:
                clms.append(dict_temp[column])
        writer.writerow(clms)

    return response



def upload(request):

    data = Titanic.objects.all()
    # prompt is a context variable that can have different values depending on their context
    prompt = {
        'order': 'Order of the CSV should be passid, survived, pclass, name,age,sibsp,parch,ticket,fare,embarked',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, 'csv_download/upload.html', prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Titanic.objects.update_or_create(passid=column[0],
                    survived=column[1],
                    pclass=column[2],
                    name=column[3],
                    age=column[4],
                    sibsp=column[5],
                    parch=column[6],
                    ticket=column[7],
                    fare=column[8],
                    embarked=column[9],
                    )
    context = {}

    return render(request,'csv_download/upload.html',context)
