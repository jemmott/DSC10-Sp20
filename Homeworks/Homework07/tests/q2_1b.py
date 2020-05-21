test = {
  'name': 'Question 2_1b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(writing_fixed, bpd.DataFrame)
          True
          >>> set(writing_fixed.columns.values) == {'Study Hrs/wk', 'course', 'grades'}
          True
          >>> isinstance(course_means_fixed, bpd.DataFrame)
          True
          >>> set(course_means_fixed.columns.values) == {'Study Hrs/wk', 'grades'}
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
