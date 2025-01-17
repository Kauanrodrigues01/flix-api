import uuid
from django.db import models

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRA', 'Brasil'),
    ('CAN', 'Canadá'),
    ('MEX', 'México'),
    ('ARG', 'Argentina'),
    ('CHL', 'Chile'),
    ('COL', 'Colômbia'),
    ('PER', 'Peru'),
    ('VEN', 'Venezuela'),
    ('URY', 'Uruguai'),
    ('FRA', 'França'),
    ('DEU', 'Alemanha'),
    ('ITA', 'Itália'),
    ('ESP', 'Espanha'),
    ('PRT', 'Portugal'),
    ('NLD', 'Países Baixos (Holanda)'),
    ('BEL', 'Bélgica'),
    ('CHE', 'Suíça'),
    ('AUT', 'Áustria'),
    ('SWE', 'Suécia'),
    ('NOR', 'Noruega'),
    ('DNK', 'Dinamarca'),
    ('FIN', 'Finlândia'),
    ('POL', 'Polônia'),
    ('CZE', 'República Tcheca'),
    ('HUN', 'Hungria'),
    ('GRC', 'Grécia'),
    ('JPN', 'Japão'),
    ('CHN', 'China'),
    ('IND', 'Índia'),
    ('PAK', 'Paquistão'),
    ('IDN', 'Indonésia'),
    ('PHL', 'Filipinas'),
    ('RUS', 'Rússia'),
    ('AUS', 'Austrália'),
    ('NZL', 'Nova Zelândia'),
    ('ZAF', 'África do Sul'),
    ('EGY', 'Egito'),
    ('NGA', 'Nigéria'),
    ('KEN', 'Quênia'),
    ('ETH', 'Etiópia'),
    ('TUR', 'Turquia'),
    ('KOR', 'Coreia do Sul'),
    ('SAU', 'Arábia Saudita'),
    ('ISR', 'Israel'),
    ('GBR', 'Reino Unido'),
    ('IRL', 'Irlanda'),
    ('THA', 'Tailândia'),
    ('VNM', 'Vietnã'),
    ('SGP', 'Singapura'),
    ('MYS', 'Malásia'),
)


class Actor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
