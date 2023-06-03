import dbhelpers

def get_all_books():
    results = dbhelpers.run_procedure('call get_all_books()',[])
    print(results)

get_all_books()