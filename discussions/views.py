from django.shortcuts import (
    get_object_or_404,
    get_list_or_404,
    render)
from .models import Topic, Comment
from .models import (
    MAX_TITLE_LENGTH,
    MAX_DESCRIPTION_LENGTH,
    MAX_COMMENT_LENGTH)


def index(request):
    latest_topics = Topic.objects.order_by('-pub_date')[:5]
    context = {
        'latest_topics': latest_topics
    }
    return render(request, 'discussions/index.html', context)


def detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    comments = Comment.objects.filter(topic_id=topic_id)
    context = {
        'topic': topic,
        'comments': comments,
        'max_comment_length': MAX_COMMENT_LENGTH
    }
    return render(request, 'discussions/detail.html', context)
