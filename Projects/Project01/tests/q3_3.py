
test = {
  'name': 'q3_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be a dataframe
	>>> isinstance(sea_averages, bpd.DataFrame)
	True
	>>> set(sea_averages.columns) == {'TEMPERATURE', 'LEVEL'}
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
