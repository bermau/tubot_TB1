# Définir les broches pour chaque segment et le point décimal



class DrawingSystem():
    def __init__(self, type):
        self.type = type
        if type == 'tube_writter':
            self.x = 200    # steps
            self.y = 30     # degrees


    def draw_segment(self, A, B):
        if self.type == 'tube_writter':
            print(f"Dessine de {A} à {B}")
        elif self.type == 'pen_drawing':
            print(f"Trace de {A} à {B}")

    def avance(self):
        if self.type == 'tube_writter':
            print(f"Avance de {self.x * 1.1} ")

    def up(self):
        pass

    def down(self):
        pass

class Segments():
    # on doit définir les Segments :
    segments = {0: [[0, 0], [1, 0]],
                1: [[1, 0], [1, 1]],
                2: [[1, 1], [1, 2]],
                3: [[1, 2 ], [0, 2 ]],
                4: [[0, 2], [0, 1]],
                5: [[0, 1], [0, 0]],
                6: [[0, 1], [1, 1]],
                'dot': [[int(1 + 1.1), 2], [int(1 + 1.1), 2]]
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

class Main():
    def __int__(self, tw, segments):
        self.tool = tw
        self.seg = segments

    def display_text(self, txt):
        for letter in txt:
            self.tool.


if __name__ == '__main__':
    tw = DrawingSystem('tube_writter')
    s = Segments(tw)
    m = Main(tw, s)

    m.display_text("282")
