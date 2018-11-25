from rest_framework.generics import ( ListCreateAPIView, RetrieveUpdateDestroyAPIView )
from cats.models import Cat
from .serializers import CatSerializer

class CatMixin(object):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

class CatList(CatMixin, ListCreateAPIView):
    """
    Return a list of all cats, or
    create new ones
    """
    pass

class CatDetail(CatMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific cat, update it, or delete it.
    """
    pass
# Create your views here.