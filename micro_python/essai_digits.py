# Définir les broches pour chaque segment et le point décimal

x = 200   # steps
y = 30    # degrés !


class DrawingSystem():
    def __init__(self, type):
        self.type = type

    def draw_segment(self, A, B):
        if self.type == 'tube_writter':
            print(f"Dessine de {A} à {B}")
        elif self.type == 'pen_drawing':
            print(f"Trace de {A} à {B}")

    def avance(self):
        if self.type == 'tube_writter':
            print(f"Avance de {x * 1.1} ")

    def up(self):
        pass

    def down(self):
        pass

class Segments():
    # on doit définir les Segments :
    segments = {0: [[0, 0], [x, 0]],
                1: [[x, 0], [x, y]],
                2: [[x, y], [x, 2 * y]],
                3: [[x, 2 * y], [0, 2 * y]],
                4: [[0, 2 * y], [0, y]],
                5: [[0, y], [0, 0]],
                6: [[0, y], [x, y]],
                'dot': [[int(x + 1.1), 2 * y], [int(x + 1.1), 2 * y]]
                }

    # Définition des chiffres et de leur configuration respective
    # Le 0 est en haut, on tourne dans le sens horaire, puis le 6 est la
    # barre du milieu. Le dot est le point.
    numbers = {
        0: (1, 1, 1, 1, 1, 1, 0),
        1: (0, 1, 1, 0, 0, 0, 0),
        2: (1, 1, 0, 1, 1, 0, 1),
        3: (1, 1, 1, 1, 0, 0, 1),
        4: (0, 1, 1, 0, 0, 1, 1),
        5: (1, 0, 1, 1, 0, 1, 1),
        6: (1, 0, 1, 1, 1, 1, 1),
        7: (1, 1, 1, 0, 0, 0, 0),
        8: (1, 1, 1, 1, 1, 1, 1),
        9: (1, 1, 1, 1, 0, 1, 1)
,    }

    def __init__(self, effector):
        pass
        self.effector = effector

    def segment_on(self, num_seg):
        seg = self.segments[num_seg]
        draw(seg[0], seg[1])

    def segment_off(self, num_seg):
        pass


# Fonction pour afficher un chiffre avec un point décimal
    def display_digit(self, number):
        if number in self.numbers:
            for s, state in enumerate(self.numbers[number], start=0):
                if state:
                    S = self.segments[s]
                    self.effector.draw_segment(S[0], S[1])
                # self.segments[s].value = state
            # self.dot.value = 1  # Allumer le point décimal si nécessaire
        else:
            pass

    def display_text(self, text):
        for letter in text:
            self.display_digit(int(letter))  # PAS logieque : ordre à donner au robot
            self.effector.avance()



if __name__ == '__main__':
    print("Beginning...")
    tube_writter = DrawingSystem('tube_writter')

    S = Segments(tube_writter)
    S.display_digit(2)
    S.display_text("282")

