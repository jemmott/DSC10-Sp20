test = {
  'name': 'Question 2.3.7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(enrollment_explanations, list)
          True
          >>> all([x in (1,2,3,4) for x in totchol_diabp_explanations])
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
