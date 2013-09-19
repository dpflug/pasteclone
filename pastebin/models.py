from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from pastebin import settings
from pastebin.utils import random_id

class Paste(models.Model):
    """Represents all the data associated with a pasted text."""
    id = models.CharField(primary_key=True, max_length=settings.PASTE_ID_LENGTH)
    title = models.CharField('Title', max_length=500, blank=True)
    text = models.TextField('Text')
    created = models.DateTimeField('Creation time', default=timezone.now())
    accessed = models.DateTimeField('Last accessed time', default=timezone.now())

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        self.accessed = timezone.now()
        if not self.id:
            new_id = random_id(settings.PASTE_ID_LENGTH)
            # Now, we should avoid collisions. This could be a problem if the
            # hash space got filled, but this isn't going to production.
            # I could increase hash size or change the function.
            # Just remember to migrate if you change hash size.
            while len(Paste.objects.filter(id=new_id)) > 0:
                new_id = random_id(settings.PASTE_ID_LENGTH)
            self.id = new_id
        super(Paste, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('paste',
                       kwargs={'pastehash': self.id})

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.title
