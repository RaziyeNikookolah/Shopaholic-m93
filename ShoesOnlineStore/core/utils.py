from django.db import models
from django.utils.translation import gettext_lazy as _


class ROLE(models.IntegerChoices):
    USER = 0, _('User')
    CUSTOMER = 1, _('Customer')
    MANAGER = 2, _('Manager')
    STAFF = 3, _('Staff')


PROVINCES = [
    ('thr', _('Tehran')),
    ('az-sh', _('Azarbayejan Sharghi')),
    ('az-gh', _('Azarbayejan Gharbi')),
    ('ard', _('Ardebil')),
    ('esf', _('Esfehan')),
    ('alb', _('Alborz')),
    ('ilm', _('Ilam')),
    ('bsh', _('Booshehr')),
    ('chm', _('Charmahal o Bakhtiari')),
    ('kh-j', _('Khorasan Jonobi')),
    ('kh-r', _('Khorasan Razavi')),
    ('kh-sh', _('Khorasan Shomali')),
    ('khz', _('Khoozestan')),
    ('znj', _('Zanjan')),
    ('smn', _('Semnan')),
    ('sbch', _('Sistan Baloochestan')),
    ('frs', _('Fars')),
    ('ghz', _('Ghazvin')),
    ('qom', _('Qom')),
    ('krd', _('Kordestan')),
    ('krm', _('Kerman')),
    ('kr-sh', _('Kerman Shah')),
    ('khb', _('Kohkilooye Boyer Ahmad')),
    ('gls', _('Golestan')),
    ('gil', _('Gilan')),
    ('lor', _('Lorestan')),
    ('maz', _('Mazandaran')),
    ('mrk', _('Markazi')),
    ('hrm', _('Hormozgan')),
    ('hmd', _('Hamedan')),
    ('yzd', _('Yazd')),
]
