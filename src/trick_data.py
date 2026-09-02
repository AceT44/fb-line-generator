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

}
