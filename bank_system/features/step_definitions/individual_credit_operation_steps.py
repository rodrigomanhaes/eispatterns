# -*- coding: utf-8 -*-
from lettuce import step, world
from should_dsl import should
from domain.node.person import Person
from domain.node.machine import Machine
from domain.movement.process import Process
from domain.movement.transformation import Transformation
from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
from bank_system.decorators.bank_account_decorator import BankAccountDecorator

#It is not necessary to have a person and a machine, however they are created
#to show the whole process of decoration and use
@step(u'Given I am a registered Credit Analyst')
def given_i_am_a_registered_credit_analyst(step):
    world.person = Person()
    world.person.name = 'John'
    world.credit_analyst = CreditAnalystDecorator('09876-5')
    world.credit_analyst.decorate(world.person)

@step(u'And an individual customer with account number (.+) asks for a personal loan')
def and_an_individual_customer_with_account_number_account_number_asks_for_a_personal_loan(step, account_number):
    world.machine = Machine()
    world.account = BankAccountDecorator(account_number)
    world.account.decorate(world.machine)

@step(u'And the loan request is of (.+)')
def and_the_loan_request_is_of_desired_value(step, desired_value):
    #GUI action
    pass

@step(u'When I confirm the loan request')
def when_i_confirm_the_loan_request(step):
    #GUI action
    pass

@step(u'Then a new loan request with the (.+) and (.+) is created')
def then_a_new_loan_request_with_the_account_number_and_desired_value_is_created(step, account_number, desired_value):
    world.an_individual_credit_operation = Process()
    world.loan_request_creation = Transformation()

@step(u'And the new loan request is associated to the Credit Analyst')
def and_the_new_loan_request_is_associated_to_the_credit_analyst(step):
    pass

