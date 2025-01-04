from .models import Message

def unseen_message_count(request):
    if request.user.is_authenticated:
        count = Message.objects.filter(sentTo=request.user, seen=False).count()
    else:
        count = 0
    return {'unseen_message_count': count}