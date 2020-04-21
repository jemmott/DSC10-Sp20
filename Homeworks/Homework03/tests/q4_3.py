test = {
  'name': 'Question 4_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> callable(lastname_length)
          True
          >>> lastname_length('Quer, Giorgio') == 4
          True
          >>> lastname_length('Twomey, Robert') == 6
          True
          >>> lastname_length('Tiefenbruck, Janine') == 11
          True
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
