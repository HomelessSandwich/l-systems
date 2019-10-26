from LSystem import LSystem

rule1 = {
    "a": 'F',
    "b": 'F-G+F+G-F'
}

rule2 = {
    "a": 'G',
    "b": 'GG'
}

sierpinski_triangle = LSystem(
    axiom='F-G-G',
    rules=[rule1, rule2],
    angle=120,
    start_pos=(0, 0),
    start_ang=0,
    iterations=5,
    line_len=50,
    screen_size=1000
)

sierpinski_triangle.generate()
