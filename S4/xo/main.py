import random
import uuid


class Player:
    def __init__(self, name):
        self.name = name
        self.id = str(uuid.uuid4())


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.board = [
            ["-7-", "-8-", "-9-"],
            ["-4-", "-5-", "-6-"],
            ["-1-", "-2-", "-3-"],
        ]
        self.selected_choice = []
        self.game_player: Player = random.choice([self.player1, self.player2])
        self.game_player_badge = "x"
        self.winner: Player = None

    def assign_badge_to_board(self, choice):
        self.selected_choice.append(choice)
        match choice:
            case 1:
                self.board[2][0] = self.game_player_badge
            case 2:
                self.board[2][1] = self.game_player_badge
            case 3:
                self.board[2][2] = self.game_player_badge
            case 4:
                self.board[1][0] = self.game_player_badge
            case 5:
                self.board[1][1] = self.game_player_badge
            case 6:
                self.board[1][2] = self.game_player_badge
            case 7:
                self.board[0][0] = self.game_player_badge
            case 8:
                self.board[0][1] = self.game_player_badge
            case 9:
                self.board[0][2] = self.game_player_badge

    def is_valid_choice(self, choice):
        if choice > 9 or choice < 1 or (choice in self.selected_choice):
            return False
        return True

    def get_badge_from_player(self):
        self.print_board()
        choice = int(input(f"{self.game_player.name} please enter your choice : "))
        if self.is_valid_choice(choice):
            self.assign_badge_to_board(choice)
            if self.game_player.id == self.player1.id:
                self.game_player = self.player2
            else:
                self.game_player = self.player1
            self.game_player_badge = "x" if self.game_player_badge == "o" else "o"
            return
        else:
            print("Please repeat")
            self.get_badge_from_player()

    def print_board(self):
        for row in self.board:
            print(row[0], "|", row[1], "|", row[2])

    def is_board_full(self) -> bool:
        for row in self.board:
            for char in row:
                if char != "x" or char != "o":
                    return False

        return True

    def check_winner(self, badge: str) -> bool:
        for row in self.board:
            if row[0] == badge and row[1] == badge and row[2] == badge:
                return True

        for i in range(3):  # 0 1 2:
            if self.board[0][i] == badge and self.board[1][i] == badge and self.board[2][i] == badge:
                return True

        if self.board[0][0] == badge and self.board[1][1] == badge and self.board[2][2] == badge:
            return True

        if self.board[0][2] == badge and self.board[1][1] == badge and self.board[2][0] == badge:
            return True

        return False

    def have_winner(self) -> bool:
        if self.check_winner("x") or self.check_winner("o"):
            self.winner = self.player1 if self.game_player == self.player2 else self.player2
            return True
        return False

    def can_continue(self) -> bool:
        if not self.have_winner() and not self.is_board_full():
            return True
        return False


# validation player choice
# play with pc

p1_name = input("please enter your name (1) : ")
p2_name = input("please enter your name (2) : ")

p1 = Player(p1_name)
p2 = Player(p2_name)

game = Game(p1, p2)

while game.can_continue():
    game.get_badge_from_player()

if game.have_winner():
    print(game.winner.name, "wiiiiiiiiiiiiiin")
else:
    print("board is full")
