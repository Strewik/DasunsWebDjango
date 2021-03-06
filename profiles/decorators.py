from django.http import HttpResponse
from django.shortcuts import redirect


# This works if you have a separate login and register pages which are not models on the home page
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profiles:homepage')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'admin':
            return redirect('profiles:dashboard')

        if group == 'serviceprovider':
            return redirect('profiles:serviceproviderdash')

        if group == 'serviceuser':
            return redirect('profiles:serviceuserdash')
        
        else:
        #     return view_func(request, *args, **kwargs)
            return HttpResponse(str("You don't belong to any user group yet, Contact admin"))           
    return wrapper_func