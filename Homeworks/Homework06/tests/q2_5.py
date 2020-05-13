test = {
  'name': 'Question 2_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(lower_bound, numbers.Real)
          True
          >>> isinstance(upper_bound, numbers.Real)
          True
          >>> upper_bound <= 100
          True
          >>> lower_bound <= 100
          True
          >>> upper_bound >= 0
          True
          >>> lower_bound >= 0
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import numbers',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
