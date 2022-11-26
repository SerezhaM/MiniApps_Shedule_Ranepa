import time

from django.shortcuts import render, HttpResponseRedirect, reverse

from .forms import *
from .python.main import *

table_html = ''

# Create your views here.
def index(request):
    global table_html

    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            info_form = request.POST
            kurs = info_form['kurs']
            group = info_form['group']

            table_html = sender(kurs, group)
            # form.save()
            return HttpResponseRedirect(reverse('table'))
    else:
        context = {'form': form}
        return render(request, 'main/index.html', context)

def sender(kurs, group):
    print(kurs)
    print(group)

    return start_py(kurs, group)

def table(request):
    global table_html
    table = table_html
    # time.sleep(2)
    return render(request, 'main/table.html', {'table': table})