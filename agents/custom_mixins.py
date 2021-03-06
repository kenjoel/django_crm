from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class OwnerAndLoginMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_owner:
            return redirect("leads:condor")
        return super().dispatch(request, *args, **kwargs)
