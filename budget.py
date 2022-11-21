class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __repr__(self):
        title = f'{self.name:*^30}'
        items = ''
        total = 0
        for item in self.ledger:
            amount_float = "{:.2f}".format(item['amount'])
            items += f"{item['description'][:23]}{amount_float[:7]:>{30-len(item['description'][:23])}}\n"
            total += item['amount'] 
        total = "{:.2f}".format(total)    
        items += f"Total: {total}"
        line = f"{title}\n{items}"
        return line
        
        
    def deposit(self, amount, description=''):
        self.ledger.append({'amount':amount, 'description':description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount':-amount, 'description':description}) 
            return True
        else:
            return False    

    def get_balance(self):
        self.balance = 0
        for item in self.ledger:
            self.balance += item['amount']
        return self.balance  
        #print('El balance de {} es: '.format(self.name) + str(self.balance))
                    
    def transfer(self, amount, budget):
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to {}'.format(budget.name))
            budget.deposit(amount, 'Transfer from {}'.format(self.name))
            return True 
        return False
          

    def check_funds(self, amount):
        self.get_balance()
        if amount > self.balance:
            return False
        else:
            return True

def create_spend_chart(categories):
    total_wd = 0
    withdraws = {} 
    wd_percent = {}
    for cat in categories:
        cat_wd = 0
        for i in cat.ledger:
            if i['amount'] < 0:
                cat_wd += i['amount'] * (-1)
                total_wd += i['amount'] *(-1)
        withdraws[cat.name] = cat_wd 
    for cat in categories:
        wd_percent[cat.name] = (withdraws[cat.name] * 100 / total_wd)
    graph = 'Percentage spent by category\n'
    for n in range(100, -10, -10):
        bar_len = 1
        graph += f'{str(n)+"|":>4} '
        for val in wd_percent.values():
            if n < val:
                graph += 'o  '  
            else:
                graph += '   '
            bar_len += 3    
        graph += '\n'
    graph += '    '      
    graph += ('-' * bar_len) + '\n'   
    
    cat_max = 0
    words_bars = ''
    for cat in categories:
        if len(cat.name) > cat_max:
            cat_max = len(cat.name)
    for n in range(cat_max):
        letters = '     '
        for cat in categories:
            if n >= len(cat.name):
                letters += "   "                
            else: 
                letters += cat.name[n] + '  '
        if n != (cat_max-1):
            letters += '\n'
        words_bars += letters        
    graph += words_bars
    return graph
