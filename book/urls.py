from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="book-home"),
    path('about/', views.about, name='book-about'),
    path('contact/', views.contact, name='book-contact'),
    path('<int:year>/<str:month>/', views.home, name="book-home"),
    path('venue/', views.venues_list, name='venue-list'),
    path('reservation/', views.all_reservations, name='reservation-list'),
    path('add_reservation/', views.add_reservation, name='add-reservation'),
    path('search_reservation/', views.search_reservation, name='search-reservation'),
    path('update_reservation/<reservation_id>', views.update_reservation, name='update-reservation'),
    path('delete_reservation/<reservation_id>', views.delete_reservation, name='delete-reservation'),
    path('reservation_pdf', views.reservation_pdf, name='reservation_pdf'),
    path('admin_approval', views.admin_approval, name='admin_approval'),
]
    