from django.shortcuts import render
from testapp.forms import StudentForm
# Create your views here.
def studentinput_view(req):
    submitted = False
    name = ''
    if req.method == 'POST':
        form = StudentForm(req.POST)
        if form.is_valid():
            print('Form Validation is Successful and Print Data')
            print('Roll No:',form.cleaned_data['rollno'])
            print('Name:',form.cleaned_data['name'])
            print('Marks:',form.cleaned_data['marks'])
            name = form.cleaned_data['name']
            submitted = True
    form = StudentForm()
    my_dict = {'form': form,'submitted':submitted,'name':name}
    return render(req,'testapp/input.html',my_dict)