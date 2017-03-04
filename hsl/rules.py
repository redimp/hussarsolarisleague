"""

  rules.py -- all rules necessary for the hussar league

"""

def check_hangar_for_errors(mechs, trials):
    """Check if the selected_mechs and trial_mechs contains any errors"""

    # settings
    min_l = 4
    min_m = 4
    min_h = 4
    min_a = 4

    max_l = 6
    max_m = 6
    max_h = 6
    max_a = 6

    min_total = 18
    max_total = 18

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
    if (l_t + l) > max_l:
        return ['You are only allowed to pick %i Lights.' % max_l ]
    if (l_t == 0 and l < min_l):
        return ['You have to pick %i Lights. You can pick trials as jokers.' % min_l ]
    # check mediums
    if (m_t + m) > max_m:
        return ['You are only allowed to pick %i Mediums.' % max_l ]
    if (m_t == 0 and m < min_m):
        return ['You have to pick %i Mediums. You can pick trials as jokers.' % min_m ]
    # check heavys
    if (h_t + h) > max_h:
        return ['You are only allowed to pick %i Heavys.' % max_h ]
    if (h_t == 0 and h < min_h):
        return ['You have to pick %i Heavys. You can pick trials as jokers.' % min_h ]
    # check assaults
    if (a_t + a) > max_a:
        return ['You are only allowed to pick %i Assaults.' % max_a ]
    if (a_t == 0 and a < min_a):
        return ['You have to pick %i Assaults. You can pick trials as jokers.' % min_a ]

    total_trials = l_t + m_t + h_t + a_t
    total_mechs = l + m + h + a

    if (total_mechs + total_trials > max_total):
        return ['You are only allowed to pick %i Mechs.' % max_total]
    if (total_trials == 0 and total_mechs < min_total):
        return ['You have to pick %i Mechs. You can pick trials as jokers.' % min_total ]

    return None
