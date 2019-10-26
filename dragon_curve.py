from LSystem import LSystem

rule1 = {
    "a": 'X',
    "b": 'X+YF+'
}

rule2 = {
    "a": 'Y',
    "b": '-FX-Y'
}

dragon_curve = LSystem(
    axiom='FX',
    rules=[rule1, rule2],
    angle=90,
    start_pos=(500, 500),
    start_ang=90,
    iterations=15,
    line_len=5,
    screen_size=1000
)

dragon_curve.generate()
