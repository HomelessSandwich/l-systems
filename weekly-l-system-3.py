from LSystem import LSystem

rule1 = {
    "a": 'F',
    "b": '+F--F+'
}

system = LSystem(
    axiom='F+F+F+F+F+F+F+F',
    rules=[rule1],
    angle=45,
    start_pos=(750, 1800),
    start_ang=0,
    iterations=13,
    line_len=8,
    screen_size=2000
)

system.generate()
