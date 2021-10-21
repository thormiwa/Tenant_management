import frappe

def get_context(context):
    properties = frappe.db.sql(""" SELECT property_name, address, image, property_price, status FROM `tabProperty`;""", as_dict=True)
    context.properties = properties

    return context