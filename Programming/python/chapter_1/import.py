
import module

print(module.get_morpho3('παιχνιδιού',pos='noun',gender='neutral',case='genitive',number='singular'))

from module import get_morpho3

print(get_morpho3('παιχνιδιού',pos='noun',gender='neutral',case='genitive',number='singular'))

from module import get_morpho2,get_morpho

print(get_morpho('παιχνιδιού','noun','neutral','genitive','singular'))
print(get_morpho2('παιχνιδιού','noun','neutral','genitive','singular'))

import module as m

print(m.get_morpho3('παιχνιδιού',pos='noun',gender='neutral',case='genitive',number='singular'))

from module import get_morpho3 as getm

print(getm('παιχνιδιού',pos='noun',gender='neutral',case='genitive',number='singular'))

from module import *

print(get_morpho('παιχνιδιού','noun','neutral','genitive','singular'))
print(get_morpho2('παιχνιδιού','noun','neutral','genitive','singular'))
print(get_morpho3('παιχνιδιού',pos='noun',gender='neutral',case='genitive',number='singular'))
