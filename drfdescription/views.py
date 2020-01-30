from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class DummyViewSet(GenericViewSet):

    @action(detail=False)
    def description(request, *args, **kwargs):
        return Response('description')
