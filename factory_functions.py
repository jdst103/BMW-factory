def build_shiny_parts(arg1, arg2):
    if arg1 == 'metal' and arg2 == 'labour':
        return 'shiny parts'
    else:
        return 'no shiny parts'

def build_car(arg1):
    if arg1 == 'shiny parts':
        return 'Utimate driving experience'
    else:
        return 'lump of metal... or bread maybe..'

def run_factory(arg1, arg2):
    make_shiny_part = build_shiny_parts(arg1, arg2)
    make_car = build_car(make_shiny_part)
    return make_car
