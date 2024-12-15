from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create an ADMIN group with all permissions and an admin user in that group."

    def handle(self, *args, **kwargs):
        # Create the ADMIN group
        admin_group, created = Group.objects.get_or_create(name="ADMIN")

        # Assign all permissions to the ADMIN group
        all_permissions = Permission.objects.all()
        current_permissions = admin_group.permissions.all()

        # Update group permissions if new ones are found
        new_permissions = all_permissions.difference(current_permissions)
        if new_permissions:
            admin_group.permissions.add(*new_permissions)
            admin_group.save()
            self.stdout.write(
                self.style.SUCCESS("ADMIN group updated with new permissions.")
            )
        else:
            self.stdout.write(
                self.style.WARNING("No new permissions found for the ADMIN group.")
            )

        # Create a user and add to the ADMIN group
        User = get_user_model()
        admin_user, user_created = User.objects.get_or_create(
            email="admin@admin.com",
            phone_number="+251999999999",
            first_name="Admin",
            last_name="Admin",
            defaults={
                "is_staff": True,
                "is_superuser": True,
            },
        )

        if user_created:
            admin_user.set_password("admin1234")  # Hash the password
            admin_user.save()
            self.stdout.write(self.style.SUCCESS("Admin user 'admin_user' created."))
        else:
            self.stdout.write(
                self.style.WARNING("Admin user 'admin_user' already exists.")
            )

        # Add the user to the ADMIN group
        admin_user.groups.add(admin_group)
        self.stdout.write(
            self.style.SUCCESS("Admin user 'admin_user' added to ADMIN group.")
        )
