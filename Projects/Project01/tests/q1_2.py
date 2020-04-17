
test = {
  'name': 'q1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be a dataframe
	>>> isinstance(us_land_renamed, bpd.DataFrame)
	True
	>>> set(us_land_renamed.columns) == {'State', 'Class', 'EcologicalSystem', 'SquareMiles'}
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
