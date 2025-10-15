class Personaje:
    def __init__(self, name, isVillano):
        self.name = name
        self.isVillano = isVillano

    def __str__(self):
        return f"Nombre: {self.name} - ¿Es villano?: {self.isVillano}"

personajesMCU = [
    ("Iron Man", False),
    ("Captain America", False),
    ("Thor", False),
    ("Hulk", False),
    ("Black Widow", False),
    ("Hawkeye", False),
    ("Spider-Man", False),
    ("Doctor Strange", False),
    ("Black Panther", False),
    ("Scarlet Witch", False),
    ("Vision", False),
    ("Ant-Man", False),
    ("Wasp", False),
    ("Falcon", False),
    ("Winter Soldier", False),
    ("Star-Lord", False),
    ("Gamora", False),
    ("Drax", False),
    ("Rocket Raccoon", False),
    ("Groot", False),
    ("Nick Fury", False),
    ("Loki", True),
    ("Thanos", True),
    ("Ultron", True),
    ("Red Skull", True),
    ("Hela", True),
    ("Killmonger", True),
    ("Vulture", True),
    ("Mysterio", True),
    ("Ronan the Accuser", True),
]