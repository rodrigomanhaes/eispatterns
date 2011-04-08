import sys
import inspect
from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
from bank_system.decorators.bank_account_decorator import BankAccountDecorator
from domain.supportive.contract_error import ContractError
from domain.base.decorator import Decorator

class RuleChecker:

    def __init__(self):
        self.allowable_decorators = []
        self.decorators = []

    def can_decorate(self,node):
        #works only for this module
        #self.decorators = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        #What is done below must be done through iterating through the decorators
        #module, checking every single class
        credit_analyst = CreditAnalystDecorator('x')
        try:
            credit_analyst.decorate(node)
        except:
            pass
        else:
            self.allowable_decorators.append(credit_analyst.__class__.__doc__)
        bank_account = BankAccountDecorator('x')
        try:
            bank_account.decorate(node)
        except:
            pass
        else:
            self.allowable_decorators.append(credit_analyst.__class__.__doc__)

    def find_decorators(self, module):
        for name in dir(module):
           obj = getattr(module, name)
           if inspect.isclass(obj):
               if issubclass(obj, Decorator):
                  #a class is a subclass of itself, thus:
                  if obj.__name__ != 'Decorator':
                     self.decorators.append(obj)

