from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from MyProject.models import Post
import json

@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        data = {'posts': []}
        for post in posts:
            data['posts'].append({
                'id': post.id,
                'title': post.title,
                'body': post.body,
                'created_at': post.created_at.isoformat(),
                'updated_at': post.updated_at.isoformat()
            })
        return JsonResponse(data)
    elif request.method == 'POST':
        post_data = json.loads(request.body)
        post = Post(title=post_data['title'], body=post_data['body'])
        post.save()
        return JsonResponse({'id': post.id, 'title': post.title, 'body': post.body})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def post_detail(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)
        data = {
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'created_at': post.created_at.isoformat(),
            'updated_at': post.updated_at.isoformat()
        }
        return JsonResponse(data)
    elif request.method == 'PUT':
        post = get_object_or_404(Post, pk=post_id)
        post_data = json.loads(request.body)
        post.title = post_data.get('title', post.title)
        post.body = post_data.get('body', post.body)
        post.save()
        return JsonResponse({'id': post.id, 'title': post.title, 'body': post.body})
    elif request.method == 'PATCH':
        post = get_object_or_404(Post, pk=post_id)
        post_data = json.loads(request.body)
        post.title = post_data.get('title', post.title)
        post.body = post_data.get('body', post.body)
        post.save()
        return JsonResponse({'id': post.id, 'title': post.title, 'body': post.body})
    elif request.method == 'DELETE':
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid request method'})