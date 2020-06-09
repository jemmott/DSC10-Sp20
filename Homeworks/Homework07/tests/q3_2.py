test = {
  'name': 'Question 3_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> callable(predict_sd) # your answer should be a function called `predict_sd`
          True
          >>> isinstance(predict_sd(10), numbers.Real) # your function should output a number
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
