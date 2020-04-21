test = {
  'name': '4.2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> species_abundance.shape[0]
          42
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> species_abundance.shape[1]
          3
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
