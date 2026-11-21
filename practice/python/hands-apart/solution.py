def clock_angle(hour: int, minute: int) -> float:
  position_hour = (hour%12)*30 + minute*0.5
  position_minute = minute*6
  diff = abs(position_hour - position_minute)

  return min(diff, 360-diff)
