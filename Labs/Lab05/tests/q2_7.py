test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Looks like you didn't declare `sampling_q7` to one of the options.
          >>> type(sampling_q7) == int
          True
          >>> 0 < sampling_q7 < 5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Try running your cell multiple times to get new samples.
          >>> sampling_q7 != 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # In addition to looking at the histograms, look at the statistics.
          >>> sampling_q7 != 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Try running your cell multiple times to get new samples.
          >>> sampling_q7 != 4
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
