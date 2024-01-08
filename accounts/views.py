from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from foods.models import Food
from django.contrib import messages
from .decorator import unauthenticated_user
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

@unauthenticated_user
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page or view
            return redirect('home')
        else:
            context = {
                'username': username,
                'password': password,
                'error': 'ឈ្មោះអ្នកប្រើប្រាស់ឬលេខសម្ងាត់មិនត្រឹមត្រូវ'
            }
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@unauthenticated_user
def Register(request):
    username = email = password = first_name = last_name = error_message = ""
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']

        print(username)
        print(email)
        print(password)
        print(first_name)
        print(last_name)
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            login(request, user)
            return redirect('home')
        except:
            if User.objects.filter(username=username).exclude(id=request.user.id).exists():
                error_message = 'ឈ្មោះអ្នកប្រើប្រាស់នេះត្រូវបានប្រើជាមួយគណនីផ្សេងរួចហើយ'
            if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                error_message = 'អ៊ីម៉ែលនេះត្រូវបានប្រើជាមួយគណនីផ្សេងរួចហើយ'
            context = {
                'error': error_message,
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'email': email,
                'password': password
            }
            return render(request, 'accounts/register.html', context)
    else:
        return render(request, 'accounts/register.html')

@login_required
def Dashboard(request):
    if request.method == 'POST':
        if not request.user.is_superuser:
            return render(request, 'accounts/dashboard.html', { 'error': 'អ្នកពុំមានសិទ្ធក្នុងការបន្ថែមនោះទេ' })
        # Get data from the HTML form
        title = request.POST.get('food_title')
        price = int(request.POST.get('food_price'))
        category = request.POST.get('food_category') 
        special_price = request.POST.get('food_special_price', None)
        promotion_end_at = request.POST.get('food_end_promotion', None) 
        description = request.POST.get('food_desc')
        image_relative_url = request.POST.get('food_image')
        # Create the Food object
        try:
            kwargs = {
                'title': title,
                'price': price,
                'category': category,
                'description': description,
                'image_relative_url': image_relative_url
            }
            if special_price:
                kwargs['special_price'] = special_price
            if promotion_end_at:
                kwargs['promotion_end_at'] = promotion_end_at
            Food.objects.create(**kwargs)
            
            messages.success(request, "បានបន្ថែមមុខម្ហូបថ្មីបានដោយជោគជ័យ")

            return redirect('dashboard')
        except Exception as e:
            context = {
                'title': title,
                'price': price,
                'category': category,
                'description': description,
                'promotion_end_at': promotion_end_at,
                'special_price': special_price,
                'image_relative_url': image_relative_url,
                'error': 'ការបន្ថែមមុខម្ហូបថ្មីបានបរាជ័យ'
            }
            return render(request, 'accounts/dashboard.html', context)

    else:
        # Render the form template (if GET request)
        return render(request, 'accounts/dashboard.html')

@login_required
def UpdateProfile(request):
    if request.method == 'POST':
        # Get the updated information from the form
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exclude(id=request.user.id).exists():
            # Handle the case where the username is already taken
            context = {'error': 'ឈ្មោះអ្នកប្រើប្រាស់នេះត្រូវបានប្រើជាមួយគណនីផ្សេងរួចហើយ'}  # Pass an error message to the template
            return render(request, 'accounts/update_profile.html', context)
        if User.objects.filter(email=email).exclude(id=request.user.id).exists():
            context = {'error': 'អ៊ីម៉ែលនេះត្រូវបានប្រើជាមួយគណនីផ្សេងរួចហើយ'}
            return render(request, 'accounts/update_profile.html', context)
        # Update the user's information
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.username = username
        request.user.email = email
        request.user.save()
        messages.success(request, "ការធ្វើបច្ចុប្បន្នភាពព័ត៍មានគណនីបានសម្រេច")

        return redirect('update_profile')
    else:
        return render(request, "accounts/update_profile.html")

@login_required
def ChangePassword(request):
    if request.method == 'POST':
        old_password = request.POST.get('old-password')
        new_password = request.POST.get('new-password-1')
        confirm_password = request.POST.get('new-password-2')

        user = request.user

        # Check if the old password is correct
        if not user.check_password(old_password):
            # Handle incorrect old password (e.g., display an error message)
            context = {'error': 'Incorrect old password.'}
            return render(request, 'accounts/change_password.html', context)

        # Check if the new passwords match
        if new_password != confirm_password:
            # Handle mismatched new passwords (e.g., display an error message)
            context = {'error': 'New passwords do not match.'}
            return render(request, 'accounts/change_password.html', context)
        
        # Set the new password
        user.set_password(new_password)
        user.save()

        # Update the session to avoid logging out the user
        update_session_auth_hash(request, user)

        # Redirect to a success page or display a success message
        return redirect('dashboard')

    else:
        # GET request: Render the password change form
        return render(request, "accounts/change_password.html")