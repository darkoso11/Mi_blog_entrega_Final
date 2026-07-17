from .models import Author


def sync_author_for_user(user):
    if not user or not user.is_authenticated:
        return None

    email = user.email or f'{user.username}@example.com'
    name = user.get_full_name() or user.username
    author = Author.objects.filter(user=user).first()
    if not author:
        author = Author.objects.filter(email=email).first()

    if author:
        author.user = user
        author.name = name
        author.email = email
        author.save()
        return author

    return Author.objects.create(user=user, name=name, email=email)
