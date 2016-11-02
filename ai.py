'''
/**
 * The Big Bad GOTHELLO AI
 * Right now it sucks, but one day it will rule
 * TODO:
 *    Pattern matching to avoid holes like X...XX or XX.X.X
 *    Choose move based on some heuristic rather than randomly
 *        -Be more aggressive with edge placement
 *        -Be more safe with captures
 *    Remember moves as blocks, try to avoid touching a block to an enemy piece
 */
 '''

import random

class HeuristicAI:
    # Now with less documentation!

    def __init__(self, board):
        self.playing = True
        self.board = board
        self.corners = [False for i in range(4)]

        self.directions = [(-1, -1), (-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (1, -1), (-1, 1)]

    def OT_set_side(self, side):
        self.playing = True
        self.side = side
        self.opp_side = 'X'
        if side == 'X':
            self.opp_side = 'O'

    def OT_get_move(self):
        return self.print_move(self.make_move())

    def OT_set_winner(self, result):
        self.playing = False
        self.corners = [False for i in range(4)]

    def print_move(self, move):
        x,y = move

        x = str(unichr(x+97))
        y = str(y+1)

        return x+y

    def analyze_position(self):
        return -1

    def is_corner(self, mv):
        return mv in [(0,0), (0, self.board.hgt), (self.board.wdt, 0), (self.board.wdt, self.board.hgt)]

    def filter_corners(self, ls):
        return [mv for mv in ls if is_corner(mv)]

    def is_edge(self, mv):
        return mv[0] in [0, self.board.wdt] or mv[1] in [0, self.board.hgt]

    def filter_edges(self, ls):
        return [mv for mv in ls if is_edge(ls)]

    def need(self, mv):
        if self.corners[0] and self.corners[1]:
            return mv[0] == 0

        if self.corners[1] and self.corners[2]:
            return y == 0

        if self.corners[2] and self.corners[3]:
            return x == self.board.width

        if self.corners[3] and self.corners[0]:
            return y == self.board.height

    def filter_needed(self, ls):
        return [mv for mv in ls if need(mv)]

    #dtn is direction, dir is taken :(
    def is_capture(self, mv, safe, first):
        for dtn in self.directions:
            nm = (mv[0] + dtn[0], mv[1] + dtn[0])

            if not self.board.in_bounds(nm[0], nm[1]):
                continue
            elif self.board.get(nm[0], nm[1]) == '.':
                continue
            elif self.board.get(nm[0], nm[1]) == self.side and (not first or safe):
                return True
            elif self.board.get(nm[0], nm[1]) == self.opp_side:
                if self.is_capture(nm, dtn, safe, False):
                    return True
                else:
                    continue

    def check_captures(self, ls, safe):
        out = []

        for mv in ls:
            return [mv for mv in ls if self.is_capture(mv, safe, True)]

    def filter_captures(self, ls):
        return self.check_captures(ls, False)

    def filter_safes(self, ls):
        return self.check_captures(ls, True)

    def is_odd_edge(self, mv, turn):
        # A bad edge is one that contains an odd number of empty squares
        return false # If you want a challenge, implement this to make the heuristic better

    def filter_odd_edges(self, ls, turn):
        return [mv for mv in ls if is_odd_edge(mv)]

    def make_move(self):
        legal_moves = [] #get empty squares from board
        corners = self.filter_corners(legal_moves)
        edges = self.filter_edges(legal_moves)
        captures = self.filter_captures(legal_moves)
        safes = self.filter_safes(legal_moves)
        edge_caps = self.filter_captures(edges)
        edge_safes = self.filter_safes(edges)
        edge_needs = self.filter_needed(edge_safes)

        if corners:
            out = r.choice(corners)

            if (out[0] == 0 and out[1] == self.board.hgt):
                this.corners[0] = True
            elif (out[0] == 0 and out[1] == 0):
                this.corners[1] = True
