"""UnicornAttractor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from cart import urls as urls_cart
from accounts import urls as urls_accounts
from checkout import urls as urls_checkout
from bugs import urls as urls_bugs
from features import urls as urls_features
from bugs.views import all_bugs
from django.views import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_bugs, name='index'),
    url(r'^cart/', include(urls_cart)),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^features/', include(urls_features)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^bugs/', include(urls_bugs)),
]
