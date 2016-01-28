from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, DetailView

from models import Photo
User = get_user_model()


class UserListView(ListView):
    model = User
    template_name = "photoviewer/user_list.html"

user_list_view = UserListView.as_view()


# user view ( list the user's photos and user details )
class UserDetailView(TemplateView):
    template_name = "photoviewer/user_detail.html"

    def get_context_data(self, **kwargs):
        user_id = kwargs['pk']

        # get the user, check if user_id is valid
        user = get_object_or_404(User, pk=user_id)

        # get the photos
        photos = Photo.objects.filter(created_by=user)

        return {
            'user' : user,
            'photos' : photos,
        }

user_detail_view = UserDetailView.as_view()


class PhotoDetailView(DetailView):
    model = Photo

photo_detail_view = PhotoDetailView.as_view()


class UploadPhotoView(CreateView):
    model = Photo
    fields = ['caption', 'created_by', 'image']

    def get_success_url(self):
        return reverse('list-users')

photo_upload_view = UploadPhotoView.as_view()
