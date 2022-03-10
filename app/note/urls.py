from django.urls import path, include
from rest_framework import routers

from .views import NoteViewSet, TagViewSet, NoteList, NoteSearch

app_name='note'

router = routers.DefaultRouter()
router.register('list', NoteViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    # path('docs/', include_docs_urls(title='My API')),
    path('notes/', include(router.urls)),
    path('filter', NoteList.as_view()),
    path('search', NoteSearch.as_view())
]
