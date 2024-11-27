from .models import Profile


def get_author_profile_img(post):
    profile = Profile.objects.get(user__username=post.user)
    return profile.profile_img.url
