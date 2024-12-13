from utils.docs import FastAPIRouteParameters


class RetrieveTagDocs(FastAPIRouteParameters):
    status_code: int = 200


class ListTagDocs(FastAPIRouteParameters):
    status_code: int = 200


class CreateTagDocs(FastAPIRouteParameters):
    status_code: int = 201


class UpdateTagDocs(FastAPIRouteParameters):
    status_code: int = 200


class DestroyTagDocs(FastAPIRouteParameters):
    status_code: int = 204


retrieve_tag_docs = RetrieveTagDocs().model_dump()
list_tag_docs = ListTagDocs().model_dump()
create_tag_docs = CreateTagDocs().model_dump()
update_tag_docs = UpdateTagDocs().model_dump()
destroy_tag_docs = DestroyTagDocs().model_dump()
