def max_profit(stock_prices, start_index, end_index):
    # If the stocks can't be bought
    if end_index <= start_index:
        return 0
    
    maximum_profit = 0
    
    for i in range(start_index, end_index):
        for j in range(i + 1, end_index + 1):
            if stock_prices[j] > stock_prices[i]:
                # Update the current profit
                current_profit = stock_prices[j] - stock_prices[i] + \
                                 max_profit(stock_prices, start_index, i - 1) + \
                                 max_profit(stock_prices, j + 1, end_index)
                
                # Update the maximum profit so far
                maximum_profit = max(maximum_profit, current_profit)
    
    return maximum_profit


if __name__ == '__main__':
    stock_prices = [100, 180, 260, 310, 40, 535, 695]
    num_prices = len(stock_prices)
    
    print("Maximum Profit:", max_profit(stock_prices, 0, num_prices - 1))


# Answer: 865
