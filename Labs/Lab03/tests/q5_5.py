test = {
  'name': 'Question 5_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # check if table has correct # of rows
          >>> install_stats.shape[0] == 6
          True
          >>> # check if "Install" column has correct data
          >>> 85711130 < install_stats.get(install_stats.columns[0]).sum() < 85711140
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
