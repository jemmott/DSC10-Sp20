test = {
  'name': 'q2_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Examine the histogram again, think about what .sample() does.
          >>> 2 not in true_statements
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Examine the histogram again.
          >>> 3 not in true_statements
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(true_statements) == set([1, 4])
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
