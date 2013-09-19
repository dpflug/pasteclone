from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.utils import timezone
from pastebin import settings
from pastebin.forms import PasteForm
from pastebin.models import Paste

def paste_view(request, pastehash = None):
    """Basic pastebin."""

    context = {}
    context['errors'] = []
    
    if request.method == "POST" and request.POST:
        paste = Paste()
        pasteform = PasteForm(request.POST, instance=paste)

        if pasteform.is_valid():
            paste = pasteform.save()
            return redirect(paste.get_absolute_url())
            
    else:
        if pastehash:
            paste = get_object_or_404(Paste, id=pastehash)
            paste.save()
            context['paste'] = paste

    # Let's remove some expired posts...
    # There are better ways to do this (Celery, for instance),
    # but I'm not running a full site.
    exp_time = timezone.now() - timezone.timedelta(30)
    Paste.objects.filter(accessed__lt=exp_time).delete()

    pasteform = PasteForm()
    context['pasteform'] = pasteform

    context['previous_pastes'] = Paste.objects.all()[:10]

    return render(request, 'paste.html', context)
