test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(with_ranking, bpd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # make sure that you are assigning both columns
          >>> with_ranking.shape == (10, 3)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # hmm, the column names don't look exactly right
          >>> set(with_ranking.columns) == {'Name', 'Rating', 'Ranking'}
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
