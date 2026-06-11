def get_quad_params():
    return {
        'model_name': 'LiteWing',
        'spec_source_url': 'https://circuitdigest.com/wiki/litewing/',
        'frame_span_m': 0.1,
        'quad_l': 0.05,
    }

def get_params():
    return {
        'g': 9.81,
        'ma': 0.5,
        'mb': 0.045,
        'mc': 0.06,
        'Iaxx': 0.00183545735083,
        'Iayy': 0.0102709090504,
        'Iazz': 0.00843570169962,
        'Iaxy': 0,
        'Iaxz': 0.0027371070607,
        'Iayz': 0,
        'Ibx': 5.625e-05,
        'Iby': 5.625e-05,
        'Ibz': 0.0001125,
        'Icx': 0.03,
        'Icy': 0.025,
        'Icz': 0.02,
        'xO_A': 0.0184421935367,
        'yO_A': 0,
        'zO_A': -0.0530188793112,
        'xB_A': 0.159999998311,
        'yB_A': 0,
        'zB_A': 0,
        'xC_A': -0.26,
        'yC_A': 0,
        'zC_A': 0,
    }