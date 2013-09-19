from django.utils import timezone
from django.test import TestCase
from pastebin.models import Paste

class PasteTest(TestCase):
    def test_create_paste(self):
        self.p = Paste(title="testly", text="Testcase")
        self.p.save()

        self.assertEqual(Paste.objects.get(id=self.p.id), self.p)
        self.p.delete()

    def test_many_create_paste(self):
        """Because I can. Also, makes a good stress test.
        My current ID length is set to 6. This should give me a hash space
        of just over a billion. 32^6. Collisions won't be an issue."""
        count = 1000  # 1,000,000 takes just under a half hour on my setup
        for x in xrange(count):
            p = Paste(title="test%s" % x, text="multiple test %s" % x)
            p.save()

        self.assertEqual(count, Paste.objects.count())
