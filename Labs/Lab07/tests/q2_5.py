test = {
  'name': 'q2_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You can think about the max of our sample being 135 as
          >>> # the chance of 135 being in our resample at least once.
          >>> abs(resampling_q5 - 0.6432138) < 0.001
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
