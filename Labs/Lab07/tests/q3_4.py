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
          >>> 0 < stdv < 20
          True
          >>> 0 < new_right_end - new_left_end < 90
          True
          >>> len(new_bootstrap_estimates) == 5000
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
