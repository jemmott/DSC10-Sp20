test = {
  'name': 'q3_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 < simulating_q5 < 5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Careful, what if we get a really bad sample?
          >>> # What is the definition of the "95% confidence interval"?
          >>> simulating_q5 != 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # What is the definition of the "95% confidence interval"?
          >>> simulating_q5 != 3
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # What is the definition of the "95% confidence interval"?
          >>> simulating_q5 != 4
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

