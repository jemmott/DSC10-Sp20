test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Looks like you didn't declare `sampling_q5` to one of the options.
          >>> type(sampling_q5) == int
          True
          >>> 0 < sampling_q5 < 5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Careful, is this really an accurate representation?
          >>> sampling_q5 != 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Even relatively small samples can give good pictures!
          >>> sampling_q5 != 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Careful, is this really an accurate representation?
          >>> sampling_q5 != 3
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
