from django.shortcuts import render
from rest_framework.generics import ListAPIView
from api.models import Post

# Create your views here.
from api.serializers import (PostSerializer)

class PostListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
