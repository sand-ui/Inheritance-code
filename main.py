


class BasketballPlayer:

    def __init__(self, player_id, name, points):
        self.__player_id = player_id
        self.name = name
        self._points = points
        print("BasketballPlayer constructor called.")

    def get_player_id(self):
        return self.__player_id

    def score_points(self, points):
        self._points += points
        print(f"{self.name} now has {self._points} points.")

    def display_details(self):
        return f"ID: {self.__player_id} | Name: {self.name} | Points: {self._points}"


class PointGuard(BasketballPlayer):

    def __init__(self, player_id, name, points, assists):
        super().__init__(player_id, name, points)

        self.assists = assists
        print("PointGuard constructor called.")

    def add_assist(self):
        self.assists += 1
        print(f"{self.name} now has {self.assists} assists.")

    
    def display_details(self):
        return f"ID: {self.get_player_id()} | Point Guard: {self.name} | Points: {self._points} | Assists: {self.assists}"


class Center(BasketballPlayer):

    def __init__(self, player_id, name, points, rebounds):
        super().__init__(player_id, name, points)

        self.rebounds = rebounds
        print("Center constructor called.")

    def add_rebound(self):
        self.rebounds += 1
        print(f"{self.name} now has {self.rebounds} rebounds.")

    # Overrides the inherited method.
    def display_details(self):
        return f"ID: {self.get_player_id()} | Center: {self.name} | Points: {self._points} | Rebounds: {self.rebounds}"


if __name__ == "__main__":
    print("--- Testing PointGuard Class ---")

    guard_1 = PointGuard(
        player_id="P100",
        name="Curry",
        points=12,
        assists=8
    )

    # Inherited method
    guard_1.score_points(3)

    # Position-specific method
    guard_1.add_assist()

    # Overridden method
    print(guard_1.display_details())

    print("\n--- Testing Center Class ---")

    center_1 = Center(
        player_id="C100",
        name="Shaq",
        points=16,
        rebounds=10
    )

    # Inherited method
    center_1.score_points(2)

    # Position-specific method
    center_1.add_rebound()

    # Overridden method
    print(center_1.display_details())

    print("\n--- Testing Polymorphism ---")

    for player in [guard_1, center_1]:
        print(player.display_details())

    