from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Message
from django.contrib.auth import get_user_model

User = get_user_model()


@login_required
def inbox(request):
    # Get all unique conversations for logged in user
    messages_qs = Message.objects.filter(Q(sender=request.user) | Q(receiver=request.user)).order_by('-timestamp')
    # Get unique user conversations
    conversations = {}
    for msg in messages_qs:
        other_user = msg.sender if msg.receiver == request.user else msg.receiver
        if other_user.id not in conversations:
            conversations[other_user.id] = {
                'user': other_user,
                'last_message': msg,
                'unread': Message.objects.filter(sender=other_user, receiver=request.user, is_read=False).exists()
            }
    return render(request, 'messaging/inbox.html', {'conversations': list(conversations.values())})


@login_required
def conversation(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    # Enforce messaging rules
    if request.user.role == other_user.role:
        return redirect('inbox')
    
    # Get all messages in conversation
    messages_qs = Message.objects.filter(
        Q(sender=request.user, receiver=other_user) |
        Q(sender=other_user, receiver=request.user)
    ).order_by('timestamp')
    
    # Mark all messages from other user as read
    Message.objects.filter(sender=other_user, receiver=request.user).update(is_read=True)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(sender=request.user, receiver=other_user, content=content)
            return redirect('conversation', user_id=user_id)
    
    return render(request, 'messaging/conversation.html', {
        'other_user': other_user,
        'messages': messages_qs
    })
