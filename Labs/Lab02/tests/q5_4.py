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
          >>> np.isclose(proportion_in_20th_century, 0.884) or np.isclose(proportion_in_20th_century, 0.704)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # you should use the year column, not the decade column.
          >>> # but because of a mistake in the lab, both answers are accepted.
          >>> np.isclose(proportion_in_21st_century, 0.116) or np.isclose(proportion_in_21st_century, 0.296)
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
