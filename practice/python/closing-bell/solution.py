def portfolio_profit_calculator(prices: dict[str, float], purchases: list[list]):
  latest_price = prices[max(prices)]
  total = 0 
  
  for date,quantity in purchases:
    total = total + quantity * (latest_price - prices[date])
    
  return total
    
