from rest_framework import mixins, viewsets


class CreateAndReadOnlyCustom(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              viewsets.GenericViewSet):
    pass
