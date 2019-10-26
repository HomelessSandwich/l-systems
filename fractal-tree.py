from LSystem import LSystem

rule1 = {
    "a": 'F',
    "b": 'FF'
}

rule2 = {
    "a": 'L',
    "b": 'F[L]L'
}

system = LSystem(
    axiom='L',
    rules=[rule1, rule2],
    angle=45,
    start_pos=(500, 0),
    start_ang=90,
    iterations=7,
    line_len=10,
    screen_size=1000
)

system.generate()
