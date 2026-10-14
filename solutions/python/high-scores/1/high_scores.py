
"""Manage a player's high scores."""


class HighScores:
    """Represent a player's list of scores."""

    def __init__(self, scores):
        """Initialize the scores."""
        self.scores = scores

    def latest(self):
        """Return the most recently added score."""
        return self.scores[-1]

    def personal_best(self):
        """Return the highest score."""
        return max(self.scores)

    def personal_top_three(self):
        """Return the three highest scores in descending order."""
        return sorted(self.scores, reverse=True)[:3]
