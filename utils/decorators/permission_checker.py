from rest_framework import status
from rest_framework.response import Response


def check_permissions(custom_permissions=None):
    def decorator(func):
        def wrapper(self, request, *args, **kwargs):
            # Check DRF permission classes if provided
            permission_classes = self.permission_classes
            if permission_classes:
                permissions = [permission() for permission in permission_classes]
                for permission in permissions:
                    if not permission.has_permission(request, self):
                        return Response(
                            {"detail": "Permission denied."},
                            status=status.HTTP_403_FORBIDDEN,
                        )

            # Check custom permissions if provided
            if custom_permissions:
                user_groups = request.user.groups.all()

                group_permissions = set()
                for group in user_groups:
                    group_permissions.update(
                        group.permissions.values_list("codename", flat=True)
                    )

                # Ensure all required permissions exist in the group's permissions
                if not set(custom_permissions).issubset(group_permissions):
                    missing_permissions = set(custom_permissions) - group_permissions
                    return Response(
                        {
                            "detail": f"""
                            Missing required permissions: {', '.join(missing_permissions)}.
                            """
                        },
                        status=status.HTTP_403_FORBIDDEN,
                    )

            # If all permissions pass, proceed with the original method
            return func(self, request, *args, **kwargs)

        return wrapper

    return decorator
