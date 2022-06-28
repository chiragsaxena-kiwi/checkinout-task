from django.shortcuts import render,redirect
from .models import Signup
from django.core.mail import send_mail
from django.views import View
from django.contrib.auth import get_user_model

USER = get_user_model()


# def signup(request):
#     if request.method == 'POST':
#         # Get form values
#         username = request.POST['Username']
#         email = request.POST['email']
#         password = request.POST['password']
#         dob=request.POST.get('dob')
#         user = Signup(username=username, password=password,email=email,dob=dob)
#         mydict={'username':username}
#         user.save()

#         send_mail(
#              'Congratulations Mail',
#             'Your are successfully checkin',
#             'chiragsaxena001@gmail.com',
#             ['chiragsaxena001@gmail.com'],
#             fail_silently=False,
#         )
    
#         return redirect('checkin')
#     else:
#         return render(request, 'signup.html')


class  signupView(View):
 def get(self,request):    
    if request.method == 'POST':
        # Get form values
        username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        dob=request.POST.get('dob')
        user = USER(username=username, password=password,email=email,dob=dob)
        mydict={'username':username}
        user.save()

        send_mail(
             'Congratulations Mail',
            'Your are successfully checkin',
            'chiragsaxena001@gmail.com',
            ['chiragsaxena001@gmail.com'],
            fail_silently=False,
        )
    
        return redirect('checkin')
    else:
        return render(request, 'signup.html')    
       
# def checkin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email=request.POST['email']
#         password = request.POST['password']
       
       
#         try:
#             d1 = Signup.objects.get(username=username, password=password,)
#         except Signup.DoesNotExist:
#             return render(request, 'checkin.html')
#         else:
#             request.session['uid'] = d1.id
        
#         return redirect("profile")
#     else:
#         return render(request, 'checkin.html')    


class checkinView(View):
 def get(self,request): 
    if request.method == 'POST':
        username = request.POST['username']
        email=request.POST['email']
        password = request.POST['password']
       
       
        try:
            d1 = Signup.objects.get(username=username, password=password,)
        except Signup.DoesNotExist:
            return render(request, 'checkin.html')
        else:
            request.session['uid'] = d1.id
        
        return redirect("profile")
    else:
        return render(request, 'checkin.html')    



# def profile(request):
#     users=Signup.objects.all()
#     return render(request, 'profile.html', {'users':users})     
    


class profileView(View):
 def get(self,request): 
          users=Signup.objects.all()
          return render(request, 'profile.html', {'users':users})     
    


def checkout(request):
    return render(request,'logout.html')  