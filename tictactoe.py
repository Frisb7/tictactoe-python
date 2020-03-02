import os

class boards :

    def __init__(self) :
        self.board = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.player = 'X'

    def boards_display(self) :
        print("\nPlayer : {}\n".format(self.player))
        print(" {} | {} | {}".format(self.board[1], self.board[2], self.board[3]))
        print("---+---+---")
        print(" {} | {} | {}".format(self.board[4], self.board[5], self.board[6]))
        print("---+---+---")
        print(" {} | {} | {}".format(self.board[7], self.board[8], self.board[9]))

    def check_win(self) :
        l = self.board
        for i in [1, 4, 7] :
            if (l[i] != ' ' and l[i] == l[i+1] == l[i+2]) :
                print("\nPlayer {} wins".format(self.player))
                self.quit()
                break
        for i in [1, 2, 3] :
            if (l[i] != ' ' and l[i] == l[i+3] == l[i+6]) :
                print("\nPlayer {} wins".format(self.player))
                self.quit()
                break
        if (l[1] != ' ' and l[1] == l[5] == l[9]) :
            print("\nPlayer {} wins".format(self.player))
            self.quit()
        elif (l[3] != ' ' and l[3] == l[5] == l[7]) :
            print("\nPlayer {} wins".format(self.player))
            self.quit()

    def place(self) :
        n = int(input("\n>>> "))
        if n not in range(1,10) :
            print("\nerror:INVALID INPUT - try again")
            self.boards_display()
        else :
            if self.board[n] != ' ' :
                print("\nerror:INVALID INPUT - try again")
                self.boards_display()
            else :
                self.board[n] = self.player

    def next_player(self) :
        if self.player == 'X' :
            self.player = 'O'
        else :
            self.player = 'X'

    def main(self) :
        if os.name == 'nt' :
            os.system('cls')
        else :
            os.system('clear')
        self.boards_display()
        self.check_win()
        self.place()
        self.next_player()
        self.main()

    def quit(self) :
        play = str(input("\nDo you want to play again?(y/n) :"))
        if play == 'n' :
            exit()
        elif play == 'y' :
            self.board = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            self.main()
        else :
            print("\nerror:INVALID INPUT - try again")
            self.quit()

if __name__ == "__main__":
    game = boards()
    game.main()