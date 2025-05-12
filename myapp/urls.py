
from django.urls import path
from .views import home_page, matching_outfit_view, content_page,community_page, custom_page, shop_detail_page, login_page, signup_page
from django.conf import settings
from django.conf.urls.static import static
import os
from django.urls import path, include

urlpatterns = [
    path('', home_page, name='home'),
    path('index.html', home_page, name='home'),
    #path('outfits/', OutfitListView.as_view(), name='outfit-list'),
    #path('outfit/<int:pk>/', OutfitDetailView.as_view(), name='outfit-detail'),
    path('matching.html', matching_outfit_view, name='matching-page'),
    path('content.html', content_page, name='content'),
    path('community.html', community_page, name='community-page'),
    path('custom.html', custom_page, name='custom-page'),
    path('shop-detail.html', shop_detail_page, name='shopdetial-page'),
    path('login.html', login_page, name='login-page'),
    path('signup.html', signup_page, name='signup-page'),
    path('accounts/', include('allauth.urls')), # new
    path('', home_page, name='home'), #new
] + static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'myapp', 'static'))
