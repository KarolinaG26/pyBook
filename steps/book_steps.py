from behave import given, when, then
from book import Book

@given('I have a book titled "{title}" by "{author}" published in {year:d}')
def step_impl(context, title, author, year):
    context.book = Book(title, author, year)

@when('I get the book information')
def step_impl(context):
    context.info = context.book.get_info()

@then ('The information should by "{info}"')
def step_iml(context, info):
    assert context.info == info
