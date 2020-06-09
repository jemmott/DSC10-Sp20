test = {
  'name': 'Question 3_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> callable(empirical_sd) # your answer should be a function called `empirical_sd`
          True
          >>> isinstance(empirical_sd(10), numbers.Real) # your function should output a number
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'teardown': '',
      'setup': 'import numbers',
      'type': 'doctest'
    }
  ]
}
