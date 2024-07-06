from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from fastapi.params import Body
from typing import Optional, List, Dict




router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class Image(BaseModel):
    url: str
    alias: str
# each blog post is basically an instance of this. 
class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1':'val1'}
    image: Optional[Image] = None

@router.post('/new/{id}') # id is a path parameter
def create_blog(blog: BlogModel, id: int, version: int = 1): # version is a query parameter

   # this is what the url looks like for id 3 version 12 'http://localhost:8000/blog/new/3?version=12'
    return {
        'id': id,
        'data': blog,
        'version': version
        }
    
@router.post('/new/{id}/comment/{comment_id}')  
def create_comment(blog: BlogModel, id: int, 
        comment_title: int = Query(None,
            # metadata for the comment id                    
            title='comment id',
            description='description of the comment_title',
            alias='commentTitle',
            deprecated=True
        ),
        # the 'Elipsis' or '...' makes it a required field meaning if you remove it you get an error
        content: str = Body (...,
            # these are validators for the content field
            min_length=10,
            max_length=120,
            # some fucking how this nonsense below means only allow a-z spaces and star
            regex='^[a-z\s]*$'
        ),
        # the fuking v parameter is not giving me the option to add multiple strings 
        v: Optional[List[str]] = Query(['1.0','1.1','1.2']),
        # 'gt' is greater than, 'le' is less than or equal to
        # when I pass in 'None' as the default value like the guy in the video I get an Error "Path parameter cannot have default value"
        # fuckly no shit  # idfk 
        comment_id: int = Path(gt=5, le=10)
    ):
    return {
      'blog': blog, 
      'id': id,
      'comment_title': comment_title,
      'content': content,
      'version': v,
      'comment_id': comment_id,
    }

def required_functionality():
    return {'message':'butt'}