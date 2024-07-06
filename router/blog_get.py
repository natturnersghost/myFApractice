from fastapi import FastAPI, APIRouter, status, Response, Depends
from typing import Optional, List
from enum import Enum
from router.blog_post import required_functionality
# enum means a set of symbolic names bound to unique, constant values
# ex ->
# Class Color(Enum):
  # RED = 1
  # GREEN = 2
  # BLUE = 3

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

@router.get('/all',
         # 'summary' and 'description' provide optional documentation for the function, description is longer
         summary=" retrieve all blogs",
         description=" this api call simulates retrieving all blogs",
         # info about the output of the function is 'response_description'
         response_description=" the list of availible blogs"
         )

# 'page' has a default value, 'page_size' does not, it's optional and must be an int
# 'Depends' keyword is what allows me to use the imported function required_functionality
def get_all_blogs(page = 1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
    return {'message': f'all {page_size} blogs on page {page}', 'req': req_parameter}

@router.get('/{id}/comments/{comment_id}', tags=['comment'])
# 'id' and 'comment_id' are path parameters
# path parameters are required
# valid and username are query parameters   
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    # triple quotes provide a description
    """ 
        simulates recieving a comment
        - **id**: mandatory path parameter
        - **comment_id**: mandatory path parameter
        - **valid**: optional query parameter
        - **username**: optional query parameter
    """
    return{'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

class BlogType(str, Enum): 
    short = 'short'
    story = 'story' 
    howto = 'howto'
    
@router.get('/type/{type}')    
def get_blog_type(type: BlogType, req_parameter: dict = Depends(required_functionality)):
    return {'message': f'blogs of type: {type}'}

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id < 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'blog with id: {id}'} 

