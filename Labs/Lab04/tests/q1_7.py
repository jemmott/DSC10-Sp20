test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> (result == 'Wow!') or (result == 'Meh.') or (result == 'Okay!')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import babypandas as bpd
          >>> ten_nachos = np.array(['neither', 'cheese', 'both', 'both', 'cheese', 'salsa', 'both', 'neither', 'cheese', 'both'])
          >>> ten_nachos_reactions = bpd.DataFrame().assign(Nachos=ten_nachos)
          >>> ten_nachos_reactions = ten_nachos_reactions.assign(Reactions=ten_nachos_reactions.get("Nachos").apply(nacho_reaction))
          >>> both_or_neither(ten_nachos_reactions)
          'Wow!'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import babypandas as bpd
          >>> seven_nachos = np.array(['neither', 'cheese', 'both', 'both', 'neither', 'both', 'neither'])
          >>> seven_nachos_reactions = bpd.DataFrame().assign(Nachos=seven_nachos)
          >>> seven_nachos_reactions = seven_nachos_reactions.assign(Reactions=seven_nachos_reactions.get("Nachos").apply(nacho_reaction))
          >>> both_or_neither(seven_nachos_reactions)
          'Okay!'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
