class Figure:
    color = 'white'
    place = ('F', 5)

    def set_color_for_figure(self):
        if self.color == 'white':
            self.color = 'black'
        elif self.color == 'black':
            self.color = 'white'
        return f'Color has been changed to {self.color}'

    def set_place_for_figure(self, *coordinates):
        self.place = coordinates
        for i in self.place:
            if type(i) == int and self._is_not_out_of_range():
                return f'You moved figure to this {self.place} coordinates'

        return 'Please check if you typed your coordinates right'

    def _is_not_out_of_range(self):
        for i in self.place:
            if type(i) == int:
                if 0 < i <= 7:
                    return True
                elif 0 > i or i > 7:
                    return 'Please check if you typed your coordinates right'
                return False

    def is_possible_to_move(self, *coordinates):
        ...


class Pawn(Figure):
    def is_possible_to_move(self, *coordinates):
        for i in self.place:
            for j in coordinates:
                if type(i) == str and type(j) == str and i != j:
                    return 'Its impossible to move this figure like this'
                if type(i) == int and type(j) == int:
                    if super()._is_not_out_of_range():
                        num = i - j
                        if num == 1 or num == -1:
                            if self.color == 'black' and num == 1:
                                return f'Its possible to move Pawn on {coordinates}'
                            elif self.color == 'white' and num == -1:
                                return f'Its possible to move Pawn on {coordinates}'
                        else:
                            return 'Its impossible to move Pawn like this'

        return 'Its impossible to move Pawn like this'


class Knight(Figure):
    def is_possible_to_move(self, *coordinates):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        index_check = [1, 2, -1, -2]
        check_for_letter = 0
        check_for_number = 0
        for i in self.place:
            for j in coordinates:
                if type(i) == str and type(j) == str:
                    a = letters.index(i) - letters.index(j)
                    if a in index_check:
                        check_for_letter = 1
                if type(i) == int and type(j) == int:
                    if super()._is_not_out_of_range():
                        num = i - j
                        if num == 3 or num == -3:
                            check_for_number = 1
        if check_for_letter + check_for_number == 2:
            return f'Its possible to move Knight on {coordinates}'

        return 'Its impossible to move Knight like this'


class Rook(Figure):
    def is_possible_to_move(self, *coordinates):
        for i in self.place:
            for j in coordinates:
                if i is j:
                    return f'Its possible to move Rook on {coordinates}'

        return 'Its impossible to move Rook like this'


class Bishop(Figure):
    def is_possible_to_move(self, *coordinates):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        index = 0
        num = 0
        for i in self.place:
            for j in coordinates:
                if type(i) == str and type(j) == str and i is not j:
                    index = letters.index(i) - letters.index(j)
                if type(i) == int and type(j) == int and i != j:
                    if super()._is_not_out_of_range():
                        num = i - j
                    else:
                        return 'Its impossible to move Bishop like this'

                if abs(index) == abs(num) and i != j:
                    return f'Its possible to move Bishop on {coordinates}'
                elif abs(index) == abs(num) == 0:
                    return 'Its impossible to move Bishop like this'

        return 'Its impossible to move Bishop like this'


class Queen(Figure):
    def is_possible_to_move(self, *coordinates):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        index = 0
        num = 0
        for i in self.place:
            for j in coordinates:
                if type(i) == int and type(j) == int:
                    if super()._is_not_out_of_range():
                        num = i - j
                if type(i) == str and type(j) == str and i != j:
                    index = letters.index(i) - letters.index(j)
                if abs(index) == abs(num) or i == j:
                    return f'Its possible to move Queen on {coordinates}'
        return 'Its impossible to move Queen like this'


pawn = Pawn()
print(pawn.set_color_for_figure())
print(pawn.set_place_for_figure('A', 5))
print(pawn.is_possible_to_move('A', 4))

knight = Knight()
print(knight.set_color_for_figure())
print(knight.set_place_for_figure('D', 4))
print(knight.is_possible_to_move('F', 5))

rook = Rook()
print(rook.set_color_for_figure())
print(rook.set_place_for_figure('F', 4))
print(rook.is_possible_to_move('F', 5))

bishop = Bishop()
print(bishop.set_color_for_figure())
print(bishop.set_place_for_figure('E', 5))
print(bishop.is_possible_to_move('F', 4))

queen = Queen()
print(queen.set_color_for_figure())
print(queen.set_place_for_figure('E', 5))
print(queen.is_possible_to_move('F', 4))
