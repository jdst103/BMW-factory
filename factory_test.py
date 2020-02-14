from factory_functions import *
print(build_shiny_parts('metal', 'labour') == 'shiny parts')
print('Got:', build_shiny_parts('metal', 'labour'))

print('testing build_car() with "shiny parts". Expected Utimate driving experience')
print(build_car('shiny parts') == 'Utimate driving experience')
print('got:', build_car('shiny parts'))

print('testing run_factory() with "metal" and "labour". Expect "Utimate driving experience"')
print(run_factory('metal','labour') == 'Utimate driving experience')
print('got;', run_factory('metal','labour'))