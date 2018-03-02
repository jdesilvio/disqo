import logging
from django.shortcuts import (
    get_object_or_404,
    get_list_or_404,
    render,
    redirect)
from django.utils import timezone
from .models import Topic, Comment
from .models import (
    MAX_TITLE_LENGTH,
    MAX_DESCRIPTION_LENGTH,
    MAX_COMMENT_LENGTH)


logger = logging.getLogger(__name__)


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


def new(request):
    context = {
        'max_title_length': MAX_TITLE_LENGTH,
        'max_desc_length': MAX_DESCRIPTION_LENGTH
    }
    return render(request, 'discussions/new.html', context)


def create(request):
    topic = Topic(title=request.POST['title'],
                  description=request.POST['description'],
                  pub_date=timezone.now())
    topic.save()
    logger.info('Saving new topic: {}'.format(topic))
    return redirect('/discussions/{}'.format(topic.id))


def comment(request, topic_id):
    comment = Comment(topic_id=topic_id,
                      comment_text=request.POST['comment_text'],
                      pub_date=timezone.now())
    comment.save()
    logger.info('New comment: {}, Topic ID: {}'
                .format(comment, topic_id))
    return redirect('/discussions/{}'.format(topic_id))
