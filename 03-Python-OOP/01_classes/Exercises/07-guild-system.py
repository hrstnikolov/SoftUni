class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added" \
               f" to the collection of" \
               f" the player {self.name}"

    def player_info(self):
        info = f'Name: {self.name}\n' \
               f'Guild: {self.guild}\n' \
               f'HP: {self.hp}\n' \
               f'MP: {self.mp}\n'
        for skill_name, mana_cost in self.skills.items():
            info += f'==={skill_name} - {mana_cost}\n'

        return info


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def has_this_guild(self, player: Player):
        return player.guild == self.name or player.guild == 'Unaffiliated'

    def is_player_in_guild(self, player: Player):
        return player in self.players

    def is_player_name_in_guild(self, player_name):
        for p in self.players:
            if player_name == p.first_name:
                return True
        return False

    def get_player_index_by_name(self, player_name):
        for index, player in enumerate(self.players):
            if player.first_name == player_name:
                return index

    def assign_player(self, player: Player):
        if not self.has_this_guild(player):
            return f"Player {player.name} is in another guild."
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        if not self.is_player_name_in_guild(player_name):
            f"Player {player_name} is not in the guild."
        index = self.get_player_index_by_name(player_name)
        self.players.pop(index)
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        guild_info = f'Guild: {self.name}\n'
        players_info = ''.join([player.player_info() for player in self.players])
        return guild_info + players_info


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
