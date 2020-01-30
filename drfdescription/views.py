from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class DummyViewSet(GenericViewSet):
    # queryset = Account.objects.all()
    # serializer_class = AccountSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]

    @action(detail=True)
    def description(request, *args, **kwargs):
        return Response('foo')
