from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    # # user permissions
    # def has_permission(self, request, view):
    #     ip_address = request.META['REMOTE_ADDR']
    #     in_blacklist = Blacklist.objects.filter(ip=ip_address).exists()
    #
    #     return not in_blacklist

    # object permissions
    def has_object_permission(self, request, view, obj):
        # ReadOnly permission
        if request.method in permissions.SAFE_METHODS:
            return True
        # for CRUD operations you should be the owner of the posts
        return obj.owner == request.user
