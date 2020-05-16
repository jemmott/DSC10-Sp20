test = {
  'name': 'Question 4.2.3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sorted(summed_mn_data.columns) == ['Died', 'Participated']
          True
          >>> int(summed_mn_data.get('Died').sum())
          467
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
