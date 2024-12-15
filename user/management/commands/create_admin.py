from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create an ADMIN group with all permissions and an admin user in that group."

    def handle(self, *args, **kwargs):
        # Create the ADMIN group
        admin_group, created = Group.objects.get_or_create(name="ADMIN")

        if created:
            # Assign all permissions to the ADMIN group
            all_permissions = Permission.objects.all()
            admin_group.permissions.set(all_permissions)
            admin_group.save()
            self.stdout.write(
                self.style.SUCCESS("ADMIN group created and all permissions assigned.")
            )
        else:
            self.stdout.write(self.style.WARNING("ADMIN group already exists."))

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
