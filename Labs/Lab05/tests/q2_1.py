test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> old = full_data.assign(Age=full_data.get('Age') * 3)
          >>> np.max(histograms(old)[0]) == np.max((old.get('Age')).values)
          True
          >>> np.min(histograms(old)[0]) == np.min(old.get('Age').values)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.max(histograms(full_data)[1]) > np.max(full_data.get('Salary').values)
          True
          >>> np.min(histograms(full_data)[1]) == np.min(full_data.get('Salary').values)
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
