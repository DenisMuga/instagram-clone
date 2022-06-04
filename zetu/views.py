from django.shortcuts import render,redirect,get_list_or_404

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            f_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=f_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegForm()
    return render(request, 'registration/signup.html', {'form': form})