
test = {
  'name': 'q3_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be a dataframe
	>>> isinstance(sea_temp_kelvin, bpd.DataFrame)
	True
	>>> set(sea_temp_kelvin.columns) == {'YEAR', 'MONTH', 'DAY', 'SURFACE_TEMP_K'}
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
