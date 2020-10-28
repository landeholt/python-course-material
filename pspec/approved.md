182 Yatzy
----
###### John Landeholt 
###### 950713-0178

Flödet kommer att se ut på följande vis:
1. Programmet startas upp
2. Momenten läses in från fil
3. Protokollet frågar om antalet spelare
4. Protokollet skapar spelare från de namn som anges
5. Spelet börjar och protokollet håller koll på vems tur det är
6. Spelet emulerar ett tärningskast med 5 tärningar
7. Sedan får spelaren bestämma vilket moment de vill använda för omgången
    7.1. Inuti moment-instansen bestäms det den högsta poängmängden utifrån tärningarna som har kastats
    7.2. Poängen sparas undan i protokollet
8. upprepning av 6-7 görs tills alla moment har används
9. protokollet berättar vem som har vunnit

Programmet kommer att vara uppdelat i två delar. En del som tar hand om all logik och en del som tar hand om allt grafiskt.

Jag väljer att placera all min logik i en modul jag kallar för modell. Där kommer följande saker att finnas:
* Regler för varje moment
    Varje moment har olika regler för vilka tärningskombinationer som får matas in.
    Exempel:
        för moment 'Ettor', får enbart en mängd med ettor matas in
* Spelets state
* Felhantering för inmatning av ogiltiga tärningskombinationer för ett moment
* Logik angående tärningskast

Genom att konstruera en protokoll-klass, kan man bevara informationen om spelets state i själva klassen och jag tänker mig att dessa metoder kommer att behövas:

```python
class Protocol:
    
    def __init__(self, nplayers):
        # alla unika moment-instanser
        self.moments = {}
        # alla unika spelare
        self.players = []
        # protokollets poäng, uppdelat per spelare
        self.scores = {}

    # läser in momenten från en textfil och har inbyggd felhantering för när filen inte kan hittas.
    def get_moments_from_file(self):
        pass

    # lägger till en spelare till protokollet
    def add_player(self, name):
        pass
    
    """
    sätter poängen på det valda momentet. Momentet i sig tar hand om felhanteringen
    """
    def set_score(self, moment, dice_set):
        pass

    """
    returnerar spelets state till grafiska delen av programmet
    @return {
        'players_turn': 'P1',
        'players': {
            'P1': {
            'ettor': None,
            'tvåor: 4,
            ...
            'summa': 48,
            'bonus': None,
            ...
            'Yatzy': None,
            'summa': 70
        },
            'P2': {
            ...
            }
        }
    }
    """
    def get_state(self):
        pass
```

Sedan tänker jag att man använder sig utav subklasser av moment för att särskilja på reglerna per klass. Där superklassen kommer att se ut såhär:

```python
class Moment:
    
    def __init__(self):
        pass

    # Här kontrolleras reglerna från Yatzy, beroende på vilket moment det handlar om
    def check_dices(self, dice_set):
        pass

    # @return maximala summan av de tillåtna tärningsmängden som bestäms av check_dices
    def get_score(self):
        pass


class Ettor(Moment):

    def __init__(self):
        pass

    def check_dices(self, dice_set):
        pass
```
