from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post 
from .serializers import PostSerializer



@api_view(["GET"])
def index(request):
    return Response({"message": "Hello, world!"})



@api_view(["GET"])
def GetAllPost(request):
    get_posts = Post.objects.all()
    serilializer = PostSerializer(get_posts, many=True)
    return Response(serilializer.data)


@api_view(["GET","POST"])
def CreatePost(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success": " Your post was saved successfully "}, status=201)
    else:
     return Response(serializer.errors, status=400)
    

@api_view(["DELETE"])
def DeletePost(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return Response({"Success": "Post deleted successfully"}, status=200)
    except Post.DoesNotExist:
        return Response({"Error": "Post not found"}, status=404)
    
@api_view(["GET"])
def GetSingle(request, id):
    try:
        post = Post.objects.get(id=id)
        serilializer = PostSerializer(post)
        return Response(serilializer.data)
    except Post.DoesNotExist:
        return Response({"Error": "Post not found"}, status=404)



@api_view(["PUT"])
def UpdatePost(request, id):
    post = Post.objects.get(id=id)
    get_new_title = request.data.get('title')
    get_new_content = request.data.get('content')

    try:
        post = Post.objects.get(id=id)

        if get_new_title:
            post.title = get_new_title

        if get_new_content:
            post.content = get_new_content

        post.save()
        return Response({"Success": "Post updated successfully"}, status=200)

    except Post.DoesNotExist:
        return Response({"Error": "Post not found"}, status=404)
