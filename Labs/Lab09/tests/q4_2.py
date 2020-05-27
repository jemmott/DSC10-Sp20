test = {
  'name': 'q4_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> true_predictions != []
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Try looking at the other statements, see if that can help you figure out
          >>> # why this prediction isn't reliable.
          >>> 1 in true_predictions
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Try looking at the other statements, see if that can help you figure out
          >>> # why this prediction isn't reliable.
          >>> 3 in true_predictions
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Are you sure? Try checking if the table has rows for duration 0, 2.5, and 60.
          >>> 4 in true_predictions
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Are you sure? Do we have data for durations less than 0? Greater than 60?
          >>> 5 in true_predictions
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(true_predictions) == {2}
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
