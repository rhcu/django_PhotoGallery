from django.shortcuts import render, redirect
from .models import Photo
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
class PhotoView(generic.ListView):
    template_name = 'photo.html'
    context_object_name = 'photo_list'
    def get_queryset(self):
        return Photo.objects.all()
    def search_list(request):
        query = request.GET.get("q")
        return Photo.objects.all().filter(title__icontanes=query)
        

class DetailView(generic.DetailView):
    model = Photo
    template_name = 'detail.html'
    
    
class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'
    # blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    # process form 
    def post(self, request):
        form = self.form_class(request.POST)    
        
        if form.is_valid():
            user = form.save(commit = False)
            
            #cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            #save User to database
            user.save()
            
            # returns User if correct
            user = authenticate(username = username, password = password) 
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('photo_list')
                    
        return render(request, self.template_name, {'form': form})

	
	
class PhotoCreate(CreateView):
    template_name = 'photo_form.html'
    model = Photo
    fields = ['title', 'width', 'height', 'image']
    
class PhotoDelete(DeleteView):
    model = Photo 
    success_url = reverse_lazy('photo_list')

class PhotoUpdate(UpdateView):
    template_name = 'photo_form.html'
    model = Photo
    fields = ['title', 'width', 'height', 'image']
    
