from django.contrib import admin
from .models import Event
from .models import lendingLinks
from .models import Jobs
from .models import Docs
from .models import Partner

admin.site.register(Event)
admin.site.register(lendingLinks)
admin.site.register(Jobs)
admin.site.register(Docs)
admin.site.register(Partner)
