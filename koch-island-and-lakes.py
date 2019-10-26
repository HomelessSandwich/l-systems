from LSystem import LSystem

rule1 = {
    "a": 'F',
    "b": 'F+G-FF+F+FF+FG+FF-G+FF-F-FF-FG-FFF'
}

rule2 = {
    "a": 'G',
    "b": 'GGGGGG'
}

system = LSystem(
    axiom='F+F+F+F',
    rules=[rule1, rule2],
    angle=90,
    start_pos=(250, 250),
    start_ang=90,
    iterations=4,
    line_len=5,
    screen_size=2000
)

system.generate()
