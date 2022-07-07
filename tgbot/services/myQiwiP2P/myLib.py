import typing
from pyqiwip2p.p2p_types import Bill
import httpx
from pyqiwip2p.p2p_types import QiwiDatetime, QiwiCustomer


def myBill(bill_id="", amount="", comment="", currency='KZT',
           lifetime=30, expiration=None, auth_key="",
           customer: typing.Union[QiwiCustomer, dict] = None, fields: dict = None):
    alt = "qp2p.0708.su"
    amount_round = str(round(float(amount), 2))
    amount = (
        amount_round
        if len(str(float(amount)).split(".")[1]) > 1
        else str(round(float(amount), 2)) + "0"
    )

    expiration = (
        QiwiDatetime(moment=expiration).qiwi
        if expiration
        else QiwiDatetime(lifetime=lifetime).qiwi
    )

    qiwi_request_headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_key}",
    }

    qiwi_request_data = {
        "amount": {"currency": currency, "value": amount},
        "comment": comment,
        "expirationDateTime": expiration,
        "customer": customer.dict
        if type(customer) is QiwiCustomer
        else QiwiCustomer(json_data=customer).dict
        if customer
        else {},
        "customFields": fields,
    }
    client = httpx.Client()

    qiwi_raw_response = client.put(
        f"https://api.qiwi.com/partner/bill/v1/bills/{bill_id}",
        json=qiwi_request_data,
        headers=qiwi_request_headers,
    )
    qiwi_response = Bill(qiwi_raw_response, alt)
    return qiwi_response
