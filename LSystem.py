import turtle
import time


class LSystem():

    def __init__(
        self, axiom, rules, angle, start_pos, start_ang,
        iterations, line_len, screen_size
    ):
        '''
        Inputs:
            axiom | string | The string that starts the L-system generation.

            rules | array of dicts | An array of dicts that contain the rules
            needed to transform sentances. Dicts must be in the form:
                {
                    "a": "F",
                    "b": "FF"
                }
            Where the key a contains the character to be transformed and the
            key b contains the characters that a will transform into. In this
            case: F -> FF

            angle | float | The number of degrees that the turtle will rotate by,
            when going left or right.

            start_pos | tuple of floats | The starting position of the turle.
            E.g. (100, 100)

            start_ang | float | The starting angle of the turtle.

            iterations | integer | The number of iterations the turtle will complete.

            line_len | integer | The length of the line produced each time the turtle
            goes forward.

            screen_size | integer | The amount of pixels that affects the window size
            and the coordinate system. E.g. 1000 -> a window size of 1000 x 1000 and a
            coordinate system that goes from (0, 0) to (1000, 1000)
        '''

        self.axiom = axiom
        self.rules = rules
        self.angle = angle
        self.start_pos = start_pos
        self.start_ang = start_ang
        self.iterations = iterations
        self.line_len = line_len
        self.screen_size = screen_size

    def gen_sentance(self, sentance):
        '''
        Generates a new sentance based of an input sentance and its rules.

        Inputs:
            sentance | string | The L-system string to be transformed.
        '''

        next_sentance = ""

        for c in sentance:
            found = False

            try:
                for rule in self.rules:
                    if c == rule["a"]:
                        next_sentance += rule["b"]
                        found = True
                        break
            except KeyError:
                print('One of the rules did not contain a key of "a" or "b"')

            if not found:
                next_sentance += c

        return next_sentance
