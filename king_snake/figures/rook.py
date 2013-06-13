"""Rook chess piece."""

from .figure import Figure


class Rook(Figure):

    """Rook chess piece."""

    start_position = {"white": ["A1", "H1"],
                      "black": ["A8", "H8"]}

    def __init__(self, player):
        super(Rook, self).__init__(player)

    @property
    def legal_moves(self):
        """Return legal moves from current position."""
        return self._fields_in_directions(("to_left", "to_right", "above",
                                           "below"))
