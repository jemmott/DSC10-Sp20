test = {
  'name': 'q3_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.mean(bootstrap_estimates) > 0
          True
          >>> np.mean(bootstrap_estimates) < 200
          True
          >>> np.mean(bootstrap_estimates) > 110
          True
          >>> np.mean(bootstrap_estimates) < 130
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
