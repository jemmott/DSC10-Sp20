
test = {
  'name': 'q4_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be a dataframe
	>>> isinstance(energy, bpd.DataFrame)
	True
	>>> set(energy.columns) == {'BIOGAS', 'BIOMASS', 'GEOTHERMAL', 'SMALL HYDRO', 'SOLAR', 'SOLAR THERMAL', 'WIND TOTAL'}
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
