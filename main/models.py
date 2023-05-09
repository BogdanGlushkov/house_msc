from django.conf import settings
from django.db import models


class Event(models.Model):
    DAYS = [
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('06', '06'),
        ('07', '07'),
        ('08', '08'),
        ('09', '09'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31')
    ]

    HOURS = [
        ('00', '00'),
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('06', '06'),
        ('07', '07'),
        ('08', '08'),
        ('09', '09'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23')
    ]

    MINUTES = [
        ('00', '00'),
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('06', '06'),
        ('07', '07'),
        ('08', '08'),
        ('09', '09'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
        ('32', '32'),
        ('33', '33'),
        ('34', '34'),
        ('35', '35'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
        ('46', '46'),
        ('47', '47'),
        ('48', '48'),
        ('49', '49'),
        ('50', '50'),
        ('51', '51'),
        ('52', '52'),
        ('53', '53'),
        ('54', '54'),
        ('55', '55'),
        ('56', '56'),
        ('57', '57'),
        ('58', '58'),
        ('59', '59')
    ]

    title = models.CharField('Название', max_length=50)
    day = models.CharField('День', choices=DAYS, blank=False, default='01', max_length=2)
    month = models.CharField('Месяц', choices=settings.MONTHS, blank=False, max_length=2, default='01')
    year = models.PositiveSmallIntegerField('Год', default=2023)
    timeHour = models.CharField('Час начала', choices=HOURS, blank=False, default='00', max_length=2)
    timeMinute = models.CharField('Минута начала', choices=MINUTES, blank=False, default='00', max_length=2)
    place = models.CharField('Место проведения', max_length=250)
    place_link = models.CharField('Ссылка на место', max_length=250)
    guest = models.PositiveSmallIntegerField('Количество гостей')
    timeDuration = models.PositiveSmallIntegerField('Длительность мероприятия')
    dress_style = models.CharField('Дресс-код', max_length=40)
    price = models.IntegerField('Новая Цена')
    procents = models.IntegerField('Скидка Процентов')
    link1 = models.CharField('Ссылка на подробнее', max_length=250, default='0', blank=False)
    link2 = models.CharField('Ссылка на подробнее', max_length=250, default='0', blank=False)
    link3 = models.CharField('Ссылка на подробнее', max_length=250, default='0', blank=False)
    link4 = models.CharField('Ссылка на подробнее', max_length=250, default='0', blank=False)
    link5 = models.CharField('Ссылка на подробнее', max_length=250, default='0', blank=False)
    link6 = models.CharField('Ссылка на подробнее', max_length=250, default='0', blank=False)
    link7 = models.CharField('Ссылка на подробнее', max_length=250, default='0', blank=False)
    link8 = models.CharField('Ссылка на подробнее', max_length=250, default='0', blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class lendingLinks(models.Model):
    title = models.CharField('Название', max_length=50, default='name')
    link1 = models.CharField('Ссылка баннер', max_length=250, default='#')
    link2 = models.CharField('Ссылка ноутбук', max_length=250, default='#')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ссылки на странице'
        verbose_name_plural = 'Ссылки'


class Jobs(models.Model):
    title = models.CharField('Название', max_length=50, default='New')
    description = models.CharField('Описание вакансии', max_length=250)
    salary = models.IntegerField('Заработная плата')
    salaryDesc = models.CharField('Время заработка', max_length=25, default='смена')
    link = models.CharField('Ссылка на вакансию', max_length=250, default='https://t.me/chausmoscow_bot')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class Docs(models.Model):
    title = models.CharField('Название', max_length=50, default='New')
    link = models.CharField('Ссылка на документ', max_length=250, default='#')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Partner(models.Model):
    title = models.CharField('Название', max_length=50, default='New')
    link = models.CharField('Ссылка на партнера', max_length=250, default='#')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
