try:
    from StringIO import StringIO
except ImportError:
    # Python 3 StringIO import
    from io import StringIO

from pytest import raises

from transactionpro.import_types import Invoice


def test_basic():
    invoice = Invoice()
    out = StringIO()
    invoice.add_row(customer='Joe', ref_number='1', item='Noodles')
    invoice.write_csv_to(out)
    expected = """Last Name,ShipTo Country,Memo,Exchange Rate,BillTo City,Other,Ship Method,Due Date,Fax,AR Account,BillTo State,ShipTo Line1,ShipTo Line2,ShipTo Line3,BillTo Line1,BillTo Line3,BillTo Line2,Ship Date,Phone,Serial /Lot Number,SO RefNumber,Customer,Sales Tax Item,Item,Service Date,Is Pending,BillTo PostalCode,Template Name,Customer Acct No,Currency,ShipTo PostalCode,Other1,Other2,Contact Name,First Name,Unit of Measure,Rep,ShipTo State,Inventory Site,Transaction Date,FOB,BillTo Line4,Email,Terms,Description,ShipTo Line4,Price,To Be E-Mailed,Item Line Class,Sales Tax Code,Customer Message,Class,To Be Printed,Inventory Bin,RefNumber,ShipTo City,PO Number,BillTo Country,Quantity\r
,,,,,,,,,,,,,,,,,,,,,Joe,,Noodles,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,1,,,,\r\n"""
    assert out.getvalue() == expected


def test_basic_array():
    invoice = Invoice()
    out = StringIO()
    for i in range(1000):
       invoice.add_row(customer='Joe', ref_number=str(i), item='Noodles')
    invoice.write_csv_to(out)
    result = out.getvalue()
    assert len(result.split('\n')) == 1002  # +1 for header, +1 for empty line at end


def test_missing_required():
    invoice = Invoice()
    with raises(KeyError):
        invoice.add_row(customer='Joe', ref_number='1')


def test_bad_kwarg():
    invoice = Invoice()
    with raises(KeyError):
        invoice.add_row(customer='Joe', ref_number='1', item='Noodles', joe='Mack')
