from LSystem import LSystem

rule1 = {
    "a": 'F',
    "b": 'FF'
}

rule2 = {
    "a": 'X',
    "b": '+F+F[+Y]-F[+X+F+X]-F-FF[-Y][+X]FF'
}

rule3 = {
    "a": 'Y',
    "b": 'X'
}

system = LSystem(
    axiom='X',
    rules=[rule1, rule2, rule3],
    angle=15,
    start_pos=(750, 0),
    start_ang=130,
    iterations=9,
    line_len=2,
    screen_size=2500
)

system.generate()
