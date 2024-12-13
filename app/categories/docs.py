from utils.docs import FastAPIRouteParameters


class RetrieveCategoryDocs(FastAPIRouteParameters):
    status_code: int = 200


class ListCategoryDocs(FastAPIRouteParameters):
    status_code: int = 200


class CreateCategoryDocs(FastAPIRouteParameters):
    status_code: int = 201


class UpdateCategoryDocs(FastAPIRouteParameters):
    status_code: int = 200


class DestroyCategoryDocs(FastAPIRouteParameters):
    status_code: int = 204


retrieve_category_docs = RetrieveCategoryDocs().model_dump()
list_category_docs = ListCategoryDocs().model_dump()
create_category_docs = CreateCategoryDocs().model_dump()
update_category_docs = UpdateCategoryDocs().model_dump()
destroy_category_docs = DestroyCategoryDocs().model_dump()
