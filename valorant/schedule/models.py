from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField(max_length=1000)

    def __str__(self):
        return self.name


class Final(models.Model):
    team1 = models.OneToOneField(Team, models.SET_NULL,
                                 blank=True,
                                 null=True, related_name='f_host')
    team2 = models.OneToOneField(Team, models.SET_NULL,
                                 blank=True,
                                 null=True, related_name='f_opponent')

    CHOICES = [(1, 'TEAM 1'),
               (-1, 'TEAM 2'),
               (0, 'NULL')]

    winner = models.PositiveSmallIntegerField(choices=CHOICES, blank=True, null=True)

    date = models.DateTimeField()

    def __str__(self):
        return self.team1.name + ' vs ' + self.team2.name


class SemiFinal(models.Model):
    team1 = models.OneToOneField(Team, models.SET_NULL,
                                 blank=True,
                                 null=True, related_name='sf_host')
    team2 = models.OneToOneField(Team, models.SET_NULL,
                                 blank=True,
                                 null=True, related_name='sf_opponent')

    CHOICES = [(1, 'TEAM 1'),
               (-1, 'TEAM 2'),
               (0, 'NULL')]

    winner = models.PositiveSmallIntegerField(choices=CHOICES, blank=True, null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.team1.name + ' vs ' + self.team2.name


class QuarterFinal(models.Model):
    team1 = models.OneToOneField(Team, models.SET_NULL,
                                 blank=True,
                                 null=True, related_name='qf_host')
    team2 = models.OneToOneField(Team, models.SET_NULL,
                                 blank=True,
                                 null=True, related_name='qf_opponent')

    CHOICES = [(1, 'TEAM 1'),
               (-1, 'TEAM 2'),
               (0, 'NULL')]

    winner = models.PositiveSmallIntegerField(choices=CHOICES, blank=True, null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.team1.name + ' vs ' + self.team2.name


class KnockOut(models.Model):
    team1 = models.OneToOneField(Team, models.SET_NULL,
                                 blank=True,
                                 null=True, related_name='ko_host')
    team2 = models.OneToOneField(Team, models.SET_NULL,
                                 blank=True,
                                 null=True, related_name='ko_opponent')

    CHOICES = [(1, 'TEAM 1'),
               (-1, 'TEAM 2'),
               (0, 'NULL')]

    winner = models.PositiveSmallIntegerField(choices=CHOICES, blank=True, null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.team1.name + ' vs ' + self.team2.name
