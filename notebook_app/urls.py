from django.urls import path
from notebook_app import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('notes/', views.notes_page, name='notes-page'),
    path('create_note/', views.create_note, name='create-note'),
    path('note_detail/<int:pk>/', views.note_detail, name='note-detail'),
    path('delete_note/<int:pk>/', views.delete_note, name='delete-note'),
    path('update_note/<int:pk>/', views.update_note, name='update-note'),
    path('todos/', views.todos_page, name='todos-page'),
    path('create_todos/', views.create_todo, name='create-todo'),
    path('update_todo/<int:pk>', views.update_todo, name='update-todo'),
    path('delete_todo/<int:pk>', views.delete_todo, name='delete-todo'),
    path('registration/', views.registration, name='registration'),
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout')

]
