'''
Created on Feb 5, 2024

@author: Pat Deegan
@copyright: Copyright (C) 2024 Pat Deegan, https://psychogenic.com
'''

from sexpdata import Symbol
ElementTemplate = {

    'wire': [Symbol('wire'), [Symbol('pts'), [Symbol('xy'), 0,0], [Symbol('xy'), 0, 2.54]], 
             [Symbol('stroke'), [Symbol('width'), 0], [Symbol('type'), Symbol('default')]], 
             [Symbol('uuid'), Symbol('ABC123')]],
    
    'global_label': [Symbol('global_label'), 'GLABEL', [Symbol('shape'), Symbol('input')], 
                     [Symbol('at'), 27.94, 33.02, 180], [Symbol('fields_autoplaced')], 
                     [Symbol('effects'), [Symbol('font'), [Symbol('size'), 1.27, 1.27]], 
                      [Symbol('justify'), Symbol('right')]], 
                     [Symbol('uuid'), Symbol('NANANA')], 
                     [Symbol('property'), 'Intersheetrefs', '${INTERSHEET_REFS}', 
                      [Symbol('at'), 21.6891, 33.02, 0], [Symbol('effects'), 
                    [Symbol('font'), [Symbol('size'), 1.27, 1.27]], 
                    [Symbol('justify'), Symbol('right')], Symbol('hide')]]],
    
    'label': [Symbol('label'), 'LABEL', 
              [Symbol('at'), 25.4, 25.4, 0], 
              [Symbol('fields_autoplaced')], 
              [Symbol('effects'), [Symbol('font'), [Symbol('size'), 1.27, 1.27]], 
               [Symbol('justify'), Symbol('left'), Symbol('bottom')]], 
              [Symbol('uuid'), Symbol('SOMEUUID')]],
    
    
    'text': [Symbol('text'), 'hello', [Symbol('at'), 58.42, 48.26, 0], 
             [Symbol('effects'), [Symbol('font'), [Symbol('size'), 2, 2], 
            [Symbol('thickness'), 0.4], Symbol('bold')], 
            [Symbol('justify'), Symbol('left'), Symbol('bottom')]], 
             [Symbol('uuid'), Symbol('TEXTUUID')]],
    
    
    'junction': [Symbol('junction'), [Symbol('at'), 50.8, 38.1], [Symbol('diameter'), 0], 
                 [Symbol('color'), 0, 0, 0, 0], 
                 [Symbol('uuid'), Symbol('JUNKID')]],

    'sheet': [
        Symbol('sheet'),
            [Symbol('at'), 280.416, 52.578],
            [Symbol('size'), 12.7, 3.81],
            [Symbol('fields_autoplaced')],
            [Symbol('stroke'),
                [Symbol('width'), 0.1524],
                [Symbol('type'), Symbol('solid')]
            ],
            [Symbol('fill'),
                [Symbol('color'), 0, 0, 0, 0.0000]
            ],
            [Symbol('uuid'), Symbol('SOMEUUID')],
            [Symbol('property'), 'Sheetname', 'usb',
                [Symbol('at'), 280.416, 51.8664, 0],
                [Symbol('effects'),
                    [Symbol('font'),
                        [Symbol('size'), 1.27, 1.27]
                    ],
                    [Symbol('justify'), Symbol('left'), Symbol('bottom')]
                ]
            ],
            [Symbol('property'), 'Sheetfile', 'default_usb.kicad_sch',
                [Symbol('at'), 280.416, 56.9726, 0],
                [Symbol('effects'),
                    [Symbol('font'),
                        [Symbol('size'), 1.27, 1.27]
                    ],
                    [Symbol('justify'), Symbol('left'), Symbol('top')]
                ]
            ]
    ]
}
