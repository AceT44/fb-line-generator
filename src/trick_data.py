ACCEPTABLE_STANCES = {
    'regular': 'nollie',
    'fakie': 'switch',
    'nollie': 'regular',
    'switch': 'fakie'
}

TRICKS = {
    'manual': {
        'difficulty': 1,
        'category': 'manual',
        'stance': 'regular'
    },
    'fakie manual': {
        'difficulty': 2,
        'category': 'manual',
        'stance': 'fakie'
    },
    'nollie manual': {
        'difficulty': 2,
        'category': 'manual',
        'stance': 'nollie'
    },
    'switch manual': {
        'difficulty': 1,
        'category': 'manual',
        'stance': 'switch'
    },
    'ollie': {
        'difficulty': 1,
        'category': 'ollie',
        'stance': 'regular'
    },
    'fakie ollie': {
        'difficulty': 1,
        'category': 'ollie',
        'stance': 'fakie'
    },
    'nollie': {
        'difficulty': 1,
        'category': 'ollie',
        'stance': 'nollie'
    },
    'switch ollie': {
        'difficulty': 1,
        'category': 'ollie',
        'stance': 'switch'
    },
    'BS shuvit': {
        'difficulty': 1,
        'category': 'spin',
        'stance': 'regular'
    },
    'fakie BS shuvit': {
        'difficulty': 1,
        'category': 'spin',
        'stance': 'fakie'
    },
    'nollie BS shuvit': {
        'difficulty': 2,
        'category': 'spin',
        'stance': 'nollie'
    },
    'switch BS shuvit': {
        'difficulty': 2,
        'category': 'spin',
        'stance': 'switch'
    },
    'FS shuvit': {
        'difficulty': 2,
        'category': 'spin',
        'stance': 'regular'
    },
    'fakie FS shuvit': {
        'difficulty': 2,
        'category': 'spin',
        'stance': 'fakie'
    },
    'nollie FS shuvit': {
        'difficulty': 2,
        'category': 'spin',
        'stance': 'nollie'
    },
    'switch FS shuvit': {
        'difficulty': 2,
        'category': 'spin',
        'stance': 'switch'
    },
    'FS 180': {
        'difficulty': 1,
        'category': 'rotation',
        'stance': 'regular'
    },
    'fakie FS 180': {
        'difficulty': 1,
        'category': 'rotation',
        'stance': 'fakie'
    },
    'nollie FS 180': {
        'difficulty': 2,
        'category': 'rotation',
        'stance': 'nollie'
    },
    'switch FS 180': {
        'difficulty': 2,
        'category': 'rotation',
        'stance': 'switch'
    },
    'BS 180': {
        'difficulty': 1,
        'category': 'rotation',
        'stance': 'regular'
    },
    'half cab': {
        'difficulty': 1,
        'category': 'rotation',
        'stance': 'fakie'
    },
    'nollie BS 180': {
        'difficulty': 2,
        'category': 'rotation',
        'stance': 'nollie'
    },
    'switch BS 180': {
        'difficulty': 2,
        'category': 'rotation',
        'stance': 'switch'
    },
    'kickflip': {
        'difficulty': 2,
        'category': 'flip',
        'stance': 'regular'
    },
    'fakie kickflip': {
        'difficulty': 2,
        'category': 'flip',
        'stance': 'fakie'
    },
    'nollie kickflip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'nollie'
    },
    'switch kickflip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'switch'
    },
    'FS kickflip': {
        'difficulty': 2,
        'category': 'flip',
        'stance': 'regular'
    },
    'fakie FS kickflip': {
        'difficulty': 2,
        'category': 'flip',
        'stance': 'fakie'
    },
    'nollie FS kickflip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'nollie'
    },
    'switch FS kickflip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'switch'
    },
    'BS kickflip': {
        'difficulty': 2,
        'category': 'flip',
        'stance': 'regular'
    },
    'half cab flip': {
        'difficulty': 2,
        'category': 'flip',
        'stance': 'fakie'
    },
    'nollie BS kickflip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'nollie'
    },
    'switch BS kickflip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'switch'
    },
    'hardflip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'regular'
    },
    'fakie hardflip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'fakie'
    },
    'nollie hardflip': {
        'difficulty': 4,
        'category': 'flip',
        'stance': 'nollie'
    },
    'switch hardflip': {
        'difficulty': 4,
        'category': 'flip',
        'stance': 'switch'
    },
    'varial flip': {
        'difficulty': 2,
        'category': 'flip',
        'stance': 'regular'
    },
    'fakie varial flip': {
        'difficulty': 2,
        'category': 'flip',
        'stance': 'fakie'
    },
    'nollie varial flip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'nollie'
    },
    'switch varial flip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'switch'
    },
    'treflip': {
        'difficulty': 2,
        'category': 'flip',
        'stance': 'regular'
    },
    'fakie treflip': {
        'difficulty': 2,
        'category': 'flip',
        'stance': 'fakie'
    },
    'nollie treflip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'nollie'
    },
    'switch treflip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'switch'
    },
    '540 flip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'regular'
    },
    'fakie 540 flip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'fakie'
    },
    'nollie 540 flip': {
        'difficulty': 4,
        'category': 'flip',
        'stance': 'nollie'
    },
    'switch 540 flip': {
        'difficulty': 4,
        'category': 'flip',
        'stance': 'switch'
    },
    'heelflip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'regular'
    },
    'fakie heelflip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'fakie'
    },
    'nollie heelflip': {
        'difficulty': 4,
        'category': 'flip',
        'stance': 'nollie'
    },
    'switch heelflip': {
        'difficulty': 4,
        'category': 'flip',
        'stance': 'switch'
    },
    'FS heelflip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'regular'
    },
    'fakie FS heelflip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'fakie'
    },
    'nollie FS heelflip': {
        'difficulty': 5,
        'category': 'flip',
        'stance': 'nollie'
    },
    'switch FS heelflip': {
        'difficulty': 4,
        'category': 'flip',
        'stance': 'switch'
    },
    'BS heelflip': {
        'difficulty': 4,
        'category': 'flip',
        'stance': 'regular'
    },
    'half cab heel': {
        'difficulty': 4,
        'category': 'flip',
        'stance': 'fakie'
    },
    'nollie BS heelflip': {
        'difficulty': 5,
        'category': 'flip',
        'stance': 'nollie'
    },
    'switch BS heelflip': {
        'difficulty': 5,
        'category': 'flip',
        'stance': 'switch'
    },
    'varial heel': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'regular'
    },
    'fakie varial heel': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'fakie'
    },
    'nollie varial heel': {
        'difficulty': 4,
        'category': 'flip',
        'stance': 'nollie'
    },
    'switch varial heel': {
        'difficulty': 5,
        'category': 'flip',
        'stance': 'switch'
    },
    'laserflip': {
        'difficulty': 4,
        'category': 'flip',
        'stance': 'regular'
    },
    'fakie laserflip': {
        'difficulty': 4,
        'category': 'flip',
        'stance': 'fakie'
    },
    'nollie laserflip': {
        'difficulty': 5,
        'category': 'flip',
        'stance': 'nollie'
    },
    'switch laserflip': {
        'difficulty': 5,
        'category': 'flip',
        'stance': 'switch'
    },
    '540 heel': {
        'difficulty': 5,
        'category': 'flip',
        'stance': 'regular'
    },
    'fakie 540 heel': {
        'difficulty': 5,
        'category': 'flip',
        'stance': 'fakie'
    },
    'nollie 540 heel': {
        'difficulty': 5,
        'category': 'flip',
        'stance': 'nollie'
    },
    'switch 540 heel': {
        'difficulty': 5,
        'category': 'flip',
        'stance': 'switch'
    },
    'inward heel': {
        'difficulty': 5,
        'category': 'flip',
        'stance': 'regular'
    },
    'fakie inward heel': {
        'difficulty': 5,
        'category': 'flip',
        'stance': 'fakie'
    },
    'nollie inward heel': {
        'difficulty': 5,
        'category': 'flip',
        'stance': 'nollie'
    },
    'switch inward heel': {
        'difficulty': 5,
        'category': 'flip',
        'stance': 'switch'
    },
    'BS bigspin': {

        'difficulty': 3,
        'category': 'spin',
        'stance': 'regular'
    },
    'fakie BS bigspin': {
        'difficulty': 3,
        'category': 'spin',
        'stance': 'fakie'
    },
    'nollie BS bigspin': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'nollie'
    },
    'switch BS bigspin': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'switch'
    },
    'FS bigspin': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'regular'
    },
    'fakie FS bigspin': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'fakie'
    },
    'nollie FS bigspin': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'nollie'
    },
    'switch FS bigspin': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'switch'
    },
    'BS 360 shuvit': {
        'difficulty': 2,
        'category': 'spin',
        'stance': 'regular'
    },
    'fakie BS 360 shuvit': {
        'difficulty': 2,
        'category': 'spin',
        'stance': 'fakie'
    },
    'nollie BS 360 shuvit': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'nollie'
    },
    'switch BS 360 shuvit': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'switch'
    },
    'FS 360 shuvit': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'regular'
    },
    'fakie FS 360 shuvit': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'fakie'
    },
    'nollie FS 360 shuvit': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'nollie'
    },
    'switch FS 360 shuvit': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'switch'
    },
    'BS 540 shuvit': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'regular'
    },
    'fakie BS 540 shuvit': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'fakie'
    },
    'nollie BS 540 shuvit': {
        'difficulty': 5,
        'category': 'spin',
        'stance': 'nollie'
    },
    'switch BS 540 shuvit': {
        'difficulty': 5,
        'category': 'spin',
        'stance': 'switch'
    },
    'FS 540 shuvit': {
        'difficulty': 5,
        'category': 'spin',
        'stance': 'regular'
    },
    'fakie FS 540 shuvit': {
        'difficulty': 5,
        'category': 'spin',
        'stance': 'fakie'
    },
    'nollie FS 540 shuvit': {
        'difficulty': 5,
        'category': 'spin',
        'stance': 'nollie'
    },
    'switch FS 540 shuvit': {
        'difficulty': 5,
        'category': 'spin',
        'stance': 'switch'
    },
    'bigflip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'regular'
    },
    'fakie bigflip': {
        'difficulty': 3,
        'category': 'flip',
        'stance': 'fakie'
    },
    'nollie bigflip': {
        'difficulty': 4,
        'category': 'flip',
        'stance': 'nollie'
    },
    'switch bigflip': {
        'difficulty': 4,
        'category': 'flip',
        'stance': 'switch'
    },
    'bigheel': {
        'difficulty': 4,
        'category': 'flip',
        'stance': 'regular'
    },
    'fakie bigheel': {
        'difficulty': 4,
        'category': 'flip',
        'stance': 'fakie'
    },
    'nollie bigheel': {
        'difficulty': 5,
        'category': 'flip',
        'stance': 'nollie'
    },
    'switch bigheel': {
        'difficulty': 5,
        'category': 'flip',
        'stance': 'switch'
    },
    'impossible': {
        'difficulty': 2,
        'category': 'spin',
        'stance': 'regular'
    },
    'fakie impossible': {
        'difficulty': 2,
        'category': 'spin',
        'stance': 'fakie'
    },
    'nollie impossible': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'nollie'
    },
    'switch impossible': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'switch'
    },
    'front finger impossible': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'regular'
    },
    'fakie front finger impossible': {
        'difficulty': 4,
        'category': 'spin',
        'stance': 'fakie'
    },
    'nollie front finger impossible': {
        'difficulty': 5,
        'category': 'spin',
        'stance': 'nollie'
    },
    'switch front finger impossible': {
        'difficulty': 5,
        'category': 'spin',
        'stance': 'switch'
    },
    'FS boardslide': {
        'difficulty': 1,
        'category': 'slide',
        'stance': 'regular'
    },
    'fakie FS boardslide': {
        'difficulty': 1,
        'category': 'slide',
        'stance': 'fakie'
    },
    'nollie FS boardslide': {
        'difficulty': 2,
        'category': 'slide',
        'stance': 'nollie'
    },
    'switch FS boardslide': {
        'difficulty': 2,
        'category': 'slide',
        'stance': 'switch'
    },
    'BS boardslide': {
        'difficulty': 1,
        'category': 'slide',
        'stance': 'regular'
    },
    # 'fakie BS boardslide': {
    #     'difficulty': 4,
    #     'category': 'slide',
    #     'stance': 'fakie'
    # },
    # 'nollie BS boardslide': {
    #     'difficulty': 4,
    #     'category': 'slide',
    #     'stance': 'nollie'
    # },
    'switch BS boardslide': {
        'difficulty': 2,
        'category': 'slide',
        'stance': 'switch'
    },
    'FS lipslide': {
        'difficulty': 2,
        'category': 'slide',
        'stance': 'regular'
    },
    'fakie FS lipslide': {
        'difficulty': 2,
        'category': 'slide',
        'stance': 'fakie'
    },
    'nollie FS lipslide': {
        'difficulty': 2,
        'category': 'slide',
        'stance': 'nollie'
    },
    'switch FS lipslide': {
        'difficulty': 3,
        'category': 'slide',
        'stance': 'switch'
    },
    'BS lipslide': {
        'difficulty': 4,
        'category': 'slide',
        'stance': 'regular'
    },
    # 'fakie BS lipslide': {
    #     'difficulty': 5,
    #     'category': 'slide',
    #     'stance': 'fakie'
    # },
    # 'nollie BS lipslide': {
    #     'difficulty': 5,
    #     'category': 'slide',
    #     'stance': 'nollie'
    # },
    'switch BS lipslide': {
        'difficulty': 4,
        'category': 'slide',
        'stance': 'switch'
    },
    'FS bluntslide': {
        'difficulty': 4,
        'category': 'slide',
        'stance': 'regular'
    },
    'fakie FS bluntslide': {
        'difficulty': 4,
        'category': 'slide',
        'stance': 'fakie'
    },
    'nollie FS bluntslide': {
        'difficulty': 4,
        'category': 'slide',
        'stance': 'nollie'
    },
    'switch FS bluntslide': {
        'difficulty': 4,
        'category': 'slide',
        'stance': 'switch'
    },
    'BS bluntslide': {
        'difficulty': 2,
        'category': 'slide',
        'stance': 'regular'
    },
    # 'fakie BS bluntslide': {
    #     'difficulty': 5,
    #     'category': 'slide',
    #     'stance': 'fakie'
    # },
    # 'nollie BS bluntslide': {
    #     'difficulty': 5,
    #     'category': 'slide',
    #     'stance': 'nollie'
    # },
    'switch BS bluntslide': {
        'difficulty': 5,
        'category': 'slide',
        'stance': 'switch'
    },
    'FS noseblunt': {
        'difficulty': 3,
        'category': 'slide',
        'stance': 'regular'
    },
    'fakie FS noseblunt': {
        'difficulty': 3,
        'category': 'slide',
        'stance': 'fakie'
    },
    'nollie FS noseblunt': {
        'difficulty': 3,
        'category': 'slide',
        'stance': 'nollie'
    },
    'switch FS noseblunt': {
        'difficulty': 4,
        'category': 'slide',
        'stance': 'switch'
    },
    'BS noseblunt': {
        'difficulty': 4,
        'category': 'slide',
        'stance': 'regular'
    },
    # 'fakie BS noseblunt': {
    #     'difficulty': 5,
    #     'category': 'slide',
    #     'stance': 'fakie'
    # },
    # 'nollie BS noseblunt': {
    #     'difficulty': 5,
    #     'category': 'slide',
    #     'stance': 'nollie'
    # },
    'switch BS noseblunt': {
        'difficulty': 4,
        'category': 'slide',
        'stance': 'switch'
    },
    'FS tailslide': {
        'difficulty': 1,
        'category': 'slide',
        'stance': 'regular'
    },
    'fakie FS tailslide': {
        'difficulty': 2,
        'category': 'slide',
        'stance': 'fakie'
    },
    'nollie FS tailslide': {
        'difficulty': 3,
        'category': 'slide',
        'stance': 'nollie'
    },
    'switch FS tailslide': {
        'difficulty': 4,
        'category': 'slide',
        'stance': 'switch'
    },
    # 'BS tailslide': {
    #     'difficulty': 4,
    #     'category': 'slide',
    #     'stance': 'regular'
    # },
    # 'fakie BS tailslide': {
    #     'difficulty': 5,
    #     'category': 'slide',
    #     'stance': 'fakie'
    # },
    # 'nollie BS tailslide': {
    #     'difficulty': 5,
    #     'category': 'slide',
    #     'stance': 'nollie'
    # },
    # 'switch BS tailslide': {
    #     'difficulty': 5,
    #     'category': 'slide',
    #     'stance': 'switch'
    # },
    'FS noseslide': {
        'difficulty': 3,
        'category': 'slide',
        'stance': 'regular'
    },
    'fakie FS noseslide': {
        'difficulty': 3,
        'category': 'slide',
        'stance': 'fakie'
    },
    'nollie FS noseslide': {
        'difficulty': 4,
        'category': 'slide',
        'stance': 'nollie'
    },
    'switch FS noseslide': {
        'difficulty': 2,
        'category': 'slide',
        'stance': 'switch'
    },
    'BS noseslide': {
        'difficulty': 2,
        'category': 'slide',
        'stance': 'regular'
    },
    # 'fakie BS noseslide': {
    #     'difficulty': 5,
    #     'category': 'slide',
    #     'stance': 'fakie'
    # },
    # 'nollie BS noseslide': {
    #     'difficulty': 5,
    #     'category': 'slide',
    #     'stance': 'nollie'
    # },
    # 'switch BS noseslide': {
    #     'difficulty': 4,
    #     'category': 'slide',
    #     'stance': 'switch'
    # },
    'FS 50-50': {
        'difficulty': 1,
        'category': 'grind',
        'stance': 'regular'
    },
    'fakie FS 50-50': {
        'difficulty': 1,
        'category': 'grind',
        'stance': 'fakie'
    },
    'nollie FS 50-50': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'nollie'
    },
    'switch FS 50-50': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'switch'
    },
    'BS 50-50': {
        'difficulty': 1,
        'category': 'grind',
        'stance': 'regular'
    },
    # 'fakie BS 50-50': {
    #     'difficulty': 4,
    #     'category': 'grind',
    #     'stance': 'fakie'
    # },
    # 'nollie BS 50-50': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'nollie'
    # },
    'switch BS 50-50': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'switch'
    },
    'FS 5-0': {
        'difficulty': 1,
        'category': 'grind',
        'stance': 'regular'
    },
    'fakie FS 5-0': {
        'difficulty': 1,
        'category': 'grind',
        'stance': 'fakie'
    },
    'nollie FS 5-0': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'nollie'
    },
    'switch FS 5-0': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'switch'
    },
    'BS 5-0': {
        'difficulty': 1,
        'category': 'grind',
        'stance': 'regular'
    },
    # 'fakie BS 5-0': {
    #     'difficulty': 4,
    #     'category': 'grind',
    #     'stance': 'fakie'
    # },
    # 'nollie BS 5-0': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'nollie'
    # },
    'switch BS 5-0': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'switch'
    },
    'FS nosegrind': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'regular'
    },
    'fakie FS nosegrind': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'fakie'
    },
    'nollie FS nosegrind': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'nollie'
    },
    'switch FS nosegrind': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'switch'
    },
    'BS nosegrind': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'regular'
    },
    # 'fakie BS nosegrind': {
    #     'difficulty': 4,
    #     'category': 'grind',
    #     'stance': 'fakie'
    # },
    # 'nollie BS nosegrind': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'nollie'
    # },
    'switch BS nosegrind': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'switch'
    },
    'FS crooked grind': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'regular'
    },
    'fakie FS crooked grind': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'fakie'
    },
    'nollie FS crooked grind': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'nollie'
    },
    'switch FS crooked grind': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'switch'
    },
    'BS crooked grind': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'regular'
    },
    # 'fakie BS crooked grind': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'fakie'
    # },
    # 'nollie BS crooked grind': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'nollie'
    # },
    'switch BS crooked grind': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'switch'
    },
    'FS suski': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'regular'
    },
    'fakie FS suski': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'fakie'
    },
    'nollie FS suski': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'nollie'
    },
    'switch FS suski': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'switch'
    },
    'BS suski': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'regular'
    },
    # 'fakie BS suski': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'fakie'
    # },
    # 'nollie BS suski': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'nollie'
    # },
    'switch BS suski': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'switch'
    },
    'FS salad': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'regular'
    },
    'fakie FS salad': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'fakie'
    },
    'nollie FS salad': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'nollie'
    },
    'switch FS salad': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'switch'
    },
    'BS salad': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'regular'
    },
    # 'fakie BS salad': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'fakie'
    # },
    # 'nollie BS salad': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'nollie'
    # },
    'switch BS salad': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'switch'
    },
    'FS smith': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'regular'
    },
    'fakie FS smith': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'fakie'
    },
    'nollie FS smith': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'nollie'
    },
    'switch FS smith': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'switch'
    },
    'BS smith': {
        'difficulty': 4,
        'category': 'grind',
        'stance': 'regular'
    },
    # 'fakie BS smith': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'fakie'
    # },
    # 'nollie BS smith': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'nollie'
    # },
    'switch BS smith': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'switch'
    },
    'FS feeble': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'regular'
    },
    'fakie FS feeble': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'fakie'
    },
    'nollie FS feeble': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'nollie'
    },
    'switch FS feeble': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'switch'
    },
    'BS feeble': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'regular'
    },
    # 'fakie BS feeble': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'fakie'
    # },
    # 'nollie BS feeble': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'nollie'
    # },
    'switch BS feeble': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'switch'
    },
    'FS willy': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'regular'
    },
    'fakie FS willy': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'fakie'
    },
    'nollie FS willy': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'nollie'
    },
    'switch FS willy': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'switch'
    },
    'BS willy': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'regular'
    },
    # 'fakie BS willy': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'fakie'
    # },
    # 'nollie BS willy': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'nollie'
    # },
    'switch BS willy': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'switch'
    },
    'FS losi': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'regular'
    },
    'fakie FS losi': {
        'difficulty': 2,
        'category': 'grind',
        'stance': 'fakie'
    },
    'nollie FS losi': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'nollie'
    },
    'switch FS losi': {
        'difficulty': 4,
        'category': 'grind',
        'stance': 'switch'
    },
    'BS losi': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'regular'
    },
    # 'fakie BS losi': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'fakie'
    # },
    # 'nollie BS losi': {
    #     'difficulty': 5,
    #     'category': 'grind',
    #     'stance': 'nollie'
    # },
    'switch BS losi': {
        'difficulty': 3,
        'category': 'grind',
        'stance': 'switch'
    }
}
