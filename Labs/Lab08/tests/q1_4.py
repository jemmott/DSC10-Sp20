test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 < q1_4 < 5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # What shape does the distribution need to be for this to be true?
          >>> # Do we know the shape of the distribution?
          >>> q1_4 != 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # We know that a certain of percentage of data falls within ± z, not just +
          >>> q1_4 != 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Take a look at Chebychev again!
          >>> q1_4 != 4
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