from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('faq/', views.faq, name="faq"),
    path('advantages/', views.advantages, name="advantages"),
    path('development/', views.development, name="development"),
    path('blogvhub/', views.blogvhub, name="blogvhub"),
    path('customer/', views.customer, name="customer"),
    path('design/', views.design, name="design"),
    path('oportunity/', views.oportunity, name="oportunity"),
    path('purpose/', views.purpose, name="purpose"),
    path('ad/', views.ad, name="ad"),
    path('conversion/', views.conversion, name="conversion"),
    path('long-short/', views.long_short, name="long-short"),
    path('sales-funel/', views.sales_funel, name="sales-funel"),
    path('seo/', views.seo, name="seo"),
    path('content/', views.content, name="content"),
    path('curtain/', views.curtain, name="curtain"),
    path('deviance/', views.deviance, name="deviance"),
    path('organization/', views.organization, name="organization"),
    path('ranking/', views.ranking, name="ranking"),
    path('research/', views.research, name="research"),
]
