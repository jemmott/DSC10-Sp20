
test = {
  'name': 'q4_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be a dataframe
	>>> isinstance(energy_with_time, bpd.DataFrame)
	True
	>>> energy_with_time.shape == (67584, 11)
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
