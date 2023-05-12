from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):  
    
    # This line sets the number of items to be returned in each page to 3.
    page_size = 3

    ''' This line specifies the field to be used for ordering the results. 
    In this case, the results will be ordered by the name field.'''

    ordering = 'name'

    '''This line sets the query parameter to be used for the cursor. 
    By default, the query parameter is cursor, but this line changes it to cu.'''
    
    cursor_query_param = 'cu'