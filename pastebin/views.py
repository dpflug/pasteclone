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

    # For now, I'm going to leave the expiration here.
    Paste.objects.remove_expired()

    pasteform = PasteForm()
    context['pasteform'] = pasteform

    context['previous_pastes'] = Paste.objects.all()[:10]

    return render(request, 'paste.html', context)
