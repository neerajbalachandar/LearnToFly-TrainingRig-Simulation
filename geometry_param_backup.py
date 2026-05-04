import numpy as np

def get_params():
    return {
        'g': 9.81,
        'ma': 1.0,
        'mb': 1.2,
        'mc': 0.8,

        'Iaxx': 0.02, 'Iayy': 0.02, 'Iazz': 0.02,
        'Iaxy': 0.0,  'Iaxz': 0.0,  'Iayz': 0.0,

        'Ibx': 0.01, 'Iby': 0.01, 'Ibz': 0.01,
        'Icx': 0.01, 'Icy': 0.01, 'Icz': 0.01,

        'xO_A': 0.0, 'yO_A': 0.0, 'zO_A': 0.0,
        'xB_A': 0.1, 'yB_A': 0.0, 'zB_A': 0.0,
        'xC_A': -0.1,'yC_A': 0.0, 'zC_A': 0.0,
}