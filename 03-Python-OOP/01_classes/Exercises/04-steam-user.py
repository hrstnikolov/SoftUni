class SteamUser:
    def __init__(self, username, games, played_hours=0):
        self.username = username
        self.games = games
        self.played_hours = played_hours

    def is_owned(self, game):
        return game in self.games

    def play(self, game, hours):
        if not self.is_owned(game):
            return f"{game} is not in library"
        self.played_hours += hours
        return F"{self.username} is playing {game}"

    def buy_game(self, game):
        if self.is_owned(game):
            return f"{game} is already in your library"
        self.games.append(game)
        return f"{self.username} bought {game}"

    def stats(self):
        games_count = len(self.games)
        return f"{self.username} has {games_count} games." \
               f" Total play time: {self.played_hours}"


user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.stats())