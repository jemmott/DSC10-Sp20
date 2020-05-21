test = {
  'name': 'Question 2_1a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(course_means, bpd.DataFrame)
          True
          >>> set(course_means.columns.values) == set(['Study Hrs/wk', 'grades'])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
