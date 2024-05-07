from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
# main landing page
def landing(request):
    return render(request,'app1/landing.html')	
	
#sign-up page
def Sign_up(request):
    if request.method=='POST':
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()# save the data in the databse
            return redirect('login')# redirect the new user to login page
        else:
            return render(request,'app1/index.html',{'form':form, 'error_message': form.errors.get('__all__')})
    else:
        form=UserCreationForm()
    return render(request,'app1/index.html',{'form':form})

#login page
def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']# take username from the submitted form
            password = form.cleaned_data['password']#take password from the submitted form
            print(username,password)
            user = authenticate(request, username=username, password=password) # check wether the data taken is correct or not, If the user with the details exist then it will have the user object else None
            print("hello",user.get_username())
            if user is not None:     #if the user exist then
                login(request, user)  # login the user
                # Redirect to a success page after login
                return redirect('success_page')  # Replace 'success_page' with the URL name of the success page,for now this page does not exist
        # If authentication fails or form is invalid, render the form with error message
        return render(request, 'app1/index.html', {'form': form, 'error_message': form.errors.get('__all__')})
    else:
        form = AuthenticationForm()
    return render(request, 'app1/index.html', {'form': form})
