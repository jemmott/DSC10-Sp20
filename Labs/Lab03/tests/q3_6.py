test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure to remove the "(No previous year)" CEOs 
          >>> "(No previous year)" not in with_previous_compensation.get("% Change")
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import math
          >>> # You have the column, but some of your values may be wrong
          >>> t = with_previous_compensation.sort_values(by="Previous_Total_Pay", ascending=False)
          >>> value = t.get("Previous_Total_Pay").values[0]
          >>> math.isclose(value, 67700000.0, rel_tol = 1000)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have the column, but your number of rows is off
          >>> with_previous_compensation.shape[0] == 81
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
