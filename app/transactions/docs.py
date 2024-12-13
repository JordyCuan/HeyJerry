from utils.docs import FastAPIRouteParameters


class RetrieveTransactionDocs(FastAPIRouteParameters):
    status_code: int = 200


class ListTransactionDocs(FastAPIRouteParameters):
    status_code: int = 200


class CreateTransactionDocs(FastAPIRouteParameters):
    status_code: int = 201


class UpdateTransactionDocs(FastAPIRouteParameters):
    status_code: int = 200


class DestroyTransactionDocs(FastAPIRouteParameters):
    status_code: int = 204


retrieve_transaction_docs = RetrieveTransactionDocs().model_dump()
list_transaction_docs = ListTransactionDocs().model_dump()
create_transaction_docs = CreateTransactionDocs().model_dump()
update_transaction_docs = UpdateTransactionDocs().model_dump()
destroy_transaction_docs = DestroyTransactionDocs().model_dump()
