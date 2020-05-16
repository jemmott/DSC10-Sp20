test = {
  'name': 'Question 2.2.5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> _colleges_sim1 = simulate_colleges_null()
          >>> _colleges_sim2 = simulate_colleges_null()
          >>> _colleges_sim1 != _colleges_sim2
          True
          >>> _colleges_sim1 < colleges_observed_statistic and _colleges_sim2 < colleges_observed_statistic
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
