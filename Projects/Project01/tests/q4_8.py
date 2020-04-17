
test = {
  'name': 'q4_8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be a dataframe
	>>> isinstance(hourly_averages_july_2016, bpd.DataFrame)
	True
	>>> hourly_averages_july_2016.shape == (24, 7)
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
