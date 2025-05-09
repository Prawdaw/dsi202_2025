# Create your views here.
from django.shortcuts import render

def home_page(request):
    return render(request, 'index.html')  # You’ll create this template

#from django.views.generic import ListView
#from .models import Outfit
#from django.db.models import Q

#class OutfitListView(ListView):
#    model = Outfit
#    template_name = 'outfit_list.html'
#    context_object_name = 'outfits'

#    def get_queryset(self):
#        query = self.request.GET.get('q')
#        if query:
#            return Outfit.objects.filter(
#                Q(name__icontains=query) | Q(style__icontains=query)
#            )
#        return Outfit.objects.all()

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['search_query'] = self.request.GET.get('q', '')
#        return context

#from django.views.generic import DetailView

#class OutfitDetailView(DetailView):
    #model = Outfit
    #template_name = 'outfit_detail.html'
    #context_object_name = 'outfit'


from django.shortcuts import render

def matching_outfit_view(request):
    return render(request, 'matching.html')

def content_page(request):
    return render(request, 'content.html')

def community_page(request):
    return render(request, 'community.html') 

from django.shortcuts import render

def custom_page(request):
    return render(request, 'custom.html')

def shop_detail_page(request):
    return render(request, 'shop-detail.html')

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')

from django.shortcuts import render

def custom_page(request):
    if request.method == 'POST':
        # handle form
        ...
    return render(request, 'custom.html')