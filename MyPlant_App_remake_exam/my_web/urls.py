from django.urls import path, include

from MyPlant_App_remake_exam.my_web.views import index, catalogue, create_plant, edit_plant, delete_plant, \
    details_plant, create_profile, edit_profile, delete_profile, details_profile

urlpatterns = (
    path('', include([
        path('', index, name='index'),
        path('catalogue/', catalogue, name='catalogue'),
    ])),

    path('create/', create_plant, name='create-plant'),

    path('edit/<int:pk>/', edit_plant, name='edit-plant'),
    path('delete/<int:pk>/', delete_plant, name='delete-plant'),
    path('details/<int:pk>/', details_plant, name='details-plant'),

    path('profile/', include([
        path('create/', create_profile, name='create-profile'),
        path('edit/', edit_profile, name='edit-profile'),
        path('delete/', delete_profile, name='delete-profile'),
        path('details/', details_profile, name='details-profile'),
    ]))
)

"""
http://localhost:8000/ - home page
http://localhost:8000/catalogue/ - catalogue

http://localhost:8000/create/ - plant create page

http://localhost:8000/details/1/ - plant details page
http://localhost:8000/edit/1/ - plant edit page
http://localhost:8000/delete/1/ - plant delete page

http://localhost:8000/profile/create/ - profile create page
http://localhost:8000/profile/details/ - profile details page
http://localhost:8000/profile/edit/ - profile edit page
http://localhost:8000/profile/delete/ - profile delete page
"""
