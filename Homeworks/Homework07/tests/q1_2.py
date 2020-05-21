test = {
  'name': 'Question 1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(boot_leads, np.ndarray)
          True
          >>> len(boot_leads) == 1000
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import numbers',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
