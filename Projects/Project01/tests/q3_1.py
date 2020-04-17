
test = {
  'name': 'q3_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be a dataframe
	>>> isinstance(sea_level_rounded, bpd.DataFrame)
	True
	>>> set(sea_level_rounded.columns) == {'year', 'month', 'level'}
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
