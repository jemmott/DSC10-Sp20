test = {
  'name': 'Question 2.3.6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numbers
          >>> len(enrollment_ci_by_region)
          9
          >>> all([x[0] <= x[1] for x in totchol_ci_by_diabp])
          True
          >>> len(enrollment_mean_by_region)
          9
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
