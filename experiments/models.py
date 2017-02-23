from django.db import models


# class Laboratory(models.Model):
#     name = models.CharField(max_length=200, null=False)
#     description = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class ResearchProject(models.Model):
#     title = models.CharField(max_length=150, null=False)
#     description = models.TextField()
#     start_date = models.DateField()
#     end_date = models.DateField()
#
#     def __str__(self):
#         return self.title


class FileUpload(models.Model):
    datafile = models.FileField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='uploaded_files')


class Experiment(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    # research_project = models.ForeignKey(ResearchProject, null=False,
    #                                      blank=False)
    # laboratory = models.ForeignKey(Laboratory, null=False, blank=False)
    nes_id = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='experiments')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('updated',)
