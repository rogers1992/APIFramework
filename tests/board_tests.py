from src.endpoints.boards import Board
board  = Board()
def test_create_board():
    response = board.create_board("testPython1")
    print(response.status_code)
    print(response.url)
    print(response.json())
def test_update_name_board():
    response = board.update_name_board("updatedTestPython")
    print(response.status_code)
    print(response.url)
    print(response.json())
def test_delete_board():
     response = board.delete_board()
     print(response.status_code)
     print(response.url)
     print(response.json())