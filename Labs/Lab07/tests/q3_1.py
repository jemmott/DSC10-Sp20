test = {
  'name': 'q3_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.mean(example_estimates) > 0
          True
          >>> np.mean(example_estimates) < 2000
          True
          >>> np.mean(example_estimates) > 800
          True
          >>> np.mean(example_estimates) < 1200
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
