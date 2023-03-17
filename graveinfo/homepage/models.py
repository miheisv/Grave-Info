from django.db import models
from sorl.thumbnail import get_thumbnail
from PIL import Image
from graveinfo.settings import STATIC_ROOT, STATIC_URL


class HumanManager(models.Manager):
    def select_main(self):
        return (
            self.get_queryset()
                .all()
                .order_by('last_name')
        )


class Human(models.Model):
    main_picture = models.ImageField(
        'post picture',
        upload_to='images/%Y/%m',
        blank=True,
    )
    first_name = models.CharField(
        'имя и отчество',
        max_length=120,
        blank=True,
        default='Иван Иванович',
    )
    last_name = models.CharField(
        'фамилия',
        max_length=60,
        blank=True,
        default='Иванов',
    )
    description = models.TextField(
        verbose_name='описание',
        max_length=300,
        default='',
    )
    age = models.PositiveIntegerField(
        'возраст',
    )
    born = models.DateTimeField(
        'дата рождения'
    )
    death = models.DateTimeField(
        'дата смерти'
    )
    NS = models.FloatField(
        'широта',
        default=0.0,
    )
    WE = models.FloatField(
        'долгота',
        default=0.0,
    )

    objects = HumanManager()

    crop_img = None

    class Meta:
        verbose_name = 'human'
        verbose_name_plural = 'humans'
        default_related_name = 'humans'

    @property
    def get_img(self):
        if not self.main_picture:
            try:
                self.main_picture = f'default.jpg'
            except FileNotFoundError:
                print('Файла стандартной иконки нет в директрории MEDIA. Добавьте файл изображения в директорию media/')
        if self.crop_img:
            return self.main_picture
        self.crop_img = Image.open(f'./media/{self.main_picture}').resize((150, 150))
        self.crop_img.save(f'./media/{self.main_picture}')        
        return self.main_picture

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
