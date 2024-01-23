
from behave import *
from src.endpoints.boards import Board
@when('I create a new Board with name "{name}"')
def create_board(context, name):
    context.board = Board()
    response = context.board.create_board(name)
@then('the board name should be "{name}"')
def validate_board_name(context, name):
    assert context.board.get_board_name() == name

@step('closed response value is "{closed}"')
def validate_board_close(context, closed):
    assert context.board.get_board_close() == False

@given('I create a new Board with name "{name}"')
def create_new_board(context, name):
    context.board = Board()
    response = context.board.create_board(name)

@when('I should be able to update the board name to "{name_updated}"')
def update_board(context, name_updated):
    response = context.board.update_name_board(name_updated)

@when('I deleted the board created')
def delete_board(context):
    response = context.board.delete_board()

@then('check to verify if board was succesfully deleted')
def check_board_deleted(context):
    assert context.board.board_exist() == True

