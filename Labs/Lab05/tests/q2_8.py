test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Looks like you didn't declare `sampling_q8` to one of the options.
          >>> type(sampling_q8) == int
          True
          >>> 0 < sampling_q8 < 6
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Try running your cell multiple times to get new samples.
          >>> # In addition to looking at the histogram, look at the statistics.
          >>> sampling_q8 != 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Try running your cell multiple times to get new samples.
          >>> # In addition to looking at the histogram, look at the statistics.
          >>> sampling_q8 != 3
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Try running your cell multiple times to get new samples.
          >>> # In addition to looking at the histogram, look at the statistics.
          >>> sampling_q8 != 4
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Try running your cell multiple times to get new samples.
          >>> # In addition to looking at the histogram, look at the statistics.
          >>> sampling_q8 != 5
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
