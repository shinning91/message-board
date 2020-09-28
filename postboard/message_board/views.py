from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import render
import requests
import json
from django.http import JsonResponse


class BoardPostList(ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        result = {}
        posts_url = 'https://jsonplaceholder.typicode.com/posts'
        posts_response = requests.get(posts_url).json()
        comments_url = 'https://jsonplaceholder.typicode.com/comments'
        comments_response = requests.get(comments_url).json()
        posts = []
        for post in posts_response:
            post_detail = {}
            post_detail['post_id'] = post['id']
            post_detail['post_title'] = post['title']
            post_detail['post_body'] = post['body']
            post_detail['total_number_of_comments'] = sum([1 for comment in comments_response if comment['postId'] == post['id']])
            posts.append(post_detail)
        sorted_posts = sorted(posts, key=lambda x: x['total_number_of_comments'])
        
        result['posts'] = sorted_posts
        result['status'] = 'success'
        return JsonResponse(result)


class SearchComment(RetrieveUpdateDestroyAPIView):
    def post(self, request, *args, **kwargs):
        result = {}
        keyword = json.loads(request.body)['keyword']
        comments_url = 'https://jsonplaceholder.typicode.com/comments'
        comments_response = requests.get(comments_url).json()
        comments = []
        for comment in comments_response:
            if keyword in comment['name'] or keyword in comment['body']:
                comments.append(comment)
        result['comments'] = comments
        result['status'] = 'success'
        return JsonResponse(result)



class CommentListCreate(ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        result = {}
        url = 'https://jsonplaceholder.typicode.com/comments'
        response = requests.get(url)
        result['comments'] = response.json()
        result['status'] = 'success'
        return JsonResponse(result)


class PostListCreate(ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        result = {}
        url = 'https://jsonplaceholder.typicode.com/posts'
        response = requests.get(url)
        result['posts'] = response.json()
        result['status'] = 'success'
        return JsonResponse(result)


class PostRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        result = {}
        post_id = kwargs['post_id']
        url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
        response = requests.get(url)
        result['post'] = response.json()
        result['status'] = 'success'
        return JsonResponse(result)