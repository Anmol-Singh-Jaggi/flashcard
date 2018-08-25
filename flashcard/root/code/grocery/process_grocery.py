#!/usr/bin/env python3
from flask import Flask, render_template, request


def process_bill(lines):
    """
    Processes the bill input and returns the bill-split information.
    :param lines: The bill input lines.
        A line is of the format `num1 num2 num3 ... label-string`,
        denoting that the amounts (num1 + num2 + num3) has to be
        divided between the persons mentioned in the labels.
        For example, `12 34 55 AS` => 101 has to be divided between 'A' and 'S'.
    :type lines: A list of strings.
    :returns: A map of 'entity' vs 'amount'.
    """
    entity_vs_amount = {}
    for line_num, line in enumerate(lines):
        try:
            line_split = line.split()
            assert(len(line_split) > 1)
            amounts = line_split[:-1]
            entities = line_split[-1]
            amount = sum(float(num) for num in amounts)
            amount_per_entity = float(amount) / len(entities)
            for entity in entities:
                entity_amount = entity_vs_amount.get(entity, 0)
                entity_amount += amount_per_entity
                entity_vs_amount[entity] = entity_amount
        except Exception:
            exception_traceback = traceback.format_exc()
            error_msg = "Line #{} is malformed: '{}'\n\n{}".format(
                line_num + 1, line, exception_traceback)
            raise Exception(error_msg)

    return entity_vs_amount


def handle_GET():
    return render_template("index_grocery.html")


def handle_POST(request):
    bill_input = request.form["bill_input"]
    bill_lines = bill_input.split("\n")
    bill_lines = [line.strip() for line in bill_lines]
    try:
        entity_vs_amount = process_bill(bill_lines)
        total_amount = sum(entity_vs_amount.values())
        output = str(entity_vs_amount) + \
            "\n\nTotal amount = {}".format(total_amount)
    except Exception as e:
        output = "Error while processing input:\n\n---- start ----\n{}\n---- end ----\n\n{}".format(
            bill_input, e)
    return render_template("index_grocery.html", bill_input=bill_input, output=output)
