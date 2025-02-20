from rest_framework.permissions import BasePermission


class GlobalDefaultModelPermission(BasePermission):
    """
    Generic permission class to handle CRUD permissions for any model.
    Assumes permissions are in the format:
    'app_label.add_model', 'app_label.change_model', 'app_label.delete_model'.
    """

    def has_permission(self, request, view):
        user = request.user
        method = request.method
        app_name = view.queryset.model._meta.app_label
        model_name = view.queryset.model._meta.model_name

        if user.is_staff:
            return True

        if method == 'GET':
            return True

        if not user.is_authenticated:
            return False

        permission_map = {
            'POST': f'{app_name}.add_{model_name}',
            'PUT': f'{app_name}.change_{model_name}',
            'PATCH': f'{app_name}.change_{model_name}',
            'DELETE': f'{app_name}.delete_{model_name}'
        }

        required_permission = permission_map.get(method)
        if required_permission:
            return user.has_perm(required_permission)

        return False
