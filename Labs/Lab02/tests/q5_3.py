test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # you should use the year column, not the decade column.
          >>> # but because of a mistake in the lab, both answers are accepted.
          >>> np.isclose(average_20th_century_rating, 8.274208144) or np.isclose(average_20th_century_rating, 8.280113636363636)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # you should use the year column, not the decade column.
          >>> # but because of a mistake in the lab, both answers are accepted.
          >>> np.isclose(average_21st_century_rating, 8.2) or np.isclose(average_21st_century_rating, 8.23108108108108)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
