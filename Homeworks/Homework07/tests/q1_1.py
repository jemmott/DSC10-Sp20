test = {
  'name': 'Question 1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0.0 <= lower_bound <= upper_bound <= 1.0
          True
          >>> isinstance(lower_bound, numbers.Real)
          True
          >>> isinstance(upper_bound, numbers.Real)
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
