from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import SignUpForm , AddRecordForm
from .models import Record , Item



# Create your views here.

def home(request):

    records=Record.objects.all()
    #Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request , username=username , password = password)
        if user is not None:
            login(request , user)
            messages.success(request , "You have been logged in")
            return redirect('home')
        else:
            messages.error(request , "There was an error logging in")
            return redirect('home')
        
    else:
        # if they are not posting the form , means they already logged in
        return render(request , 'home.html' , {'records' : records})
    
def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username , password = password)

            login(request , user)
            messages.success (request , "You have successfully registered  ")
            return redirect('home')
        
    else:
        form = SignUpForm()
        return render(request , 'register.html' , {'form': form})
    
    return render(request, 'register.html', {'form':form})


def customer_record(request , pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record}) 
    else:
        messages.success(request, "logged in and viewing the page")
        return redirect('home')
    


def delete_record(request , pk):
    if request.user.is_authenticated:
        delete_c = Record.objects.get(id=pk)
        delete_c.delete()
        messages.success(request, "Records deleted successfully.")
        return redirect('home')
    else:
        messages.error("you need to log in to delete record")
        return redirect('home')
    

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added")
                return redirect('home')
        return render(request , 'add_record.html' , {'form':form})
    else:
        messages.error(request, "you must logged in to add record.")
        return redirect('home')
    

def update_record(request , pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been updated!")
            return redirect('home')
        return render(request, 'update_record.html' , {'form':form})
    else:
        messages.success(request,"You must be logged in.")
        return redirect('home')
    
def show_record_info(request , pk):
     if request.user.is_authenticated:
        customer_info = Record.objects.get(id=pk)
        return render(request, 'info.html', {'customer_info':customer_info})
     else:
        messages.success(request, "logged in and viewing the page")
        return redirect('home')
     

     
def give_items(request,pk):
    if request.user.is_authenticated:
        giver = Record.objects.get(id=pk)

        if request.method == "POST":
            item_id=request.POST.get("item_id")
            available_customers = Record.objects.exclude(id=giver.id)
            return render(request, 'give_items.html' , {'available_customers':available_customers, "item_id":item_id})
        
    return redirect("home")

def process_give(request):
    if request.user.is_authenticated and request.method == "POST":
        recipient_id = request.POST.get("recipient_id")
        item_id = request.POST.get("item_id")

        if recipient_id and item_id:
            recipient = Record.objects.get(id=recipient_id)
            item = Item.objects.get(id=item_id)
            item.record = recipient
            item.save()

        messages.success(request, "Item successfully given!")
        return redirect("home")

    return redirect("home")
            
            


       
    


    
