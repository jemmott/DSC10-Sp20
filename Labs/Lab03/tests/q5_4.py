test = {
  'name': 'Question 5_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # check if table has correct # of rows
          >>> top_communication_apps.shape[0] == 3
          True
          >>> # check if "count" column has correct data
          >>> top_communication_apps.get(top_communication_apps.columns[0]).sum() == 268
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
