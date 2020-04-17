test = {
  'name': 'Question 4_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> callable(mean_values)
          True
          >>> isinstance(mean_values('France'), float) or isinstance(mean_values('France'), int) or isinstance(mean_values('France'), np.integer)
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
