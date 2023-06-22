from django.shortcuts import render


def index(request):
    return render(request, 'common/home-page.html')


def catalogue(request):
    return render(request, 'common/catalogue.html')


def create_plant(request):
    return render(request, 'plant/create-plant.html')


def edit_plant(request, pk):
    return render(request, 'plant/edit-plant.html')


def delete_plant(request, pk):
    return render(request, 'plant/delete-plant.html')


def details_plant(request, pk):
    return render(request, 'plant/plant-details.html')


def create_profile(request):
    return render(request, 'profile/create-profile.html')


def edit_profile(request):
    return render(request, 'profile/edit-profile.html')


def delete_profile(request):
    return render(request, 'profile/delete-profile.html')


def details_profile(request):
    return render(request, 'profile/profile-details.html')
