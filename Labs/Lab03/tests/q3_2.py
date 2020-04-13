test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You either didn't add the 'Total_Pay_Dollars' column, or 
          >>> # you mislabeled it
          >>> 'Total_Pay_Dollars' in compensation.columns
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have the column in your table, but the values may be wrong
          >>> t = compensation.sort_values("Total_Pay_Dollars", ascending=False)
          >>> t.get('Total_Pay_Dollars').values[0] == 53250000.0
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
