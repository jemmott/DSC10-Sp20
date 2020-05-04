test = {
  'name': 'Question 1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> int(round(test_statistic(.6,.5) + test_statistic(.4,.1),1))
          40
          >>> int(test_statistic(.4,.1) - test_statistic(.1,.4))
          0
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
