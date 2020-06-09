test = {
  'name': 'q4_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> zero_minute_predicted_waiting_time != (0*slope)+intercept
          False
          >>> two_point_five_minute_predicted_waiting_time == (2.5*slope)+intercept
          True
          >>> hour_predicted_waiting_time == (60*slope)+intercept
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
