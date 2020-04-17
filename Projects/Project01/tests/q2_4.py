
test = {
  'name': 'q2_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be a dataframe
	>>> isinstance(processed_beaches, bpd.DataFrame)
	True
	>>> set(processed_beaches.columns) == {'COUNTY', 'PARKING', 'FEE'}
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
