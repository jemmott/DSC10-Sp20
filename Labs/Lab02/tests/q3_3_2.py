test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(imdb_by_name, bpd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # it seems that there are too many columns
          >>> imdb_by_name.shape == (250, 4)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # hmm, the index doesn't seem to have movie names
          >>> imdb_by_name.index[0] == 'M'
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
