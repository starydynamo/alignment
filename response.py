class AlignmentSystem:
    def __init__(self):
        self.characters = {}
        self.user_assignments = {}
        self.alignment_map = {
            100: "Lawful Good",
            90: "Neutral Good",
            80: "Chaotic Good",
            70: "Lawful Neutral",
            60: "True Neutral",
            50: "Unaligned",
            40: "Chaotic Neutral",
            30: "Lawful Evil",
            20: "Neutral Evil",
            10: "Chaotic Evil",
            0: "Hellish"
        }

    def _get_alignment(self, rank):
        return self.alignment_map.get(rank, "Unknown Alignment")

    def create_character(self, name):
        if name in self.characters:
            return f"Character '{name}' already exists."
        self.characters[name] = 50  # Default alignment: Unaligned
        return f"Character '{name}' created with alignment = Unaligned (50)."

    def assign_alignment(self, name, alignment):
        if name not in self.characters:
            return f"Character '{name}' does not exist."
        if alignment not in self.alignment_map:
            return "Invalid alignment ranking. Use a valid ranking from 0 to 100."
        self.characters[name] = alignment
        return f"{name}'s Alignment = {self._get_alignment(alignment)} ({alignment})."

    def rank_character(self, name, change):
        if name not in self.characters:
            return f"Character '{name}' does not exist."
        self.characters[name] += change
        current_rank = self.characters[name]
        if current_rank > 100:
            self.characters[name] = 100
        elif current_rank < 0:
            self.characters[name] = 0
        return f"{name}'s Alignment = {self._get_alignment(self.characters[name])} ({self.characters[name]})."

    def track_alignment(self, name):
        if name not in self.characters:
            return f"Character '{name}' does not exist."
        current_rank = self.characters[name]
        return f"{name}'s Alignment = {self._get_alignment(current_rank)} ({current_rank})."

    def list_characters(self):
        if not self.characters:
            return "No characters have been created yet."
        character_list = "\n".join([f"{name}: {self._get_alignment(rank)} ({rank})" for name, rank in self.characters.items()])
        return f"Character List:\n{character_list}"

    def group_alignment(self):
        if not self.characters:
            return "No characters have been created yet."
        total_alignment = sum(self.characters.values())
        average_alignment = total_alignment // len(self.characters)
        character_list = "\n".join([f"{name}: {self._get_alignment(rank)} ({rank})" for name, rank in self.characters.items()])
        return f"Character List:\n{character_list}\n\nAverage Alignment: {self._get_alignment(average_alignment)} ({average_alignment})."

    def assign_user(self, discord_user, character_name):
        if discord_user in self.user_assignments:
            return f"You are already assigned to a character: {self.user_assignments[discord_user]}."
        if character_name not in self.characters:
            return f"Character '{character_name}' does not exist."
        self.user_assignments[discord_user] = character_name
        return f"{discord_user} has been assigned to character '{character_name}'."
