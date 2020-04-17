
test = {
  'name': 'q1_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be a dataframe
	>>> isinstance(ca_classes, bpd.DataFrame)
	True
	>>> set(ca_classes.columns) == {'SquareMiles', 'Percentage'}
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
