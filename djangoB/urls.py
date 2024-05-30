from django.urls import path
from . import views

urlpatterns = [
    path('genders', views.indexgender),
    path('genders/create', views.creategender),
    path('store_gender', views.storegender),
    path('genders/show/<int:gender_id>', views.showgender),
    path('genders/edit/<int:gender_id>', views.editgender),
    path('genders/update/<int:gender_id>', views.updategender),
    path('genders/delete/<int:gender_id>', views.deletegender),
    path('genders/destroy/<int:gender_id>', views.destroygender),
    path('users', views.index_user),
    path('users/create', views.create_user),
    path('users/store', views.store_user),
    path('users/show/<int:user_id>', views.show_user),
    path('users/edit/<int:user_id>', views.edit_user),
    path('users/update/<int:user_id>', views.update_user),
    path('users/delete/<int:user_id>', views.delete_user),
    path('users/destroy/<int:user_id>', views.destroy_user),
]
