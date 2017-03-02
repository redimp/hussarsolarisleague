"""

  rules.py -- all rules necessary for the hussar league

"""

def check_hangar_for_errors(mechs, trials):
    """Check if the selected_mechs and trial_mechs contains any errors"""

    # settings
    must_l = 3
    must_m = 3
    must_h = 3
    must_a = 3

    # count mechs
    l = len([x for x in mechs if x.weightclass == 'Light'])
    m = len([x for x in mechs if x.weightclass == 'Medium'])
    h = len([x for x in mechs if x.weightclass == 'Heavy'])
    a = len([x for x in mechs if x.weightclass == 'Assault'])
    # count trials
    l_t = len([x for x in trials if x.weightclass == 'Light'])
    m_t = len([x for x in trials if x.weightclass == 'Medium'])
    h_t = len([x for x in trials if x.weightclass == 'Heavy'])
    a_t = len([x for x in trials if x.weightclass == 'Assault'])

    # print trials
    # print "l: %i m: %i h: %i a: %i" % (l,m,h,a)
    # print "t_l: %i t_m: %i t_h: %i t_a: %i" % (l_t,m_t,h_t,a_t)

    double_picks = list(set(mechs) & set(trials))

    if len(double_picks)>0:
        return ['You are not to allowed %s as both trial and owned mech.' % x.name for x in double_picks]

    # check lights
    if (l_t + l) > must_l:
        return ['You are only allowed to pick %i Lights.' % must_l ]
    if (l_t == 0 and l < must_l):
        return ['You have to pick %i Lights. You can pick trials as jokers.' % must_l ]
    # check mediums
    if (m_t + m) > must_m:
        return ['You are only allowed to pick %i Mediums.' % must_m ]
    if (m_t == 0 and m < must_m):
        return ['You have to pick %i Mediums. You can pick trials as jokers.' % must_m ]
    # check heavys
    if (h_t + h) > must_h:
        return ['You are only allowed to pick %i Heavys.' % must_h ]
    if (h_t == 0 and h < must_h):
        return ['You have to pick %i Heavys. You can pick trials as jokers.' % must_h ]
    # check assaults
    if (a_t + a) > must_a:
        return ['You are only allowed to pick %i Assaults.' % must_a ]
    if (a_t == 0 and a < must_a):
        return ['You have to pick %i Assaults. You can pick trials as jokers.' % must_a ]

    return None
