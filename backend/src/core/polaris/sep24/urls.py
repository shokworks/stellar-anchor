from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from core.polaris.sep24.info import info
from core.polaris.sep24.fee import fee
from core.polaris.sep24.transaction import more_info, transaction, transactions
from core.polaris.sep24.withdraw import (
    withdraw,
    get_interactive_withdraw,
    post_interactive_withdraw,
    complete_interactive_withdraw,
)
from core.polaris.sep24.deposit import (
    deposit,
    complete_interactive_deposit,
    post_interactive_deposit,
    get_interactive_deposit,
)

SEP24_MORE_INFO_PATH = "transaction/more_info"

urlpatterns = [
    path("transactions/deposit/interactive", csrf_exempt(deposit)),
    path(
        "transactions/deposit/interactive/complete",
        complete_interactive_deposit,
        name="complete_interactive_withdraw",
    ),
    path(
        "transactions/deposit/webapp/submit",
        post_interactive_deposit,
        name="post_interactive_deposit",
    ),
    path(
        "transactions/deposit/webapp",
        get_interactive_deposit,
        name="get_interactive_deposit",
    ),
    path("transactions/withdraw/interactive", csrf_exempt(withdraw)),
    path(
        "transactions/withdraw/interactive/complete",
        complete_interactive_withdraw,
        name="complete_interactive_withdraw",
    ),
    path(
        "transactions/withdraw/webapp/submit",
        post_interactive_withdraw,
        name="post_interactive_withdraw",
    ),
    path(
        "transactions/withdraw/webapp",
        get_interactive_withdraw,
        name="get_interactive_withdraw",
    ),
    path("info", info),
    path("fee", fee),
    path("transaction", transaction),
    path("transactions", transactions),
    path(SEP24_MORE_INFO_PATH, more_info, name="more_info"),
]
