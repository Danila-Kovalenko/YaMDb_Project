from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.response import Response
from reviews.models import Category, Genre, Review, Title
from users.models import UserProfile

from .filters import TitleFilter
from .mixins import CreateListDestroyMixin
from .permissions import (IsAuthor, IsAdmin, IsModerator, IfSafeRequest,
                          IsMyUsername, IfSafeRequest)
from .serializers import (CategorySerializer, CommentSerializer,
                          GenreSerializer, ReviewSerializer,
                          TitleCreateSerializer, TitleSerializer,
                          UserSerializer)


class CategoryViewSet(CreateListDestroyMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, ]
    search_fields = ('name',)
    permission_classes = [IsAdmin | IfSafeRequest, ]
    lookup_field = 'slug'


class GenreViewSet(CategoryViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.select_related(
        'category').prefetch_related('genre').annotate(
            rating=Avg('reviews__score')).order_by('name')
    permission_classes = [IsAdmin | IfSafeRequest, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PATCH',):
            return TitleCreateSerializer
        return TitleSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthor | IsAdmin | IsModerator | IfSafeRequest]

    def get_title(self):
        return get_object_or_404(Title, id=self.kwargs.get('title_id'))

    def get_queryset(self):
        return self.get_title().reviews.select_related('author').all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title())


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor | IsAdmin | IsModerator | IfSafeRequest]

    def get_review(self):
        return get_object_or_404(Review, id=self.kwargs.get('review_id'))

    def get_queryset(self):
        return self.get_review().comments.select_related('author').all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self.get_review())


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin | IsMyUsername, ]

    search_fields = '=user__username'
    lookup_field = 'username'

    def get_object(self):
        if self.kwargs.get('username') == 'me':
            username = self.request.user
        else:
            username = self.kwargs.get('username')
        obj = get_object_or_404(UserProfile, username=username)
        self.check_object_permissions(self.request, obj)
        return obj

    def destroy(self, request, *args, **kwargs):
        if self.kwargs.get('username').lower() == 'me':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
