from utils.docs import FastAPIRouteParameters


class RetrieveAccountDocs(FastAPIRouteParameters):
    status_code: int = 200


class ListAccountDocs(FastAPIRouteParameters):
    status_code: int = 200


class CreateAccountDocs(FastAPIRouteParameters):
    status_code: int = 201


class UpdateAccountDocs(FastAPIRouteParameters):
    status_code: int = 200


class DestroyAccountDocs(FastAPIRouteParameters):
    status_code: int = 204


retrieve_account_docs = RetrieveAccountDocs().model_dump()
list_account_docs = ListAccountDocs().model_dump()
create_account_docs = CreateAccountDocs().model_dump()
update_account_docs = UpdateAccountDocs().model_dump()
destroy_account_docs = DestroyAccountDocs().model_dump()
