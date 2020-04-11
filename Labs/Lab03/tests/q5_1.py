test = {
  'name': 'Question 5_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import babypandas as bpd
          >>> isinstance(by_content, bpd.DataFrame)
          True
          >>> # check if it has correct # of rows
          >>> by_content.shape[0] == 6
          True
          >>> # check if you list alphabetically
          >>> by_content.get(by_content.columns[0]).index[0] == 'Adults only 18+'
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
