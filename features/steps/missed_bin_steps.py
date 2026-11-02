##verification
from behave import given, when, then
from resident_service import submit_missed_bin_report


@given('the resident provides their name "{name}"')
def step_resident_name(context, name):
    context.name = name


@given('the resident provides their postcode "{postcode}"')
def step_resident_postcode(context, postcode):
    context.postcode = postcode


@given('the resident selects the bin type "{bin_type}"')
def step_bin_type(context, bin_type):
    context.bin_type = bin_type


@given('the resident provides the missed collection date "{date}"')
def step_collection_date(context, date):
    context.date = date


@when('the resident submits the report')
def step_submit_report(context):
    context.result = submit_missed_bin_report(
        context.name,
        context.postcode,
        context.bin_type,
        context.date
    )


@then('the report should be accepted')
def step_report_accepted(context):
    assert context.result["accepted"] is True


@then('the report should be rejected')
def step_report_rejected(context):
    assert context.result["accepted"] is False


@then('a confirmation message should be displayed')
def step_confirmation(context):
    assert context.result["message"] == (
        "Missed bin collection report submitted successfully"
    )


@then('an error message "{message}" should be displayed')
def step_error_message(context, message):
    assert context.result["message"] == message
