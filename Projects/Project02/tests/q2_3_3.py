test = {
  'name': 'Question 2.3.3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numbers
          >>> callable(calculate_ci)
          True
          >>> lower, upper = calculate_ci(np.array([1, 2, 3, 4, 5, 6]))
          >>> isinstance(lower, numbers.Real)
          True
          >>> isinstance(upper, numbers.Real)
          True
          >>> lower_bound <= upper_bound
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
