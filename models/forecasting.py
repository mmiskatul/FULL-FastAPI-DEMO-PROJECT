def forecast_stockout(sales_history, inventory):
    avg_daily_sales = sum(sales_history) / len(sales_history)
    days_left = inventory / avg_daily_sales
    return int(days_left)
