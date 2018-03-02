from django.http import HttpResponse
from .models import Topic, Comment


def index(request):
    latest_topics = Topic.objects.order_by('-pub_date')[:5]
    response = '\n\n'.join(topic.title for topic in latest_topics)
    return HttpResponse(response)


def detail(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    comments = Comment.objects.filter(topic_id=topic_id)
    response = topic.title + ' ' + ' '.join(
        comment.comment_text for comment in comments)
    return HttpResponse(response)
