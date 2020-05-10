test = {
  'name': 'q3_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from numpy import std
          >>> stdv = new_bootstrap_estimates.std()
          >>> 10 < stdv < 20
          True
          >>> 45 < new_right_end - new_left_end < 90
          True
          >>> abs(((new_right_end - new_left_end) / stdv) - 3.9) < 0.2
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
