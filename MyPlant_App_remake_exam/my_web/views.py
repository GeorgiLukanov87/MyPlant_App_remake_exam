from django.shortcuts import render, redirect

from MyPlant_App_remake_exam.my_web.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm, PlantCreateForm, \
    PlantDeleteForm, PlantEditForm
from MyPlant_App_remake_exam.my_web.models import Plant, Profile


def get_profile():
    return Profile.objects.first()


def index(request):
    return render(request, 'common/home-page.html')


def catalogue(request):
    plants = Plant.objects.all()
    context = {'plants': plants, }
    return render(request, 'common/catalogue.html', context, )


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, }

    return render(request, 'profile/create-profile.html', context, )


def details_profile(request):
    plants = Plant.objects.all()
    profile = get_profile()

    context = {'plants': plants, 'profile': profile, }

    return render(request, 'profile/profile-details.html', context, )


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details-profile')

    context = {'form': form, 'profile': profile, }

    return render(request, 'profile/edit-profile.html', context, )


def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, 'profile': get_profile()}

    return render(request, 'profile/delete-profile.html', context, )


def create_plant(request):
    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form, }

    return render(request, 'plant/create-plant.html', context, )


def edit_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'plant': plant, 'form': form, }

    return render(request, 'plant/edit-plant.html', context, )


def delete_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form, 'plant': plant, }

    return render(request, 'plant/delete-plant.html', context, )


def details_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    context = {'plant': plant, }
    return render(request, 'plant/plant-details.html', context, )
