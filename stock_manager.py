"""
Refer to the assignment specification for more details
"""

from module03_stacks_and_queues.part00_preclass.stack import ArrayStack

class StockManager:

    __PROFIT = 0

    def __init__(self, o_name, o_surname):
        """
        Initialises the Stock Manager with the name and surname of the portfolio
        :param o_name: name of the owner of the porfolio
        :param o_surname: surname of the portfolio
        """
        self.o_name = o_name
        self.o_surname = o_surname
        self.google_stack = ArrayStack()
        self.apple_stack = ArrayStack()
        self.bmw_stack = ArrayStack()

    def buy_shares(self, company, number, buy_price):
        """
        Buy stocks
        :param company: the company of which shares are being bought
        :param number: the number of shares to buy
        :param buy_price: the price (per share) at which shares are bought
        """
        if company == "Google":
            self.google_stack.push([number, buy_price])
        elif company == "Apple":
            self.apple_stack.push([number, buy_price])
        else:
            self.bmw_stack.push([number, buy_price])



    def sell_shares(self, company, number, sell_price):
        """
        Sell shares (only if you have enough to sell!)
        :param company: the company of which shares are being bought
        :param number: the number of shares to buy
        :param sell_price: the price (per share) at which shares are sold
        """
        cur_profit = 0
        if company == "Google":
            while not self.google_stack.is_empty() and number > 0:
                if number >= self.google_stack.top()[0]:
                    number -= self.google_stack.top()[0]
                    cur_profit += self.google_stack.top()[0] * sell_price - self.google_stack.top()[0] * self.google_stack.top()[1]
                    self.google_stack.pop()

                else:
                    self.google_stack.top()[0] -= number
                    cur_profit += number * sell_price - number * self.google_stack.top()[1]
                    number = 0

            if number > 0:
                print("We don't have that amount of shares!")

            StockManager.__PROFIT += cur_profit
            return cur_profit

        elif company == "Apple":
            while not self.apple_stack.is_empty() and number > 0:
                if number >= self.apple_stack.top()[0]:
                    number -= self.apple_stack.top()[0]
                    cur_profit = self.apple_stack.top()[0] * sell_price - self.apple_stack.top()[0] * self.apple_stack.top()[1]
                    self.apple_stack.pop()
                else:
                    self.apple_stack.top()[0] -= number
                    cur_profit += number * sell_price - number * self.apple_stack.top()[1]
                    number = 0

            if number > 0:
                print("We don't have that amount of shares!")

            StockManager.__PROFIT += cur_profit
            return cur_profit

        else:
            while not self.bmw_stack.is_empty() and number > 0:
                if number >= self.bmw_stack.top()[0]:
                    number -= self.bmw_stack.top()[0]
                    cur_profit += self.bmw_stack.top()[0] * sell_price - self.bmw_stack.top()[0] * self.bmw_stack.top()[1]
                    self.bmw_stack.pop()
                else:
                    self.bmw_stack.top()[0] -= number
                    cur_profit += number * sell_price - number * self.bmw_stack.top()[1]
                    number = 0

            if number > 0:
                print("We don't have that amount of shares!")

            StockManager.__PROFIT += cur_profit
            return StockManager.__PROFIT


    def buy_multiple(self, company_list, number_list, price_list):
        for i in range(len(company_list)):
            self.buy_shares(company_list[i], number_list[i], price_list[i])


    def sell_multiple(self, company_list, number_list, price_list):
        cur_profit = 0
        for i in range(len(company_list)):
            cur_profit += self.sell_shares(company_list[i], number_list[i], price_list[i])
        return cur_profit

    def get_profit(self):
        return StockManager.__PROFIT


    """ allows to print the current stock held by the investor (name of stocks, numbers of stocks, and 
    prices at which they were bought)"""
    def print_portfolio(self):
        print("Google's ", end='')
        self.google_stack.print_contents()
        print("Apple's ", end='')
        self.apple_stack.print_contents()
        print("BMW's ", end='')
        self.bmw_stack.print_contents()






if __name__ == '__main__':
    # extend this code to test all the functions of your portfolio manager
    P = StockManager("Donald", "Trump")

    P.buy_shares("Google", 20, 100)
    P.buy_shares("Google", 20, 100)

    P.sell_shares("Google", 50, 100)

    print("Profit: {0}".format(P.sell_shares("Google", 5, 120)))
    print("Current cumulative profit: {0}".format(P.get_profit()))
    print("Profit: {0}".format(P.sell_shares("Google", 31, 127)))
    print("Current cumulative profit: {0}".format(P.get_profit()))
    print("Profit: {0}".format(P.sell_shares("Google", 2, 23)))
    print("Current cumulative profit: {0}".format(P.get_profit()))
    P.print_portfolio()

    P.sell_shares("Google", 50, 150)
    P.buy_multiple(["Google", "Apple"],[10, 56], [56, 27])
    P.sell_multiple(["Google", "Apple"], [1,1], [56, 27])
    P.print_portfolio()

    P.sell_shares("Google", 30, 100)

    
