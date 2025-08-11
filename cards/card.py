from typing import Optional
    
class Card:
    def __init__(self, name: str, description: str, attributes: Optional[dict] = None, face_up: bool = False):
        """Initializes a Card instance.

        Args:
            name (str): Name of the card.
            description (str): Description or flavor text.
            attributes (dict, optional): Additional properties. Defaults to empty dict.
            face_up (bool, optional): Whether the card is face up. Defaults to False.
        """
        self.name = name
        self.description = description
        self.attributes = attributes or {}
        self.face_up = face_up or attributes.get('face_up', False) if attributes else False

    def __str__(self):
        return f"{self.name}: {self.description}"

    def __repr__(self):
        return self.description
        # return f"Card(name={self.name}, description={self.description})"