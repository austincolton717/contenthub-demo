from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def faq(request):
    return render(request, 'faq.html', {})


def advantages(request):
    return render(request, 'development/advantages.html', {})


def development(request):
    return render(request, 'development/development.html', {})


def blogvhub(request):
    return render(request, 'development/blogvhub.html', {})


def customer(request):
    return render(request, 'development/customer.html', {})


def design(request):
    return render(request, 'development/design.html', {})


def oportunity(request):
    return render(request, 'development/oportunity.html', {})


def purpose(request):
    return render(request, 'development/purpose.html', {})


def ad(request):
    return render(request, 'marketing/ad.html', {})


def conversion(request):
    return render(request, 'marketing/conversion.html', {})


def long_short(request):
    return render(request, 'marketing/longterm-v-shortterm.html', {})


def sales_funel(request):
    return render(request, 'marketing/sales-funel.html', {})


def seo(request):
    return render(request, 'marketing/seo.html', {})


def content(request):
    return render(request, 'power/content.html', {})


def curtain(request):
    return render(request, 'power/curtain.html', {})


def deviance(request):
    return render(request, 'power/deviance.html', {})


def organization(request):
    return render(request, 'power/organization.html', {})


def ranking(request):
    return render(request, 'power/ranking.html', {})


def research(request):
    return render(request, 'power/research.html', {})


# Create your views here.
