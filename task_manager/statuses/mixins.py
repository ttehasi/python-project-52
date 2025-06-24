from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


class ExistsTask:
    def post(self, request, *args, **kwargs):
        status = self.get_object()
        if getattr(status, 'tasks').exists():
            messages.add_message(request,
                                 messages.ERROR,
                    'Невозможно удалить статус, потому что он используется')
            return redirect(reverse('all_statuses'))
        return super().post(request, *args, **kwargs)