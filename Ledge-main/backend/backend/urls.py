"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

# REST framework urls 
urlpatterns +=[
    path('api/User/', include('User.api.urls', 'user_api')),
    path('api/Account/', include('Account.api.urls', 'account_api')),
    path('api/Transaction/', include('Transaction.api.urls', 'transaction_api')),
    path('api/Category/', include('Category.api.urls', 'category_api')),
    path('api/Budget/', include('Budget.api.urls', 'budget_api')),  
    path('api/currency/', include('currency.api.urls', 'currency_api')),  
]
