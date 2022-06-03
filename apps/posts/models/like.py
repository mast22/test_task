from django.db import models as m


class Like(m.Model):
    post = m.ForeignKey("posts.Post", on_delete=m.CASCADE)
    user = m.ForeignKey("users.User", on_delete=m.CASCADE)

    # To ensure that every user leaves only a single like
    unique_together = ['post', 'user']
