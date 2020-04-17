
test = {
  'name': 'q3_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be a dataframe
	>>> isinstance(sea_averages_added, bpd.DataFrame)
	True
	>>> set(sea_averages_added.columns) == {'TEMPERATURE', 'LEVEL','INCREASE'}
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
