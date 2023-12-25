#   TYPE = ([STRONG AGAINST], [WEAK AGAINST], [NO EFFECT])

NORMAL = ([],
          ['rock','steel'],
          ['ghost'])

FIRE = (['grass','ice','bug','steel'],
        ['fire','water','rock','dragon'],
        [])

WATER = (['fire','ground','rock'],
         ['water','grass','dragon'],
         [])

ELECTRIC = (['water','flying'],
            ['electric','grass','dragon'],
            ['ground'])

GRASS = (['water','ground','rock'],
         ['fire','grass','poison','flying','bug','dragon','steel'],
         [])

ICE = (['grass','ground','flying','dragon'],
       ['fire','water','ice','steel'],
       [])

FIGHTING = (['normal','ice','rock','dark','steel'],
            ['poison','flying','psychic','bug','fairy'],
            ['ghost'])

POISON = (['grass','fairy'], 
          ['poison','ground','rock','ghost'],
          ['steel'])

GROUND = (['fire','electric','poison','rock','steel'],
          ['grass','bug'],
          ['flying'])

FLYING = (['grass','fighting','bug'],
          ['electric','rock','steel'],
          [])

PSYCHIC = (['fighting','poison'],
           ['psychic','steel'],
           ['dark'])

BUG = (['grass','psychic','dark'],
       ['fire','fighting','poison','flying','ghost','steel','fairy'],
       [])

ROCK = (['fire','ice','flying','bug'],
        ['fighting','ground','steel'],
        [])

GHOST = (['psychic','ghost'],
         ['dark'],
         ['normal'])

DRAGON = (['dragon'],
          ['steel'],
          ['fairy'])

DARK = (['psychic','ghost'],
        ['fighting','dark','fairy'],
        [])

STEEL = (['ice','rock','fairy'],
         ['fire','water','electric','steel'],
         [])

FAIRY = (['fighting','dragon','dark'],
         ['fire','poison','dark'],
         [])


def tally(pokemon, type_dict):
    for type in pokemon:
        for type_key in type_dict:
            effectiveness = globals()[type_key.upper()]
            if type in effectiveness[0]:  #checking strengths
                type_dict[type_key] -= 1
            if type in effectiveness[1]:  #checking weaknesses
                type_dict[type_key] += 1
            if type in effectiveness[2]:
                type_dict[type_key] += 2
    
    return type_dict

def main():
    team = (['fire'],['psychic','flying'], ['flying','poison'], ['water','flying'], ['fighting'])
    type_dict = {
        'normal' : 0, 'fire' : 0, 'water' : 0, 'electric' : 0,
        'grass' : 0, 'ice' : 0, 'fighting' : 0, 'poison' : 0,
        'ground' : 0, 'flying' : 0, 'psychic' : 0, 'bug' : 0,
        'rock' : 0, 'ghost' : 0, 'dragon' : 0, 'steel' : 0, 'fairy' : 0
        }
    for pokemon in team:
        tally(pokemon, type_dict)

    print(type_dict)

main()