test = {
  'name': 'q3_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure your column labels are correct.
          >>> faithful_predictions.columns.values == ('duration', 'wait', 'predicted_wait')
          array([ True,  True,  True])
          >>> faithful_predictions.iloc[:, 2].mean() < 71
          True
          >>> faithful_predictions.iloc[:, 2].mean() < 70
          False
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
