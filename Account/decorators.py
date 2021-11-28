from django.http import HttpResponse
from django.shortcuts import redirect, render

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles= []):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None

            # to check if th egroup indicated exists and 
            # consequently allow the users with the specified roles to view the pages
            
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                #return render(request, 'Company/login.html')
                return HttpResponse('You are not authorised to view this page')

            #return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator

def admins_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group =='farmer':
            return redirect('farmer-page')

        if group == 'admin':
            return view_func(request, *args, **kwargs)
        
        if group == 'staff':
            return view_func(request, *args, **kwargs)

    return wrapper_function