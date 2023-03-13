# from fastapi import FastAPI, Query, Path, File, UploadFile, Depends, Header, HTTPException
# from enum import Enum
# from typing import Optional, List
# from pydantic import BaseModel, Field
# from fastapi.responses import HTMLResponse

from fastapi import Depends, FastAPI, Header, HTTPException
app = FastAPI()


async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key



@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])

async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]


#-------------------------------------------
# app = FastAPI()
#
#
# @app.post("/files/")
# async def create_files(files: List[bytes] = File(...)):
#     return {"file_sizes": [len(file) for file in files]}
#
#
# @app.post("/uploadfiles/")
# async def create_upload_files(files: List[UploadFile] = File(...)):
#     return {"filenames": [file.filename for file in files]}
#
#
# @app.get("/")
# async def main():
#     content = """
# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)
#
#-------------------------------------------
#
# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"
#
# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#
# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
# @app.get("/auth")
# async def auth():
#     return "Hello World"
#
# # @app.get("/items/{item_id}")
# # async def read_item(item_id):
# #     return {"item_id": item_id}
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}
#
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}
#
#
# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}
#
# ##-------USA LA CLASE MODEL_NAME DECLARADA EN LA LINEA 4-------------------------
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     #if model_name == ModelName.alexnet:
#     if model_name.value == 'alexnet':
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#
#     return {"model_name": model_name, "message": "Have some residuals"}
#
#
# #--------------------------------------------------------
#
# # @app.get("/items/")
# # async def read_items(q: str = Query("fixedquery", min_length=3)):
# #     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
# #     if q:
# #         results.update({"q": q})
# #     return results
#
# # @app.get("/items/")
# # async def read_items(q: str = Query(..., min_length=3)):
# #     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
# #     if q:
# #         results.update({"q": q})
# #     return results
#
# # @app.get("/items/")
# # async def read_items(q: Optional[List[str]] = Query(None)):
# #     query_items = {"q": q}
# #     return query_items
#
#
# @app.get("/items/")
# async def read_items(
#     q: Optional[str] = Query(
#         None,
#         title="Query string",
#         description="Query string for the items to search in the database that have a good match",
#         min_length=3,
#     )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
#
#
# #------------------------------------
# @app.get("/items/{item_id}")
# async def read_items_path(
#     #item_id: int = Path(..., title="The ID of the item to get"),
#     #q: Optional[str] = Query(None, alias="item-query"),
#     #q: str, item_id: int = Path(..., title="The ID of the item to get")
#     #*, item_id: int = Path(..., title="The ID of the item to get"), q: str
#     *,
#     item_id: int = Path(..., title="The ID of the item to get", gt=0, le=1000),
#     q: str,
#     size: float = Query(..., gt=0, lt=10.5),
#
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results
#
# #--------------------------------------------------------
# class Item_4(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: float = 10.5
#
#
# items_1 = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
#     "baz": {
#         "name": "Baz",
#         "description": "There goes my baz",
#         "price": 50.2,
#         "tax": 10.5,
#     },
# }
#
#
# @app.get(
#     "/items/{item_id}/name",
#     response_model=Item_4,
#     response_model_include={"name", "description"},
# )
# async def read_item_name(item_id: str):
#     return items_1[item_id]
#
#
# @app.get("/items/{item_id}/public", response_model=Item_4, response_model_exclude={"tax"})
# async def read_item_public_data(item_id: str):
#     return items_1[item_id]
#
# ##-------USA LA CLASE ITEM DECLARADA EN LA LINEA 9-------------------------
#
# # @app.post("/items/")
# # async def create_item(item: Item):
# #     item_dict = item.dict()
# #     if item.tax:
# #         price_with_tax = item.price + item.tax
# #         item_dict.update({"price_with_tax": price_with_tax})
# #     return item_dict
# class Item_3(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: List[str] = []
#
# @app.post("/items/", response_model=Item_3)
# async def create_item(item: Item_3):
#     return item
#
# #------------------------------------------
#
# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
#     q: Optional[str] = None,
#     item: Optional[Item] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results
#
# #------------------------------------------
# class Item_2(BaseModel):
#     name: str = Field(..., example="Foo")
#     description: Optional[str] = Field(None, example="A very nice Item")
#     price: float = Field(..., example=35.4)
#     tax: Optional[float] = Field(None, example=3.2)
#
#
# @app.put("/items/{item_id}")
# async def update_item_field(item_id: int, item: Item_2):
#     results = {"item_id": item_id, "item": item}
#     return results