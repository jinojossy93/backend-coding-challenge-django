from rest_framework.test import force_authenticate, APIRequestFactory

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Note, Tag

from .views import NoteViewSet, NoteList
# Create your tests here.

class TagTestCase(TestCase):
    def setUp(self) -> None:
        Tag.objects.create(name="2021")
        Tag.objects.create(name="2022")
        Tag.objects.create(name="news")
    
    def test_tags(self) -> None:
        tag1 = Tag.objects.get(name="2021")
        tag2 = Tag.objects.get(name="2022")
        tag3 = Tag.objects.get(name="news")
        self.assertEqual(tag1.name, "2021")
        self.assertEqual(tag2.name, "2022")
        self.assertEqual(tag3.name, "news")


class NoteTestCase(TestCase):
    def setUp(self) -> None:
        tag1 = Tag.objects.create(name="2021")
        tag2 = Tag.objects.create(name="2022")
        tag3 = Tag.objects.create(name="news")
        note = Note.objects.create(title="Test Note", 
                            body="<h1>Note Body</h1>")
        note.tags.add(tag1, tag3)
    
    def test_tags(self) -> None:
        note = Note.objects.get(id=1)
        tags = []
        for i in note.tags.all():
            tags.append(i.id)
        self.assertEqual(note.title, "Test Note")
        self.assertEqual(tags, [1,3])


class NoteModelViewTest1Case(TestCase):
    def setUp(self)-> None:
        user = User.objects.create(username="jinojossy")
        tag1 = Tag.objects.create(name="2021")
        tag2 = Tag.objects.create(name="2022")
        tag3 = Tag.objects.create(name="news")
        note1 = Note.objects.create(title="Test Note", 
                            body="<h1>Note Body</h1>",
                            author=user)
        note1.tags.add(tag1, tag3)
        note2 = Note.objects.create(title="Note 2", 
                            body="<h1>Note 2</h1>",
                            author=user,
                            public=False)
        note1.tags.add(tag1, tag2)

    def test_response(self):
        factory = APIRequestFactory()
        view = NoteViewSet.as_view({'get': 'list'})
        user = User.objects.get(username='jinojossy')
        notes = Note.objects.all()

        # Make an authenticated request to the view...
        request = factory.get('/notes/list')
        force_authenticate(request, user=user)

        response = view(request)
        self.assertEqual(len(response.data), len(notes))
        self.assertEqual(response.data[0].get('author'), 1)
        self.assertEqual(response.data[0].get('public'), True)
        self.assertEqual(response.data[1].get('public'), False)


class NoteListViewTestCase(TestCase):
    def setUp(self)-> None:
        user = User.objects.create(username="jinojossy")
        tag1 = Tag.objects.create(name="2021")
        tag2 = Tag.objects.create(name="2022")
        tag3 = Tag.objects.create(name="news")
        note1 = Note.objects.create(title="Test Note", 
                            body="<h1>Note Body</h1>",
                            author=user)
        note1.tags.add(tag1, tag3)
        note2 = Note.objects.create(title="Note 2", 
                            body="<h1>Note 2</h1>",
                            author=user,
                            public=False)
        note2.tags.add(tag1, tag2)

    def test_response(self):
        factory = APIRequestFactory()
        view = NoteList.as_view()
        user = User.objects.get(username='jinojossy')
        notes = [Note.objects.get(id=1)]

        # Make an authenticated request to the view...
        request = factory.get('/filter?tags__name=news')
        force_authenticate(request, user=user)

        response = view(request)
        self.assertEqual(len(response.data), len(notes))
        self.assertEqual(response.data[0].get('author'), 1)
        self.assertEqual(response.data[0].get('public'), True)
