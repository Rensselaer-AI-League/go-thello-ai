import ai
import logic

class Game():
    def __init__(self):
        self.running = True
        self.turn = 'X'
        self.board = logic.Board(7, 7)
        self.input = logic.Input()
        self.output = logic.Output()
        self.ai = ai.HeuristicAI(self.board)

    def setup_ai(self):
        self.ai.OT_set_side('O')

    def run(self):
        self.output.welcome()
        self.setup_ai()
        while (self.running):
            self.game()

    def gamestate(self):
        gs = []
        for y in self.board.board:
            for x in y:
                gs.append(x)
        return gs

    def game(self):
        #randomly make player X or O

        self.output.to_move(self.turn)
        self.board.draw()

        if self.board.full():
            x_ct, o_ct = self.board.dominance()
            if x_ct > o_ct:
                self.output.wins("Player 1 (X)", x_ct, o_ct)
                self.ai.OT_set_winner('X')
            elif o_ct > x_ct:
                self.output.wins("Player 2 (O)", o_ct, x_ct)
                self.ai.OT_set_winner('O')
            self.board.reset()
            self.turn = 'X'
            return

        legal_move = False
        while not legal_move:
            action = ''
            if self.turn == 'X':
                self.output.poll_move()
                action = self.input.prompt_move().lower()
            else:
                action = self.ai.OT_get_move().lower() # This is the line that calls the AI move

            if action == 'f':
                self.output.player_forfeit(self.turn)
                self.board.reset()
                self.mode = "menu"
                legal_move = True
            else:
                action = list(action)
                if len(action) == 2:
                    file = ord(action[0]) - 97
                    rank = self.board.hgt - ord(action[1]) + 48
                    
                    if self.board.place(file, rank, self.turn):
                        legal_move = True
                        if self.turn == "X":
                            self.turn = "O"
                        else:
                            self.turn = "X"

                if not legal_move:
                    self.output.illegal_move()
                    if self.turn == "O":
                        print action
                        self.ai.board.draw()
                        print self.ai.board.get_possible_moves()
                        return

if __name__ == "__main__":
    g = Game()
    g.run()
