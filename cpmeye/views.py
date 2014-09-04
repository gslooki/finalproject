from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    return HttpResponse("this be da index page")
def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render_to_response(
            'cpmeye/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)


def login(request):
    u = request.POST['username']
    p = request.POST['password']
    user = authenticate(username=u, password=p)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            return HttpResponse("invalid")
    else:
       return HttpResponse("valid")
def logout(request):
    logout(request)
    return HttpResponseRedirect('/cpmeye/')
    
