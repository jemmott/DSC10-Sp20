test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(top_10_movies, bpd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # make sure that you are assigning both columns
          >>> top_10_movies.shape == (10, 2)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # make sure that you are assigning both columns
          >>> top_10_movies.shape == (10, 2)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # hmm, the column names don't look exactly right
          >>> set(top_10_movies.columns) == {'Name', 'Rating'}
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
