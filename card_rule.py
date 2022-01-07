
card_sets = {
    'X':'single',
    'XX':'pair',
    'XXX':'triple',
    'XXXX':'bomb',
    'XXYYY':'FullHouse',
    'YYXXX':'FullHouse',
    'XXYYZZ':'cts-pair',
    'XXYY':'Nukes'
             }


def get_set(cards):
    '''
    :param cards:
    :return: is_valid,set_name,set_value
    '''
    if len(cards) == 0:
        return False,None,None

    if len(cards) == 1:
        return ''