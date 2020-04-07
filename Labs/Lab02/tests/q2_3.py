test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> try:
          ...     fifteen_year_growth_rate
          ... except NameError:
          ...     pass
          ... else:
          ...     print((3.177 < fifteen_year_growth_rate < 3.178) or (116.39 < fifteen_year_growth_rate < 116.40))
          ... try:
          ...     fifty_year_growth_rate
          ... except NameError:
          ...     pass
          ... else:
          ...     print((3.177 < fifty_year_growth_rate < 3.178) or (116.39 < fifty_year_growth_rate < 116.40))
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